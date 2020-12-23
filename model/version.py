from business.service_factory import ServiceFactory


class Version:

    def __init__(self, json_obj):
        self.__dict__ = json_obj

    def get_defining_project(self):
        if self._links.definingProject.href is not None:
            ServiceFactory.get_project_service().find_project_by_context(self._links.definingProject.href)
        return None

    def get_available_in_projects(self):
        if self._links.availableInProjects.href is not None:
            ServiceFactory.get_project_service().find_projects_by_context(self._links.availableInProjects.href)
        return None

    # TODO:
    #         "update": { "href": "/api/v3/versions/11/form", "method": "POST" }
    #         "updateImmediately": { "href": "/api/v3/versions/11", "method": "PATCH" }