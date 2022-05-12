import math
import multiprocessing
import re

from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.services.command.command import Command


class FindListCommand(Command):

    def __init__(self, connection, request, class_type):
        self.connection = connection
        self.request = request
        self.class_type = class_type

    def execute(self):
        return self.get_first(obj_list=[], json_obj=self.request.execute())

    def get_first(self, obj_list, json_obj):
        self.extract_results(obj_list, json_obj)

        if 'nextByOffset' in json_obj["_links"]:
            obj_list += self.start_queue(json_obj)

        return obj_list

    def get_link(self, url):
        try:
            json_obj = GetRequest(self.connection, url).execute()
            result = []
            self.extract_results(result, json_obj)
            return result

        except Exception as e:
            print(f"{e} {url}")
            self.get_link(url)

    def start_queue(self, json_obj):
        pages = math.ceil(json_obj["total"] / float(json_obj["pageSize"]))
        link = json_obj["_links"]["nextByOffset"]["href"].replace("offset=2", "offset={}")
        link = re.sub(r"&select=.*?&", "&", link)  # remove buggy parameter
        links = []

        for offset in range(2, pages + 1):
            page_link = link.format(offset)
            links.append(page_link)

        with multiprocessing.Pool(8) as p:
            results = p.map(self.get_link, links)

            flat_list = [item for sublist in results for item in sublist]

            return flat_list

    def extract_results(self, obj_list, json_obj):
        for obj in json_obj["_embedded"]["elements"]:
            obj_list.append(self.class_type(obj))