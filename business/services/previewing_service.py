from abc import ABCMeta, abstractmethod

from business.services.abstract_service import AbstractService


class PreviewingService(AbstractService):
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        super().__init__(connection)

    @abstractmethod
    def from_markdown(self, text): raise NotImplementedError

    @abstractmethod
    def from_markdown_by_context(self, context): raise NotImplementedError

    @abstractmethod
    def from_plain(self, text): raise NotImplementedError