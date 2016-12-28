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

@pytest.mark.userfixtures("db_conn_fixture")
def test_drop_user_0(db_conn_fixture):
    """Test without mocks."""
    print("test" + str(0))
    db_conn_fixture.list_users()
    db_conn_fixture.drop_user('dave')
    list = db_conn_fixture.list_users()
    assert(list.__contains__('dave')==False)

# def test_drop_user_1(monkeypatch):
#     """Directly patch the monkey."""
#     print("test" + str(1))
#     monkeypatch.setattr("database.DataBase.delete", True)
#     # assert square(5) == 1
#     db_conn = DbAccess('fake_db')
#     assert(db_conn.drop_user('fake')==False)

## Fixture mocks
@pytest.fixture(scope='function')
def fake_db_delete():
    """Create db connection."""
    print("\n[setup] Using fake_db_delete")
    def mock_delete(mocked_db_delete):
        assert(mocked_db_delete is DataBase.delete)
        DataBase.delete('anything')
        mocked_db_delete.called_once_with(str('anything'))
        return mock_db_delete
    return mock_delete

# @pytest.mark.userfixtures("fake_db_delete")
# def test_drop_user_2(fake_db_delete):
#     """Stub this."""
#     print("test" + str(2))
#     db_conn = DbAccess('fake_db')
#     db_conn.drop_user('fake')
#     fake_db_delete.assert_called_once_with('fake')

# def test_drop_user_3(fake_db_delete):
#     """Stub this."""
#     print("test" + str(3))
#     db_conn = DbAccess('fake_db')
#     db_conn.drop_user('fake')
#     fake_db_delete.assert_called_once_with('fake')

@pytest.mark.userfixtures("fake_db_delete")
def test_drop_user_4():
    """Stub this."""
    print("test" + str(4))
    print("userfixtures only")
    with pytest.raises(AttributeError) as excinfo:
        fake_db_delete.list_users()
    excinfo.match("'function' object has no attribute 'list_users'")

# def test_drop_user_5(monkeypatch):
#     """Patch the monkey."""
#     # def del_return(return_bool):
#     #     return return_bool
#     print("test" + str(5))
#     monkeypatch.setattr(DataBase, "delete", 'Fake')
#     db_conn = DbAccess('fake_db')
#     db_conn.drop_user('fake')
#     monkeypatch.assert_called_once_with(str('fake'))

## mock patch
@mock.patch('database.DataBase.delete', return_value=True)
def test_drop_user_6(mocked_database_delete):
    """Test Good drop_user."""
    print("test" + str(6))
    db_conn = DbAccess('fake_db')
    assert(db_conn.drop_user('fake'))

@mock.patch('database.DataBase.delete', return_value=False)
def test_drop_user_7(mocked_database_delete):
    """Test Bad drop_user."""
    print("test" + str(7))
    db_conn = DbAccess('fake_db')
    assert(db_conn.drop_user('fake')==False)

def test_drop_user_8(monkeypatch):
    """Verify dropping a user."""
    def mock_delete_user_fail(*args, **kwargs):
        """ Act like someone just typed 'yolo'. """
        return False

    def mock_delete_user_pass(*args, **kwargs):
        """ Act like someone just typed 'yolo'. """
        return True
    monkeypatch.setattr('database.DataBase.delete', mock_delete_user_pass)
    # retval should now contain 'yolo'
    assert(DbAccess('fake_db').drop_user('fake'))

## Fixture mocks
@pytest.fixture(scope='function')
def db_delete_fail(monkeypatch):
    """Create db connection."""
    def mock_delete_user_fail(*args, **kwargs):
        """ Act like someone just typed 'yolo'. """
        return False
    monkeypatch.setattr('database.DataBase.delete', mock_delete_user_fail)

@pytest.fixture(scope='function')
def db_delete_pass(monkeypatch):
    """Create db connection."""
    def mock_delete_user_pass(*args, **kwargs):
        """ Act like someone just typed 'yolo'. """
        return True
    monkeypatch.setattr('database.DataBase.delete', mock_delete_user_pass)

@pytest.mark.userfixtures("db_delete_fail")
def test_drop_user_9(db_delete_fail):
    """Stub this."""
    print("test" + str(9))
    db_conn = DbAccess('fake_db')
    assert(db_conn.drop_user('fake')==False)

@pytest.mark.userfixtures("db_delete_pass")
def test_drop_user_10(db_delete_pass):
    """Stub this."""
    print("test" + str(10))
    db_conn = DbAccess('fake_db')
    assert(db_conn.drop_user('fake'))
