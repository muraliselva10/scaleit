import unittest
from unittest.mock import patch, MagicMock
import requests
import sys
import os

# Add src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.api_client import APIClient

class TestAPIClient(unittest.TestCase):

    @patch('src.api_client.requests.get')
    def test_get_status_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"cpu": {"highPriority": 0.5}, "replicas": 5}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        
        client = APIClient("http://localhost:8123/app", {"Accept": "application/json", "Content-Type": "application/json"})
        status = client.get_status()
        self.assertIsNotNone(status)
        self.assertEqual(status['cpu']['highPriority'], 0.5)
        self.assertEqual(status['replicas'], 5)
    
    @patch('src.api_client.requests.get')
    def test_get_status_failure(self, mock_get):
        mock_get.side_effect = requests.RequestException("Error")
        
        client = APIClient("http://localhost:8123/app", {"Accept": "application/json", "Content-Type": "application/json"})
        status = client.get_status()
        self.assertIsNone(status)

    @patch('src.api_client.requests.put')
    def test_update_replicas_success(self, mock_put):
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_response.headers = {"Content-Type": "application/json"}
        mock_response.json.return_value = {"replicas": 5}
        mock_put.return_value = mock_response
        
        client = APIClient("http://localhost:8123/app", {"Accept": "application/json", "Content-Type": "application/json"})
        result = client.update_replicas(5)
        self.assertIsNotNone(result)
        self.assertEqual(result['replicas'], 5)

    @patch('src.api_client.requests.put')
    def test_update_replicas_no_content(self, mock_put):
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_response.headers = {"Content-Type": None}
        mock_put.return_value = mock_response
        
        client = APIClient("http://localhost:8123/app", {"Accept": "application/json", "Content-Type": "application/json"})
        result = client.update_replicas(5)
        self.assertIsNotNone(result)
        self.assertEqual(result, {})

    @patch('src.api_client.requests.put')
    def test_update_replicas_failure(self, mock_put):
        mock_put.side_effect = requests.RequestException("Error")
        
        client = APIClient("http://localhost:8123/app", {"Accept": "application/json", "Content-Type": "application/json"})
        result = client.update_replicas(5)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()

