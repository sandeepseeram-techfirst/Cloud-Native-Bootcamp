controlplane $ kubectl get all
NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   95s

controlplane $ kubectl create -f pv.yaml
persistentvolume/pv-volume created

controlplane $ kubectl get pv
NAME        CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS      CLAIM   STORAGECLASS   REASON   AGE
pv-volume   2Gi        RWO            Retain           Available                                   26s
controlplane $ 

controlplane $ kubectl create -f pvc.yaml
persistentvolumeclaim/pv-claim created
controlplane $

controlplane $ kubectl create -f pv-pod.yaml
pod/pv-pod created