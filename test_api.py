import unittest
from flask import jsonify, Flask
from api import app

#  Graceful json responce on bad requests
class TestingApi(unittest.TestCase):
    def test_multiply_input(self):
        with app.test_client() as c:
            rv = c.post('/multiply', json={
                "number": "5", "times": 2
            })
            json_data = rv.get_json()
            assert ("pass numbers, please" == json_data['error'])
        with app.test_client() as c:
            rv = c.post('/multiply', json={
                "number": 5, "times": "2"
            })
            json_data = rv.get_json()
            assert ("pass numbers, please" == json_data['error'])
        with app.test_client() as c:
            rv = c.post('/multiply', json={
                "number": "5.5", "times": 2
            })
            json_data = rv.get_json()
            assert ("pass numbers, please" == json_data['error'])
        with app.test_client() as c:
            rv = c.post('/multiply', json={
                "number": 5, "times": "2.0"
            })
            json_data = rv.get_json()
            assert ("pass numbers, please" == json_data['error'])
        with app.test_client() as c:
            rv = c.post('/multiply', json={
                "number": "asd5", "times": 2
            })
            json_data = rv.get_json()
            assert ("pass numbers, please" == json_data['error'])
        with app.test_client() as c:
            rv = c.post('/multiply', json={
                "number": 5, "times": "asd2"
            })
            json_data = rv.get_json()
            assert ("pass numbers, please" == json_data['error'])
        with app.test_client() as c:
            rv = c.post('/multiply', json={
                "number": True, "times": 2
            })
            json_data = rv.get_json()
            assert ("pass numbers, please" == json_data['error'])
        with app.test_client() as c:
            rv = c.post('/multiply', json={
                "number": 5, "times": True
            })
            json_data = rv.get_json()
            assert ("pass numbers, please" == json_data['error'])
        with app.test_client() as c:
            rv = c.post('/multiply', json={
                "number": 99, "times": 155
            })
            json_data = rv.get_json()
            assert ("values are too high for calculation" == json_data['error'])

    def test_group_input(self):
        with app.test_client() as c:
            rv = c.post('/group', json={
                "words": 5
            })
            json_data = rv.get_json()
            assert ("pass words, please" == json_data['error'])
        with app.test_client() as c:
            rv = c.post('/group', json={
                "words": 5.9552
            })
            json_data = rv.get_json()
            assert ("pass words, please" == json_data['error'])
        with app.test_client() as c:
            rv = c.post('/group', json={
                "words": True
            })
            json_data = rv.get_json()
            assert ("pass words, please" == json_data['error'])
        with app.test_client() as c:
            rv = c.post('/group', json={
                "words": ["word", 2, "master", "keys"]
            })
            json_data = rv.get_json()
            assert ("pass words as string, please" == json_data['error'])
    def test_serialize_input(self):
        with app.test_client() as c:
            rv = c.post('/serialize', json={
                "words": 5
            })
            json_data = rv.get_json()
            assert ("pass text, please" == json_data['error'])
        with app.test_client() as c:
            rv = c.post('/serialize', json={
                "text": 5
            })
            json_data = rv.get_json()
            assert ("pass text as string, please" == json_data['error'])
        with app.test_client() as c:
            rv = c.post('/serialize', json={
                "text": 5.28
            })
            json_data = rv.get_json()
            assert ("pass text as string, please" == json_data['error'])
        with app.test_client() as c:
            rv = c.post('/serialize', json={
                "text": True
            })
            json_data = rv.get_json()
            assert ("pass text as string, please" == json_data['error'])


if __name__ == '__main__':
    unittest.main()