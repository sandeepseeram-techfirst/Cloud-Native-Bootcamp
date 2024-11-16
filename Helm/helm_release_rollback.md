##### Helm Release Check 

controlplane:~$ helm list -n dev-ns
NAME            NAMESPACE       REVISION        UPDATED                                 STATUS          CHART           APP VERSION
mock-app        dev-ns          2               2025-04-14 07:32:41.756014477 +0000 UTC deployed        mock-app-2.0.0  1.16.0     
controlplane:~$ 


controlplane:~$ kubectl get all -n dev-ns
NAME                                       READY   STATUS    RESTARTS   AGE
pod/mock-app-deployment-6ddfb48b5c-q7mm7   1/1     Running   0          3m53s

NAME                       TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
service/mock-app-service   ClusterIP   10.105.129.206   <none>        5000/TCP   3m54s

NAME                                  READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/mock-app-deployment   1/1     1            1           3m54s

NAME                                             DESIRED   CURRENT   READY   AGE
replicaset.apps/mock-app-deployment-6ddfb48b5c   1         1         1       3m53s
replicaset.apps/mock-app-deployment-7b89fbdb7c   0         0         0       3m54s

NAME                                               REFERENCE                        TARGETS              MINPODS   MAXPODS   REPLICAS   AGE
horizontalpodautoscaler.autoscaling/mock-app-hpa   Deployment/mock-app-deployment   cpu: <unknown>/50%   1         3         1          3m54s
controlplane:~$ 