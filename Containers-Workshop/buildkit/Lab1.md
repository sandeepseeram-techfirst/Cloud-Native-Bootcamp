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


❯ docker buildx ls
NAME/NODE DRIVER/ENDPOINT STATUS  BUILDKIT PLATFORMS
default * docker                           
  default default         running 23.0.1   linux/amd64, linux/amd64/v2, linux/amd64/v3, linux/386, linux/arm64, linux/riscv64, linux/ppc64le, linux/s390x, linux/mips64le, linux/mips64, linux/arm/v7, linux/arm/v6
~ 
❯ docker buildx create --name builder --driver docker-container --use
builder
~ 
❯ docker buildx inspect --bootstrap
[+] Building 5.4s (1/1) FINISHED                                                                                         
 => [internal] booting buildkit                                                                                     5.4s
 => => pulling image moby/buildkit:buildx-stable-1                                                                  4.2s
 => => creating container buildx_buildkit_builder0                                                                  1.2s
Name:          builder
Driver:        docker-container
Last Activity: 2025-03-15 15:05:41 +0000 UTC

Nodes:
Name:      builder0
Endpoint:  unix:///var/run/docker.sock
Status:    running
Buildkit:  v0.20.1
Platforms: linux/amd64, linux/amd64/v2, linux/amd64/v3, linux/arm64, linux/riscv64, linux/ppc64, linux/ppc64le, linux/s390x, linux/386, linux/arm/v7, linux/arm/v6
~ took 5s 
❯ 

❯ docker buildx ls
NAME/NODE  DRIVER/ENDPOINT             STATUS  BUILDKIT PLATFORMS
builder *  docker-container                             
  builder0 unix:///var/run/docker.sock running v0.20.1  linux/amd64, linux/amd64/v2, linux/amd64/v3, linux/arm64, linux/riscv64, linux/ppc64, linux/ppc64le, linux/s390x, linux/386, linux/arm/v7, linux/arm/v6
default    docker                                       
  default  default                     running 23.0.1   linux/amd64, linux/amd64/v2, linux/amd64/v3, linux/386, linux/arm64, linux/riscv64, linux/ppc64le, linux/s390x, linux/mips64le, linux/mips64, linux/arm/v7, linux/arm/v6
~ 