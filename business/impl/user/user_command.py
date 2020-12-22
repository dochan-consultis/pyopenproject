from abc import abstractmethod, ABCMeta
from business.impl.command import Command


class UserCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/users/"

    @abstractmethod
    def execute(self): raise NotImplementedError
