import json

from model.membership import Membership
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class MembershipServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.membershipSer = self.factory.get_membership_service()
        with open('../data/membership.json') as f:
            self.membership = Membership(json.load(f))

    def test_find_all(self):
        memberships = self.membershipSer.find_all(filters=None)
        # 2 memberships: One for each demo project
        self.assertEqual(2, len(memberships))

    def test_find(self):
        membership = self.membershipSer.find(self.membership)
        self.assertEqual(self.membership.__dict__, membership.__dict__)

    # TODO
    def test_update(self):
        self.assertIsNotNone(self.membershipSer.update(self.membership))

    # TODO
    def test_delete(self):
        self.assertIsNotNone(self.membershipSer.delete(self.membership))

    # TODO
    def test_create(self):
        self.assertIsNotNone(self.membershipSer.create(self.membership))

    # TODO
    def test_membership_schema(self):
        self.assertIsNotNone(self.membershipSer.membership_schema(self.membership))

    # TODO
    def test_available_memberships(self):
        self.assertIsNotNone(self.membershipSer.available_memberships())

    # TODO
    def test_create_form(self):
        self.assertIsNotNone(self.membershipSer.create_form(self.membership))

    # TODO
    def test_update_form(self):
        self.assertIsNotNone(self.membershipSer.update_form(self.membership))