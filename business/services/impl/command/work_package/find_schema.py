from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.work_package.work_package_command import WorkPackageCommand
from model.schema import Schema


class FindSchema(WorkPackageCommand):

    def __init__(self, connection, work_package):
        super().__init__(connection)
        self.work_package = work_package

    def execute(self):
        try:
            json_obj = GetRequest(connection=self.connection,
                                  context=f"{self.CONTEXT}schemas/{self.work_package.id}").execute()
            return Schema(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding the work package schema") from re