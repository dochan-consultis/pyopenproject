from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.project.project_command import ProjectCommand
from model.budget import Budget


class FindBudgets(ProjectCommand):

    def __init__(self, connection, project):
        super().__init__(connection)
        self.project = project

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.project.id}/budgets").execute()
            for budget in json_obj["_embedded"]["elements"]:
                yield Budget(budget)
        except RequestError as re:
            raise BusinessError(f"Error finding budget by id: {self.project.name}") from re
