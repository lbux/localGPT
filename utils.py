import os
import csv
from datetime import datetime, timedelta


def log_to_csv(question, answer, source, response_time, queue_time):
    log_dir, log_file = "local_chat_history", "qa_log.csv"
    # Ensure log directory exists, create if not
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Construct the full file path
    log_path = os.path.join(log_dir, log_file)

    # Check if file exists, if not create and write headers
    if not os.path.isfile(log_path):
        with open(log_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["timestamp", "question", "answer", "source", "response time", "queue time"])

    # Append the log entry
    with open(log_path, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        response_time = str(timedelta(seconds=response_time))
        response_time = response_time.split(".")[0]
        queue_time = str(timedelta(seconds=queue_time))
        queue_time = queue_time.split(".")[0]
        writer.writerow([timestamp, question, answer, source, response_time, queue_time])
