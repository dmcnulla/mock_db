# mock_db
Practice mocking a dependent database connection while testing wrapper for that database connection.

# To install
git clone https://github.com/dmcnulla/mock_db
vitualenv db_mock
source db_mock/bin/activate 
pip install pytest_mock (I don't remember if this is needed)

## To run
pytest -s -v
