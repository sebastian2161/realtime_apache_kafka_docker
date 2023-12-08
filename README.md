# realtime_apache_kafka_docker
 Development real-time streaming services with docker, using Windows 10 operating system

Step 1: Download the kafka docker image

    --Download image
    docker pull wurstmeister/kafka

Step 2: Create a docker network

    --Docker network
    docker network create kafka-net

Step 3: Start a Zookeeper container (kafka dependency)

    --Docker Zookeeper container
    docker run -d `
     --name zookeeper `
     --network kafka-net `
     -p 2181:2181 `
     wurstmeister/zookeeper

Step 4: Start a Kafka container

    --Docker Kafka container
    docker run -d `
     --name kafka `
     --network kafka-net `
     -p 9092:9092 `
     -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092 `
     -e KAFKA_LISTENER_SECURITY_PROTOCOL_MAP=PLAINTEXT:PLAINTEXT `
     -e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092 `
     -e KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181 `
     -e KAFKA_INTER_BROKER_LISTENER_NAME=PLAINTEXT `
     wurstmeister/kafka

Step 5: In PowerShell run the following command to create a topic

     --Create topic
     docker exec -it kafka bash
     kafka-topics.sh --create --topic test-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

Step 6: List of created topics

     -- List
     kafka-topics.sh --list --bootstrap-server localhost:9092

Step 7: Send messages to the topic you created, open new cmd console

     -- Send messages
     python productor.py

Step 8: Receive messages from the topic, open new cmd console

     -- Receive consumidor
     python productor.py
