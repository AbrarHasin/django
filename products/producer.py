import pika, json

params = pika.URLParameters('amqps://zllzhyav:jHi18yD9N5Rr8VsvY-bVxKiz5nKsBvNX@armadillo.rmq.cloudamqp.com/zllzhyav')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish():
    # properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body="Hello")