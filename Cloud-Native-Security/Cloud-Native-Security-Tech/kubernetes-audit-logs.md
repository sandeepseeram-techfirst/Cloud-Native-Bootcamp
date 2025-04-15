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