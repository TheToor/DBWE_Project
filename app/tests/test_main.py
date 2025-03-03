import json

class TestMain():
    def test_index(self, client):
        response = client.get('/api/v1/main')
        assert response.status_code == 200
        assert response.json == {'message': 'Hello, World!'}
            