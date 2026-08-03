# Google Kubernetes Engine

Google Kubernetes Engine provides managed Kubernetes on Google Cloud.

## What GKE manages

GKE reduces the operational burden of creating and maintaining Kubernetes clusters. The exact division of responsibility depends on the selected operating mode and configuration.

## Standard and Autopilot

- Standard mode gives the user more direct control over cluster and node configuration.
- Autopilot mode manages more of the infrastructure and applies stronger defaults.

## Typical workflow

1. Create or select a cluster.
2. Configure `kubectl` credentials.
3. Deploy a containerized workload.
4. Expose the workload through a Service.
5. Inspect pods, deployments, services, events, and logs.
6. Scale or update the deployment.

## Relationship to Docker

Docker or another compatible build tool creates container images. Kubernetes and GKE deploy and operate those images across a cluster.
