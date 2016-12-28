"""Test dbaccess."""

import mock
import pytest
from dbaccess import DbAccess
from database import DataBase

@pytest.fixture()
def db_conn_fixture(request):
    """Create db connection."""
    print("\nusing db_conn_fixture")
    my_conn = DbAccess('my_db')
    my_conn.add_user('dave')
    my_conn.add_user('scott')
    my_conn.add_user('pat')
    def fin():
        my_conn = None
        # print("All done, db_conn is closed.")
    request.addfinalizer(fin)
    return my_conn

@pytest.fixture()
def fake_db_conn_fixture():
    """Create db connection."""
    print("\nusing fake_db_conn_fixture")
    my_conn = DbAccess('my_db')
    my_conn.add_user('dave')
    my_conn.add_user('scott')
    my_conn.add_user('pat')
    return my_conn

@pytest.mark.userfixtures("db_conn_fixture")
def test_drop_user2(db_conn_fixture):
    """Test without mocks."""
    db_conn_fixture.list_users()
    db_conn_fixture.drop_user('dave')
    list = db_conn_fixture.list_users()
    assert(list.__contains__('dave')==False)

@pytest.mark.userfixtures("fake_db_conn_fixture")
def test_drop_user(fake_db_conn_fixture):
    """Stub this."""
    assert(True)
