from api_client import APIClient
from auto_scaler import AutoScaler

if __name__ == "__main__":
    API_URL = "http://localhost:8123/app"
    HEADERS = {"Accept": "application/json", "Content-Type": "application/json"}
    TARGET_CPU_UTILIZATION = 0.80
    CHECK_INTERVAL = 10  # seconds

    api_client = APIClient(API_URL, HEADERS)
    auto_scaler = AutoScaler(api_client, TARGET_CPU_UTILIZATION, CHECK_INTERVAL)
    auto_scaler.auto_scale()
