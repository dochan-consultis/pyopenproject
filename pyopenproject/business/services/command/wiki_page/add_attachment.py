import json
import os

from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.post_request import PostRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.wiki_page.wiki_command import WikiPageCommand


class AddAttachment(WikiPageCommand):

    def __init__(self, connection, wiki_page, attachment_path):
        """Constructor for class AddAttachment, from WikiPageCommand

        :param connection: The connection data
        :param wiki_page: The wiki page to add the attachment
        :param attachment_path: Local path to attachment
        """
        super().__init__(connection)
        self.wiki_page = wiki_page
        self.attachment_path = attachment_path

    def execute(self):
        try:
            file_name = self.attachment_path.split(os.sep)[-1]
            PostRequest(connection=self.connection,
                        context=f"{self.CONTEXT}/{self.wiki_page.id}/attachments",
                        files={
                            "file": ("attachment", open(self.attachment_path, "rb"), 'application/octent-stream'),
                            "metadata": (None, json.dumps({"fileName": file_name}), 'application/json')
                        }).execute()
        except RequestError as re:
            raise BusinessError(f"Error adding new attachment: {self.attachment_path}") from re
