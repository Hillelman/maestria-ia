#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# pip install pika python-dotenv


# In[10]:


import os
import sys
import argparse
import time
import pika
# from dotenv import load_dotenv


# In[11]:


# Cargando la variable de entorno
# load_dotenv()

def get_connection(url=None):
    url = url or os.getenv("amqps://qxgnazdc:FG9z2xFF88E-7eQCJjPFC3R2jq-EQ6o3@kebnekaise.lmq.cloudamqp.com/qxgnazdc")
    # url = url or os.getenv("CLOUDAMQP_URL")
    if not url:
        print("Error: proporciona CLOUDAMQP_URL como variable de entorno o --url")
        sys.exit(1)
    params = pika.URLParameters(url)
    return pika.BlockingConnection(params)


# In[12]:


# -------------------
# Work queue (task distribution)
# -------------------
def send_task(url, message):
    conn = get_connection(url)
    channel = conn.channel()
    channel.queue_declare(queue="task_queue", durable=True)
    channel.basic_publish(
        exchange="",
        routing_key="task_queue",
        body=message.encode(),
        properties=pika.BasicProperties(delivery_mode=2),  # make message persistent
    )
    print(" [x] Sent task:", message)
    conn.close()


def worker(url):
    conn = get_connection(url)
    channel = conn.channel()
    channel.queue_declare(queue="task_queue", durable=True)
    channel.basic_qos(prefetch_count=1)

    print(" [*] Waiting for tasks. To exit press CTRL+C")

    def callback(ch, method, properties, body):
        message = body.decode()
        print(" [x] Received:", message)
        # Simulate work: number of dots -> seconds
        work_seconds = message.count(".")
        try:
            time.sleep(work_seconds)
        except KeyboardInterrupt:
            pass
        ch.basic_ack(delivery_tag=method.delivery_tag)
        print(" [x] Done")

    channel.basic_consume(queue="task_queue", on_message_callback=callback)
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
    conn.close()


# -------------------
# Publish/Subscribe (fanout exchange)
# -------------------
EXCHANGE_NAME = "logs_fanout"


def publish_log(url, message):
    conn = get_connection(url)
    channel = conn.channel()
    channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type="fanout", durable=False)
    channel.basic_publish(exchange=EXCHANGE_NAME, routing_key="", body=message.encode())
    print(" [x] Sent log:", message)
    conn.close()


def subscribe_logs(url):
    conn = get_connection(url)
    channel = conn.channel()
    channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type="fanout", durable=False)
    # Create a random, exclusive queue for this subscriber
    result = channel.queue_declare(queue="", exclusive=True)
    queue_name = result.method.queue
    channel.queue_bind(exchange=EXCHANGE_NAME, queue=queue_name)

    print(" [*] Waiting for logs. To exit press CTRL+C")

    def callback(ch, method, properties, body):
        print(" [x] Log:", body.decode())

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
    conn.close()


# -------------------
# CLI
# -------------------
def main():
    parser = argparse.ArgumentParser(description="CloudAMQP demo: work queue and pub/sub")
    parser.add_argument("--url", help="CloudAMQP URL (overrides CLOUDAMQP_URL env var)")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_send = sub.add_parser("task", help="Send a task to the work queue")
    p_send.add_argument("--message", "-m", default="Hello...", help="Message body")

    p_worker = sub.add_parser("worker", help="Run a worker to consume tasks")

    p_pub = sub.add_parser("pub", help="Publish a log message to pub/sub (fanout)")
    p_pub.add_argument("--message", "-m", default="Info: log", help="Log message")

    p_sub = sub.add_parser("sub", help="Subscribe to logs (pub/sub)")

    args = parser.parse_args()

    if args.cmd == "task":
        send_task(args.url, args.message)
    elif args.cmd == "worker":
        worker(args.url)
    elif args.cmd == "pub":
        publish_log(args.url, args.message)
    elif args.cmd == "sub":
        subscribe_logs(args.url)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

