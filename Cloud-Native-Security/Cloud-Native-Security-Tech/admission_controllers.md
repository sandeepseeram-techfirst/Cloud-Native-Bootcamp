# Admission Controllers

A Kubernetes admission controller is code that evaluates requests to the Kubernetes API server, then determines whether or not to allow the request.

The evaluation happens after the API server has already authenticated and authorized the request, but before the request is granted and implemented.