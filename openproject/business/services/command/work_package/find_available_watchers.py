from openproject.api_connection.exceptions.request_exception import RequestError
from openproject.api_connection.requests.get_request import GetRequest
from openproject.business.exception.business_error import BusinessError
from openproject.business.services.command.find_list_command import FindListCommand
from openproject.business.services.command.work_package.work_package_command import WorkPackageCommand
from openproject.model.user import User


class FindAvailableWatchers(WorkPackageCommand):
    def __init__(self, connection, work_package):
        super().__init__(connection)
        self.work_package = work_package

    def execute(self):
        try:
            request = GetRequest(self.connection,
                                  f"{self.CONTEXT}/{self.work_package.id}/available_watchers")
            return FindListCommand(self.connection, request, User).execute()
            # for watcher in json_obj["_embedded"]["elements"]:
            #     yield usr.User(watcher)
        except RequestError as re:
            raise BusinessError(f"Error finding available watchers for work package {self.work_package.id}") from re