import schedule
import time
import subprocess
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def job():
    try:
        logging.info("Starting data fetching and chart generation job.")
        subprocess.run(["python", "main.py"], check=True)
        upload_charts()
        logging.info("Job completed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred while running the main.py script: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

def upload_charts():
    try:
        logging.info("Starting upload of charts to GitHub Pages.")
        os.system('git add charts/*')
        os.system('git commit -m "Update charts"')
        os.system('git push origin main')
        logging.info("Charts uploaded successfully.")
    except Exception as e:
        logging.error(f"An error occurred while uploading charts: {e}")

# Schedule the job every day at 01:00
schedule.every().day.at("01:00").do(job)

logging.info("Scheduler started. Waiting for the next scheduled job...")

while True:
    schedule.run_pending()
    time.sleep(1)
