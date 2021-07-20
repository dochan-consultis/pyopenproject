import json
import os

from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.post_request import PostRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.work_package.work_package_command import WorkPackageCommand


class AddAttachment(WorkPackageCommand):

    def __init__(self, connection, work_package, attachment_path):
        super().__init__(connection)
        self.work_package = work_package
        self.attachment_path = attachment_path

    def execute(self):
        try:
            file_name = self.attachment_path.split(os.sep)[-1]
            PostRequest(connection=self.connection,
                        context=f"{self.CONTEXT}/{self.work_package.id}/attachments",
                        files={
                            "file": ("attachment", open(self.attachment_path, "rb"), 'application/octent-stream'),
                            "metadata": (None, json.dumps({"fileName": file_name}), 'application/json')
                        }).execute()
        except RequestError as re:
            raise BusinessError(f"Error adding new attachment: {self.attachment_path}") from re
