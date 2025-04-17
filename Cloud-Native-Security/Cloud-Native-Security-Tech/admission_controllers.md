# Admission Controllers

A Kubernetes admission controller is code that evaluates requests to the Kubernetes API server, then determines whether or not to allow the request.

The evaluation happens after the API server has already authenticated and authorized the request, but before the request is granted and implemented.


Admission controllers offer several important advantages as part of a Kubernetes security strategy:

Double-check requests: Admission controllers serve in a sense as a second line of defense against invalid requests that may have slipped past your RBAC controls (perhaps because of a misconfiguration in an RBAC policy, for example).

Rule flexibility: Admission controllers can evaluate requests and enforce rules based on parameters that you can’t configure (at least not easily) via RBAC. This is important because RBAC defines rules based only on identities and actions. Admission controllers offer more nuance, like the ability to limit resource requests or prevent the execution of commands on a privileged container.

Third-party integrations: Some admission controllers enable webhooks. You can use webhooks to trigger actions in third-party security systems. This means that admission controllers offer a way of integrating external security tools into Kubernetes without actually having to run those tools directly in the Kubernetes API. Arguably, this is the most powerful feature of admission controllers.