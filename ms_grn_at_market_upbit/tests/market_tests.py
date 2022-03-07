import json
import os
import unittest
from project.app import MyMicroservice
from pyms.constants import CONFIGMAP_FILE_ENVIRONMENT
from typing import Dict, List, Union, Text


class MarketTestcase(unittest.TestCase):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    def setUp(self):
        pass

    def tearDown(self):
        pass  # os.unlink(self.app.config['DATABASE'])
    
    # def test_home(self):
    #     response = self.client.get('/')
    #     self.assertEqual(404, response.status_code)
    # def test_healthcheck(self):
    #     response = self.client.get('/healthcheck')
    #     self.assertEqual(200, response.status_code)

    # def test_list_view(self):
    #     response = self.client.get('/ms_grn_at_market_upbit/')
    #     self.assertEqual(200, response.status_code)

    # def test_create_view(self):
    #     name = "blue"
    #     response = self.client.post('/ms_grn_at_market_upbit/',
    #                                 data=json.dumps(dict(name=name)),
    #                                 content_type='application/json'
    #                                 )
    #     self.assertEqual(200, response.status_code)
