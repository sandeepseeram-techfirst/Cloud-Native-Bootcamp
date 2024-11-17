controlplane:~$ helm list -n dev-ns
NAME            NAMESPACE       REVISION        UPDATED                                 STATUS          CHART           APP VERSION
mock-app        dev-ns          1               2025-04-14 08:32:13.52740234 +0000 UTC  deployed        mock-app-1.0.0  1.16.0     


controlplane:~$ kubectl get all -n dev-ns
NAME                                       READY   STATUS    RESTARTS   AGE
pod/mock-app-deployment-699945d9bc-9g8bx   1/1     Running   0          55s

NAME                       TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/mock-app-service   ClusterIP   10.101.209.64   <none>        5000/TCP   55s

NAME                                  READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/mock-app-deployment   1/1     1            1           55s

NAME                                             DESIRED   CURRENT   READY   AGE
replicaset.apps/mock-app-deployment-699945d9bc   1         1         1       55s
controlplane:~$ 

##### Helm Values 

controlplane:~$ helm get values --all mock-app -n dev-ns
COMPUTED VALUES:
appName: mock-app
image:
  repository: benmalekarim/mock-app
  tag: v1.0.0
message: You will override this message
controlplane:~$ 

controlplane:~$ helm -n dev-ns upgrade --install mock-app /charts/mock-app-1.0.0.tgz --set message="You are overriding the message using an inline value. Good job !"
Release "mock-app" has been upgraded. Happy Helming!
NAME: mock-app
LAST DEPLOYED: Mon Apr 14 08:39:15 2025
NAMESPACE: dev-ns
STATUS: deployed
REVISION: 2
TEST SUITE: None
controlplane:~$ helm get values --all mock-app -n dev-ns
COMPUTED VALUES:
appName: mock-app
image:
  repository: benmalekarim/mock-app
  tag: v1.0.0
message: You are overriding the message using an inline value. Good job !
controlplane:~$ 