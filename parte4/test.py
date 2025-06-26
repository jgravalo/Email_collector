import unittest
from datetime import datetime

from base import (
    ClassifierDeserializer,
    Email,
    NaturalLanguageConfigParser,
    WrappedClassifier,
)
from dependencies import get_nl_config_parser, get_classifier_deserializer


class TestNaturalLanguageClassifier(unittest.TestCase):

    _nl_config_parser: NaturalLanguageConfigParser
    _classifier_deserializer: ClassifierDeserializer

    _sample_email_1: Email

    def setUp(self) -> None:
        self._nl_config_parser = get_nl_config_parser()
        self._classifier_deserializer = get_classifier_deserializer()
        self._sample_email_1 = Email(
            client_id=1,
            subject="Urgente",
            body="Oferta",
            sender="test@gmail.com",
            fecha_envio=datetime.now()
        )

    def test_single_rule(self) -> None:
        nl_description = """
        Si el asunto contiene la palabra “Urgente”, clasificarlo como “urgente”. 
        Si el cuerpo contiene la palabra “oferta”, clasificarlo como “promo”. 
        Si no, usar el clasificador por defecto.
        """
        classifier = self._build_classifier(nl_description)
        self.assertEqual("urgente", classifier.classify(self._sample_email_1))

    def test_second_rule(self) -> None:
        nl_description = """
        Si el cuerpo contiene la palabra “virus”, clasificarlo como “spam”.
        Si el asunto contiene la palabra “Urgente”, clasificarlo como “urgente”.  
        Si no, usar el clasificador por defecto.
        """
        classifier = self._build_classifier(nl_description)
        self.assertEqual("urgente", classifier.classify(self._sample_email_1))

    def test_no_category(self) -> None:
        # Es posible dejar un correo sin categorizar si no encaja con ninguna regla (categoria=None).
        nl_description = """
        Si el cuerpo contiene la palabra “virus”, clasificarlo como “spam”.
        Si el asunto contiene la palabra “oferta”, clasificarlo como “promo”.
        """
        classifier = self._build_classifier(nl_description)

        empty_email = Email(client_id=1, subject="", body="", sender="", fecha_envio=datetime.now())
        self.assertEqual(None, classifier.classify(empty_email))

    def test_subject_is(self) -> None:
        nl_description = """
        Si el asunto es “Su teléfono está infectado”, clasificarlo como “spam”.
        Si no, usar el clasificador por defecto.
        """
        classifier = self._build_classifier(nl_description)

        email = Email(client_id=1, subject="Su teléfono está infectado", body="", sender="", fecha_envio=datetime.now())

        self.assertEqual("spam", classifier.classify(email))

    def test_default_classifier(self) -> None:
        nl_description = """
        Usa siempre el clasificador por defecto.
        """

        classifier = self._build_classifier(nl_description)

        email = Email(
            client_id=8,  # este cliente tiene impagos, el clasificador de la parte 1 no debería clasificarlo
            subject="",
            body="",
            sender="test@gmail.com",
            fecha_envio=datetime.now()
        )

        self.assertEqual(None, classifier.classify(email))

    def test_english(self) -> None:
        nl_description = """
        If the subject happens to contain the word “CNMC”, classify it as “cnmc”. 
        If the body contains the word “offer”, classify it as “promo”. 
        If the sender is "julian@gmail.com", classify it as “blacklist”.
        If not, use the default classifier.
        """
        classifier = self._build_classifier(nl_description)

        email = Email(client_id=1, subject="Hello", body="Hello", sender="julian@gmail.com", fecha_envio=datetime.now())
        self.assertEqual("blacklist", classifier.classify(email))

    def test_different(self) -> None:
        nl_description = """
        Primera regla: asigna la categoría "blacklist" si el remitente es "julian@gmail.com"
        Segunda regla: asigna la categoría "spam" si el asunto contiene la palabra "virus"
        Regla por defecto: usa el clasificador por defecto
        """
        classifier = self._build_classifier(nl_description)

        email = Email(client_id=1, subject="virus", body="Hello", sender="julian@gmail.com", fecha_envio=datetime.now())
        self.assertEqual("blacklist", classifier.classify(email))

    def _build_classifier(self, nl_description: str) -> WrappedClassifier:
        return WrappedClassifier(nl_description, self._nl_config_parser, self._classifier_deserializer)
