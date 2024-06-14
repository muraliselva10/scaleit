import time
import logging

# Logger configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AutoScaler:
    def __init__(self, api_client, target_cpu_utilization, check_interval):
        self.api_client = api_client
        self.target_cpu_utilization = target_cpu_utilization
        self.check_interval = check_interval

    def auto_scale(self):
        """Main loop for the auto-scaler."""
        while True:
            status = self.api_client.get_status()
            if status:
                current_cpu = status['cpu']['highPriority']
                current_replicas = status['replicas']
                logger.info(f"Current CPU: {current_cpu}, Replicas: {current_replicas}")

                if current_cpu > self.target_cpu_utilization:
                    new_replicas = current_replicas + 1
                    logger.info(f"Increasing replicas to {new_replicas}")
                    self.api_client.update_replicas(new_replicas)
                elif current_cpu < self.target_cpu_utilization:
                    new_replicas = max(1, current_replicas - 1)
                    if new_replicas != current_replicas:
                        logger.info(f"Decreasing replicas to {new_replicas}")
                        self.api_client.update_replicas(new_replicas)

            time.sleep(self.check_interval)
