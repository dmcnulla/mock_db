"""Test dbaccess."""

import mock
import pytest
from dbaccess import DbAccess
from database import DataBase

@pytest.fixture(scope='function')
def db_conn_fixture(request):
    """Create db connection."""
    print("\n[setup] Using db_conn_fixture")
    my_conn = DbAccess('my_db')
    my_conn.add_user('dave')
    my_conn.add_user('scott')
    my_conn.add_user('pat')
    def fin():
        my_conn = None
        print("\n[teardown] db_conn is closed.")
    request.addfinalizer(fin)
    return my_conn

@pytest.fixture(scope='function')
def fake_db_conn_fixture():
    """Create db connection."""
    print("\n[setup] Using fake_db_conn_fixture")
    my_conn = DbAccess('my_db')
    my_conn.add_user('dave')
    my_conn.add_user('scott')
    my_conn.add_user('pat')
    return my_conn

@pytest.mark.userfixtures("db_conn_fixture")
def test_drop_user(db_conn_fixture):
    """Test without mocks."""
    db_conn_fixture.list_users()
    db_conn_fixture.drop_user('dave')
    list = db_conn_fixture.list_users()
    assert(list.__contains__('dave')==False)

@pytest.mark.userfixtures("fake_db_conn_fixture")
def test_drop_user2(fake_db_conn_fixture):
    """Stub this."""
    print("userfixtures and parameter")
    assert(fake_db_conn_fixture.list_users().__contains__('dave'))

def test_drop_user3(fake_db_conn_fixture):
    """Stub this."""
    print("parameter only")
    assert(fake_db_conn_fixture.list_users().__contains__('dave'))

@pytest.mark.userfixtures("fake_db_conn_fixture")
def test_drop_user4():
    """Stub this."""
    print("userfixtures only")
    with pytest.raises(AttributeError) as excinfo:
        fake_db_conn_fixture.list_users()
    excinfo.match("'function' object has no attribute 'list_users'")
