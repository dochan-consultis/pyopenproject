from business.impl.command.activity.find_by_context import FindByContext
from business.impl.command.status.find_by_id import FindById
from business.status_service import StatusService


class StatusServiceImpl(StatusService):

    def find_all(self):
        return FindAll().execute

    def find_by_context(self, context):
        return FindByContext(context).execute()

    def find_by_id(self, identifier):
        return FindById(identifier).execute()