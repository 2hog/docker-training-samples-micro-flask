# Sample Flask Microservice

This is an example microservice written in Flask, intended to be used as part of 2hog's Docker trainings.

## Spec
It implements a single endpoint (`GET /`), which:

1. Requires basic authentication (configurable via the `AUTH_USER` and `AUTH_PASSWORD` environment variables)
2. Returns an HTML page fragment, based on the given `greeting` URL parameter

## Deployment

Before deploying this app with Docker Swarm or Kubernetes, make sure to build its image by running the following command

```sh
docker build -t 2hog/docker-training-samples-micro-flask
```

### Docker Swarm

```sh
docker stack deploy -c docker-compose.yml docker-training-samples-micro-flask
```

### Kubernetes

```sh
kubectl create secret generic docker-training-samples-micro-flask-secret \
--from-literal=auth_user=speak \
--from-literal=auth_password=easy
kubectl apply -f kube/
```

## License

This software is [MIT licensed](LICENSE).