# Kubernetes Audit Logs

Kubernetes provide a very important tool for helping to detect potential security events in the form of audit logs. 

Systematically recording details about access requests that are issued to the Kubernetes API. 

Kubernetes registers auditing data based on two key concepts: stages and audit events.

An audit event is any request to the API server, and stages align with the steps that the server goes through as it handles each request.

There are four possible “stages” for each event:

### RequestReceived: At this stage, the API server has received the request but has not started processing it yet.
### ResponseStarted: The server has started processing the request but has not yet sent a response.
### ResponseComplete: The server has finished processing the request and has sent a response.
### Panic: This stage happens when the API server “panics” in response to a request.

## Example: 

{
  "kind": "Event",
  "apiVersion": "audit.k8s.io/v1beta1",
  "metadata": {
    "creationTimestamp": "2018-10-08T08:26:55Z"
  },
  "level": "Request",
  "timestamp": "2018-10-08T08:26:55Z",
  "auditID": "288ace59-97ba-4121-b06e-f648f72c3122",
  "stage": "ResponseComplete",
  "requestURI": "/api/v1/pods?limit=500",
  "verb": "list",
  "user": {
    "username": "admin",
    "groups": ["system:authenticated"]
  },
  "sourceIPs": ["10.0.138.91"],
  "objectRef": {
    "resource": "pods",
    "apiVersion": "v1"
  },
  "responseStatus": {
    "metadata": {},
    "code": 200
  },
  "requestReceivedTimestamp": "2018-10-08T08:26:55.466934Z",
  "stageTimestamp": "2018-10-08T08:26:55.471137Z",
  "annotations": {
    "authorization.k8s.io/decision": "allow",
    "authorization.k8s.io/reason": "RBAC: allowed by
    
    ClusterRoleBinding "admin-cluster-binding" of ClusterRole "cluster-
    admin" to User "admin""
  
  }
}


## Audit Policy File 

apiVersion: audit.k8s.io/v1 # This is required.
kind: Policy
# Don't generate audit events for all requests in RequestReceived stage.
omitStages:
  - "RequestReceived"
rules:
  # Log pod changes at RequestResponse level
  - level: RequestResponse
    resources:
    - group: ""
      # Resource "pods" doesn't match requests to any subresource of pods,
      # which is consistent with the RBAC policy.
      resources: ["pods"]
  # Only check access to resource "pods"
  - level: Metadata
    resources:
    - group: ""
      resources: ["pods/log", "pods/status"]
  # Don't log watch requests by the "system:kube-proxy" on endpoints or services
  - level: None
    users: ["system:kube-proxy"]
    verbs: ["watch"]
    resources:
    - group: "" # core API group
      resources: ["endpoints", "services"]
  # Don't log authenticated requests to certain non-resource URL paths.
  - level: None
    userGroups: ["system:authenticated"]
    nonResourceURLs:
    - "/api*" # Wildcard matching.
    - "/version"
  # Log the request body of configmap changes in kube-system.
  - level: Request
    resources:
    - group: "" # core API group
      resources: ["configmaps"]
    # This rule only applies to resources in the "kube-system" namespace.
    # The empty string "" can be used to select non-namespaced resources.
    namespaces: ["kube-system"]
  # Log configmap and secret changes in all other namespaces at the Metadata level.
  - level: Metadata
    resources:
    - group: "" # core API group
      resources: ["secrets", "configmaps"]
  # A catch-all rule to log all other requests at the Metadata level.
  - level: Metadata
    # Long-running requests like watches that fall under this rule will not
    # generate an audit event in RequestReceived.
    omitStages:
      - "RequestReceived"

## Webhooks 
Send events over HTTP: You can use webhooks to send event data to an external security tool over HTTP. This way, your security tool can run entirely separately from your cluster.