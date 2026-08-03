# Compute Engine

Compute Engine is Google Cloud's infrastructure service for creating and operating virtual machines.

## Important concepts

- A virtual machine has a machine type, operating-system image, disks, network interfaces, and metadata.
- Resources are created in a project and usually placed in a region and zone.
- Persistent disks store data independently from the lifecycle of the virtual machine when configured appropriately.
- Firewall rules control permitted network traffic.
- Machine families and sizes should be selected according to CPU, memory, accelerator, and workload requirements.

## When to use it

Use Compute Engine when you need operating-system control, custom software installation, traditional server workloads, or a migration target for applications designed to run on virtual machines.

## Responsibility

Google operates the physical infrastructure and virtualization platform. The user remains responsible for the guest operating system, installed software, configuration, and much of the application-level security.
