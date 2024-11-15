##### Helm Installation 

controlplane:~$ curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3

controlplane:~$ chmod 700 get_helm.sh

controlplane:~$ ./get_helm.sh
Downloading https://get.helm.sh/helm-v3.17.3-linux-amd64.tar.gz
Verifying checksum... Done.
Preparing to install helm into /usr/local/bin
helm installed into /usr/local/bin/helm

##### Helm Version 

controlplane:~$ helm version 
version.BuildInfo{Version:"v3.17.3", GitCommit:"e4da49785aa6e6ee2b86efd5dd9e43400318262b", GitTreeState:"clean", GoVersion:"go1.23.7"}
controlplane:~$ 

##### Helm Repo Add and Helm Install 

controlplane:~$ helm repo add mock-app-repo https://benmalekarim.github.io/helm-scenarios-charts/
"mock-app-repo" has been added to your repositories
controlplane:~$ helm install mock-app mock-app-repo/mock-app --version 2.1.0
NAME: mock-app
LAST DEPLOYED: Mon Apr 14 07:21:09 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
controlplane:~$ 