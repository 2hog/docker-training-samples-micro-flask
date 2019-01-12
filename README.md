# Flask Sample Microservice

This is an example microservice written in Flask, intended to be used as part of 2hog's Docker trainings.

## Spec
It implements a single endpoint (`GET /`), which:

1. Requires basic authentication
2. Returns an HTML page fragment, based on the given `greeting` URL parameter

## Example

```
paris@docker-training-samples-micro-flask:/mnt/project$ curl -u antonis:kalipetis http://localhost:5000/?greeting=Konichiwa
<h1>Konichiwa, trainee!</h1>
<p>This is a simple Flask microservice that we wrote for you.</p>
```

## Configuration

The Flask Sample Microservice accepts configuration via environment variables:

- `AUTH_USER`: The username to use for Basic Authentication (default: `antonis`)
- `AUTH_PASSWORD`: The password to use for Basic Authentication (default: `kalipetis`)
- `DEBUG`: Enable debugging mode and print environment information (default: `false`)
- `ENVIRONMENT`: Environment in which the application runs (default: `production`)

## Secrets

The Flask Sample Microservice also accepts and prefers configuration for `AUTH_USER` and `AUTH_PASSWORD` as secret files:

- `/run/secrets/auth_user`: The username to use for Basic Authentication
- `/run/secrets/auth_password`: The password to use for Basic Authentication


## Deployment

## Docker

```sh
docker run -d \
-e AUTH_USER=antonis -e AUTH_PASSWORD=kalipetis \
-e DEBUG=true -e ENVIRONMENT=staging \
-p 5000 \
2hog/docker-training-samples-micro-flask
```

### Docker Swarm

```sh
docker secret create micro-flask-auth-user -
docker secret create micro-flask-auth-password -
docker stack deploy -c docker-compose.yml docker-training-samples-micro-flask
```

### Kubernetes

```sh
kubectl create secret generic docker-training-samples-micro-flask-secret \
--from-literal=auth_user=antonis \
--from-literal=auth_password=kalipetis
kubectl apply -f kube/
```

## Development

To develop the Flask Sample Microservice, follow these steps:

1. Install Docker ([docs](https://docs.docker.com/install/)) and Docker Compose ([docs](https://docs.docker.com/compose/install/))
2. Clone this repository:
    ```
    git clone https://github.com/2hog/docker-training-samples-micro-flask
    ```
3. Launch the app with Docker Compose:
    ```
    docker-compose up
    ```
4. Open your repository with your editor and rock n' roll!

## License

This software is [MIT licensed](LICENSE).
