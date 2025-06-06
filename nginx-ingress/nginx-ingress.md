# Create Ingress for existing Services 

The NGINX Ingress Controller is production‑grade Ingress controller (daemon) that runs alongside NGINX Open Source or NGINX Plus instances in a Kubernetes environment.

controlplane:~$ kubectl get pods -n ingress-nginx
NAME                                        READY   STATUS      RESTARTS   AGE
ingress-nginx-admission-create-5twz7        0/1     Completed   0          11m
ingress-nginx-admission-patch-d94cd         0/1     Completed   0          11m
ingress-nginx-controller-59867d49f9-654qp   1/1     Running     0          11m
controlplane:~$ 

The Nginx Ingress Controller has been installed.


controlplane:~$ vi ingress.yaml
controlplane:~$ kubectl apply -f ingress.yaml
ingress.networking.k8s.io/world created