# Prometheus monitoring using docker compose

This repo contains a docker compose script making use of the Prometheus, Prometheus Alertmanager, Mailhog, Stunnel and Python images. Containers are connected together using a bridge network in order to provide a complete monitoring and alert system able to run locally. Solution was tested on Linux and Windows but should work on any platform able to run Docker.

[https://phicygni.com/](https://phicygni.com/)

[https://github.com/PhiCygni](https://github.com/PhiCygni)

[https://medium.com/@emileross](https://medium.com/@emileross)

[https://twitter.com/PhiCygni](https://twitter.com/PhiCygni)

[https://www.facebook.com/PhiCygni/](https://www.facebook.com/PhiCygni/)

# Usage

**To build and start all containers:**

>$ docker-compose up

# Web UI and open ports

| Open ports | Description                    | URL                    |
| ---------- | ------------------------------ | ---------------------- |
| 9090       | Prometheus Web UI              | http://localhost:9090  |
| 9093       | Prometheus Alertmanager Web UI | http://localhost:9093  |
| 8025       | Mailhog Web UI                 | http://localhost:8025  |
| 8000       | Python code Prometheus API     | http://localhost:8000  |