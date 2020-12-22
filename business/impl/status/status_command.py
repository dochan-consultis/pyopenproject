from abc import abstractmethod, ABCMeta
from business.impl.command import Command


class StatusCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/statuses"

    @abstractmethod
    def execute(self): raise NotImplementedError
