#### Configure Docker and Buildkit to support building multi-architecture images.

To build images for multiple architectures, it is important that we make use of BuildKit. BuildKit is not always enabled by default, so you need to make sure that it is enabled in our environment. 


❯ cat /etc/docker/daemon.json | jq
{
  "bip": "172.18.0.1/24",
  "debug": true,
  "storage-driver": "overlay2",
  "registry-mirrors": [
    "http://docker-registry-mirror.sandeepseeram.com"
  ],
  "insecure-registries": [
    "registry.test.training.sandeepseeram.com:4567",
    "docker-registry-mirror.sandeepseeram.com"
  ],
  "features": {
    "buildkit": true
  }
}