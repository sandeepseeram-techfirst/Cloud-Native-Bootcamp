# Nginx Ingress

controlplane:~$ kubectl get deployments -n world
NAME     READY   UP-TO-DATE   AVAILABLE   AGE
asia     2/2     2            2           114s
europe   2/2     2            2           114s
controlplane:~$ 


### Excercise-1 

Create ClusterIP Services for both Deployments for port 80 . 
The Services should have the same name as the Deployments.

