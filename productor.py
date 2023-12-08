from confluent_kafka import Producer

def enviar_mensaje():
    # Configuración del productor
    producer_config = {
        'bootstrap.servers': 'localhost:9092',  # Reemplaza con la dirección de tus servidores Kafka
        'client.id': 'python-producer'
    }

    # Crear un productor
    producer = Producer(producer_config)

    # Nombre del tópico al que enviar mensajes
    topic = 'test-topic99'

    # Enviar un mensaje al tópico
    for i in range(0,100):
        var='Hello, Kafka!'+str(i)
        producer.produce(topic, key='key', value=var)

        # Esperar a que se entregue el mensaje o se produzca un error
        producer.flush()


if __name__ == "__main__":
    enviar_mensaje()