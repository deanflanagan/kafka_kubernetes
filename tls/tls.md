# TLS using your own certificates

First run this to make sure you have yq installed:

```
sudo wget -qO /usr/local/bin/yq https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64
sudo chmod a+x /usr/local/bin/yq
yq --version
```

Then run this short set of commands to split the strimzi operator into a kustomize ready base dir.

Great guide on kustomize here: https://www.densify.com/kubernetes-tools/kustomize/ and https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/

### TLS Setup

The Tls setup script:

- Downloads Strimzi resources, crds etc
- Uses kustomize to break those out into base/overlays, adding the resources specified to environments:
    1. Develop
    2. Pre-prod
    3. Prod
- Resources you want to keep are listed in the overlaysKinds.txt in this dir
