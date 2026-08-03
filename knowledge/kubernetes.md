# Kubernetes

Kubernetes orchestrates containerized applications across a cluster.

## Core resources

- Cluster: the complete Kubernetes environment
- Node: a machine that runs workloads
- Pod: the smallest deployable unit
- Deployment: manages replicated application pods and updates
- Service: provides stable network access to a set of pods
- ConfigMap: stores non-secret configuration
- Secret: stores sensitive configuration
- PersistentVolume and PersistentVolumeClaim: represent persistent storage

## Why orchestration is needed

A production platform must schedule containers, restart failed workloads, scale replicas, provide networking, manage configuration, and support controlled updates.

## Declarative configuration

Kubernetes commonly uses YAML manifests that describe the desired state. The control plane continually works to make the actual state match the desired state.

## Common commands

```bash
kubectl get nodes
kubectl get pods
kubectl get deployments
kubectl get services
kubectl apply -f deployment.yaml
kubectl describe pod POD_NAME
kubectl logs POD_NAME
```
