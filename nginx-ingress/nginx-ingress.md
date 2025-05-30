# Create Ingress for existing Services

controlplane:~$ kubectl get pods -n ingress-nginx
NAME                                        READY   STATUS      RESTARTS   AGE
ingress-nginx-admission-create-5twz7        0/1     Completed   0          11m
ingress-nginx-admission-patch-d94cd         0/1     Completed   0          11m
ingress-nginx-controller-59867d49f9-654qp   1/1     Running     0          11m
controlplane:~$ 