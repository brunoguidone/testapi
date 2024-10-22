import unittest
import json
from api import app


class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/v1/')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Bem vindo')

    def test_page_not_found(self):
        response = self.app.get('/invalid_route')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['message'], 'Rota nao encontrada')


if __name__ == '__main__':
    unittest.main()
