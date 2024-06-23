import requests
import logging

# Logger configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class APIClient:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def get_status(self):
        """Fetch the current status of the application."""
        try:
            response = requests.get(f"{self.base_url}/status", headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Error fetching status: {e}")
            return None

    def update_replicas(self, replicas):
        """Update the number of replicas of the application."""
        try:
            response = requests.put(f"{self.base_url}/replicas", headers=self.headers, json={"replicas": replicas})
            response.raise_for_status()
            if response.headers.get("Content-Type") == "application/json":
                return response.json()
            elif response.headers.get("Content-Type") is None:
                logger.info("Replicas updated successfully, no content returned.")
                return {}
            else:
                logger.warning(f"Unexpected content type: {response.headers.get('Content-Type')}")
                return None
        except requests.RequestException as e:
            logger.error(f"Error updating replicas: {e}")
            return None
