from src.extract.business.activity_service import ActivityService
from src.extract.business.impl.activity.find_by_context import FindByContext


class CustomActionServiceImpl(CustomActionService):

    def find_by_context(self, context):
        return FindByContext(context).execute()
