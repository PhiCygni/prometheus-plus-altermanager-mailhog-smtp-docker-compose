:: Stop all containers
docker-compose stop

:: Down and remove volumes
docker-compose down --volumes 

:: Remove the produced python image
docker image rm image rm phi-cygni-python-prometheus-client-image:1.0.0