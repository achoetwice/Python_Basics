TLDR: Basically RabbitMQ is better as a message broker, redis is easier to use and having more features than merely a broker.

RABBITMQ\
Pros :
- Most developers agree (Although open for debate) that RabbitMQ is the best message broker on the planet today. It can be configured to use SSL thereby providing additional layer of security.
- Most people like the Interface for RabbitMQ. Much more versatile when compared to Redis as a message broker.
- Offers clustering and is very good at it.
- Scales to around 500,000+ messages a second.

Cons:
- Needs Erlang.
- Minimal configuration that can be done through code. (Configuring RabbitMQ is something that must be done first before even implementing your task queue.)
- Since our comparison is with Redis one can also say that for non extensive message brokers Redis obtains a slight edge due to its ability to multi-task.
#
REDIS\
Pros:
- Since it has dealings with a system's main memory Redis is fast and also scalable.
- Extremely easy to set up, use and deploy.
- Provides in-memory and advanced key-value cache.

Cons:
- Redis was created with a different intentions and not for being a message broker. It does support basic operations as a message broker however for powerful message routing Redis is not the preferred option.
- High latency in dealing with large messages. Redis is better suited for small messages.

original-link: https://www.linkedin.com/pulse/redis-vs-rabbitmq-message-broker-vishnu-kiran-k-v/