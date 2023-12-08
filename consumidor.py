from confluent_kafka import Consumer, KafkaError

def recibir_mensaje():
    # Configuración del consumidor
    consumer_config = {
        'bootstrap.servers': 'localhost:9092',  # Reemplaza con la dirección de tus servidores Kafka
        'group.id': 'python-consumer',
        'auto.offset.reset': 'earliest'
    }

    # Crear un consumidor
    consumer = Consumer(consumer_config)

    # Suscribirse a un tópico
    topic = 'test-topic99'
    consumer.subscribe([topic])

    # Esperar mensajes y procesarlos
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(msg.error())
                break

        print('Mensaje recibido: {}'.format(msg.value().decode('utf-8')))

if __name__ == "__main__":
    recibir_mensaje()
