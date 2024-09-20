from turtle import back
from fastapi import BackgroundTasks
import logging

logger = logging.getLogger(__name__)
background_tasks = BackgroundTasks()

def record_event(key: str, message=""):
    with open("event-record.txt", mode="w") as events_file:
        content = f"Writing event {key}: {message}"
        events_file.write(content)


def write_event(key: str, message=""):
    background_tasks.add_task(record_event, key, message="some notification")

# start scheduler
def run():
    logger.info("Sync: Scheduled task running...")    