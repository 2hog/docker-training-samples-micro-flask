# Sample Flask Microservice

This is an example microservice written in Flask, intended to be used as part of 2hog's Docker trainings.

## Spec
It implements a single endpoint (`GET /`), which:

1. Requires basic authentication (configurable via the `AUTH_USER` and `AUTH_PASSWORD` environment variables)
2. Returns an HTML page fragment, based on the given `greeting` URL parameter
