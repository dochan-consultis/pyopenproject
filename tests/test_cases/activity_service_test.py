import json

from business.exception.business_error import BusinessError
from model.activity import Activity
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class ActivityServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.actSer = self.factory.get_activity_service()
        with open('../data/activity.json') as f:
            self.activity = Activity(json.load(f))

    def test_activity_not_found(self):
        # There's no activity --> Exception
        with self.assertRaises(BusinessError):
            self.actSer.find(self.activity)

    def test_find_activity(self):
        # TODO: Test to find an Activity
        pass

    def test_update_activity(self):
        # TODO: We need a way to create activity in order to change it
        # There's no activity to update --> Exception
        with self.assertRaises(BusinessError):
            self.actSer.update(self.activity)
