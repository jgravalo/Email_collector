from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Email:
    client_id: int
    subject: str
    body: str
    sender: str
    fecha_envio: datetime


class Classifier(ABC):

    @abstractmethod
    def classify(self, email: Email) -> Optional[str]:
        pass


class APIClassifier(Classifier):

    def classify(self, email: Email) -> Optional[str]:
        # TODO llamar al endpoint creado en la Parte 1
        pass


class ClassifierDeserializer(ABC):

    @abstractmethod
    def deserialize(self, config: dict) -> Classifier:
        pass


class NaturalLanguageConfigParser(ABC):

    @abstractmethod
    def parse(self, natural_language: str) -> dict:
        pass


class WrappedClassifier:

    _classifier: Classifier

    def __init__(self,
                 nl_description: str,
                 nl_config_parse: NaturalLanguageConfigParser,
                 classifier_deserializer: ClassifierDeserializer):
        config = nl_config_parse.parse(nl_description)
        self._classifier = classifier_deserializer.deserialize(config)

    def classify(self, email: Email) -> Optional[str]:
        return self._classifier.classify(email)
