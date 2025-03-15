import logging
import os

# Ensure the `data/` directory exists
log_dir = "data"
os.makedirs(log_dir, exist_ok=True)

# Logger setup
logging.basicConfig(
    filename=os.path.join(log_dir, "app.log"),
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger()