from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.work_package.work_package_command import WorkPackageCommand


class FindRevisions(WorkPackageCommand):
    def __init__(self, connection, work_package):
        super().__init__(connection)
        self.work_package = work_package

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.work_package.id}/revisions").execute()
            for revision in json_obj["_embedded"]["elements"]:
                yield r.Revision(revision)
        except RequestError as re:
            raise BusinessError(f"Error finding revisions for work package {self.work_package.id}") from re