import csv
import time
import os
import argparse
import json

from kafka import KafkaProducer


def send_csv(csv_path):
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                             value_serializer=lambda x: json.dumps(x).encode('utf-8'))

    csv_file = open(os.path.join("data", csv_path))
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        producer.send("botlogs", value=row)
        time.sleep(2)

    csv_file.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("csv", help="csv file to send data from")
    args = parser.parse_args()
    send_csv(args.csv)
