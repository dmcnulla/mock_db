"""This is common module."""


class DataBase (object):
    """This class help access to the database and run common queries."""

    def __init__(self, db_con):
        """Create the DB."""
        self.db_con = db_con
        self.users = []

    def delete(self, user_name):
        """Remove user."""
        # print("Delete %s" % user_name)
        self.check_name(user_name)
        return self.users.remove(user_name)

    def add(self, user_name):
        """Add user."""
        # print("Add %s" % user_name)
        self.check_name(user_name)
        self.users.append(user_name)

    def check_name(self, name):
        """Validate name."""
        if(name.strip() == 'fake'):
            raise ValueError('You cannot use "fake" as a user name.')

    def get_names(self):
        """Print list of user names."""
        return self.users
