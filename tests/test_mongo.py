from pymongo import MongoClient
client = MongoClient(
    'localhost',
    27017,
    username='weaverusr',
    password='weaverpass'
)

db = client['weaverdb']

def test_insert():
    _initial_count = db.pytest.count_documents({})
    _create_doc = db.pytest.insert_one({"hello": "world2"})
    _new_count = db.pytest.count_documents({})
    assert _new_count == _initial_count + 1

def test_delete():
    _initial_count = db.pytest.count_documents({})
    _create_doc = db.pytest.delete_one({"hello": "world2"})
    _new_count = db.pytest.count_documents({})
    assert _new_count == _initial_count - 1

test_insert()
