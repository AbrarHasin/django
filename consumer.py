import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Product

params = pika.URLParameters('amqps://zllzhyav:jHi18yD9N5Rr8VsvY-bVxKiz5nKsBvNX@armadillo.rmq.cloudamqp.com/zllzhyav')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Received in admin')
    message = json.loads(body)
    method = message['method']
    data = message['body']
    print(f"Method: {method}")
    print(f"Data: {data}")
    ##################################
    product = Product.objects.get(id=data) #or data['id']
    product.likes = product.likes + 1
    product.save()
    print('Product likes increased!')


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()

channel.close()