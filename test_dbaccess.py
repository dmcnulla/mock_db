"""Test dbaccess."""

import mock
from mock import MagicMock
import pytest
from dbaccess import DbAccess
from database import DataBase

@pytest.fixture(scope='function')
def fake_db():
    """Create db connection."""
    mock = MagicMock(DataBase)
    mock.delete.return_value = True
    return DbAccess(mock)

def test_mock_db(fake_db):
    db_connection = fake_db
    assert(db_connection.drop_user('fake'))

def test_real_db():
    db = DataBase('test')
    db_connection = DbAccess(db)
    assert(db_connection.drop_user('fake')==False)


if __name__ == '__main__':
    pytest.main()
