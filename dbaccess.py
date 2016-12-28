"""This is common module."""
from database import DataBase


class DbAccess(object):
    """This class help access to the database and run common queries."""

    def __init__(self, db_name):
        """Create the DB."""
        self.db_con = DataBase(db_name)

    def add_user(self, user):
        """Add User."""
        try:
            self.db_con.add(user)
        except ValueError:
            print("Oh crap, couldn't add %s" % user)

    def drop_user(self, user):
        """Drop user."""
        try:
            self.db_con.delete(user)
        except ValueError:
            print("Oh crap, couldn't delete %s" % user)

    def list_users(self):
        """List users."""
        users = self.db_con.get_names()
        # for user in users:
        #     print("> " + user)
        return users
