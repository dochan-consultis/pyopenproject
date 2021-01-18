from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.root.root_command import RootCommand
from model.root import Root


class Find(RootCommand):

    def __init__(self, connection, root):
super().__init__(connection)        self.root = root

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}").execute()
            return Root(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding root: {self.root}") from re
