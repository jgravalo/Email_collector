from base import Classifier, NaturalLanguageConfigParser, ClassifierDeserializer
import requests
import re

# --- KeywordClassifier ---

class KeywordClassifier(Classifier):
    def __init__(self, field: str, operator: str, value: str, category: str):
        self.field = field
        self.operator = operator
        self.value = value.lower()
        self.category = category

    def classify(self, email) -> str | None:
        field_value = getattr(email, self.field, "").lower()
        if self.operator == "contains":
            if self.value in field_value:
                return self.category
        elif self.operator == "equals":
            if self.value == field_value:
                return self.category

        return None

# --- RuleBasedClassifier ---

class RuleBasedClassifier(Classifier):
    def __init__(self, rules: list[Classifier], default_classifier: Classifier | None = None):
        self.rules = rules
        self.default_classifier = default_classifier

    def classify(self, email) -> str | None:
        for rule in self.rules:
            categoria = rule.classify(email)
            if categoria is not None:
                return categoria
        if self.default_classifier is not None:
            return self.default_classifier.classify(email)
        return None


# --- APIClassifier ---

class APIClassifier(Classifier):
    def __init__(self, api_url: str = "http://localhost:8000/classify-email"):
        self.api_url = api_url

    def classify(self, email) -> str | None:
        try:
            response = requests.post(
                self.api_url,
                json={
                    "client_id": email.client_id,
                    "fecha_envio": email.fecha_envio.isoformat(),  # <-- fix
                    "email_body": email.body,
                },
                timeout=5
            )
        except Exception as e:
            print(f"[APIClassifier] Error llamando a la API: {e}")
        return None


# --- NaturalLanguageConfigParser ---

class SimpleNaturalLanguageConfigParser(NaturalLanguageConfigParser):
    def parse(self, text: str) -> dict:
        import re

        rules = []
        default = False

        field_map = {
            "remitente": "sender",
            "asunto": "subject",
            "cuerpo": "body",
            "sender": "sender",
            "subject": "subject",
            "body": "body"
        }

        # sentences = text.lower().split(".")
        # sentences = [text.lower()]
        sentences = [line.strip() for line in text.lower().splitlines() if line.strip()]
        
        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence:
                continue

            # patrón 1: si el asunto contiene la palabra "urgente", clasificarlo como "urgente"
            match = re.match(
                r'(?:si|if)\s+(?:el|the)\s+(\w+)\s+'
                r'(?:contiene|happens to contain)\s+(?:la palabra|the word)?\s*["“”](.+?)["“”],?'
                r'\s*(?:clasificarlo|classify it)?\s*(?:como|as)?\s*["“”](.+?)["“”]',
                sentence
            )
            if match:
                field, value, category = match.groups()

                field = field_map.get(field, field)
                rules.append({
                    "field": field,
                    "operator": "contains",
                    "value": value.strip(),
                    "category": category.strip()
                })
                print(f"DEBUG (pattern1): {rules[-1]}")
                continue

            # patrón 2: si el asunto es "xyz", clasificarlo como "abc"
            match = re.match(
                r'(?:si|if)\s+(?:el|the)\s+(\w+)\s+'
                r'(?:es|is)\s+["“”](.+?)["“”],?'
                r'\s*(?:clasificarlo|classify it)?\s*(?:como|as)?\s*["“”](.+?)["“”]',
                sentence
            )
            if match:
                field, value, category = match.groups()
                field = field_map.get(field, field)
                rules.append({
                    "field": field,
                    "operator": "equals",
                    "value": value.strip(),
                    "category": category.strip()
                })
                print(f"DEBUG (pattern2): {rules[-1]}")
                continue

            # patrón 3: primera regla: asigna la categoría "abc" si el remitente es "xyz"
            match = re.match(
                r'(?:primera|segunda|tercera)?\s*regla:?\s*asigna la categor[ií]a\s+["“”](.+?)["“”]\s+si el\s+(\w+)\s+(?:es|contiene)\s+["“”](.+?)["“”]',
                sentence
            )
            if match:
                category, field, value = match.groups()
                field_map = {
                    "remitente": "sender",
                    "asunto": "subject",
                    "cuerpo": "body",
                    "sender": "sender",
                    "subject": "subject",
                    "body": "body"
                }
                field = field_map.get(field, field)
                operator = "equals" if "es" in sentence else "contains"
                rules.append({
                    "field": field,
                    "operator": operator,
                    "value": value.strip(),
                    "category": category.strip()
                })
                print(f"DEBUG (pattern3): {rules[-1]}")
                continue
            else:
                print("DEBUG no matcheado:", sentence)


            # fallback
            if "usar el clasificador por defecto" in sentence or "use the default classifier" in sentence:
                default = True
                print("DEBUG: usando fallback a default classifier")

        return {
            "rules": rules,
            "default": default
        }

# --- ClassifierDeserializer ---

class SimpleClassifierDeserializer(ClassifierDeserializer):
    def deserialize(self, config: dict) -> Classifier:
        rules = []
        for rule_conf in config.get("rules", []):
            rules.append(
                KeywordClassifier(
                    field=rule_conf["field"],
                    operator=rule_conf["operator"],
                    value=rule_conf["value"],
                    category=rule_conf["category"]
                )
            )
        
        fallback = None
        if config.get("default", False):
            fallback = APIClassifier()
        
        return RuleBasedClassifier(rules, default_classifier=fallback)
