# Docker and Containers

A container packages an application with the libraries, runtime, and configuration required to run it consistently.

## Image and container

- An image is an immutable package used as a template.
- A container is a running instance of an image.
- Multiple containers can be started from the same image.

## Why containers are useful

- Consistent development and deployment environments
- Fast startup
- Lower overhead than a full virtual machine for many workloads
- Process and resource isolation
- Portability across compatible environments

## Common workflow

1. Write the application.
2. Create a Dockerfile.
3. Build the image.
4. Run and test a container.
5. Tag and push the image to a registry.
6. Deploy the image to a container platform.

## Common commands

```bash
docker build -t my-app .
docker run --rm -p 8080:8080 my-app
docker ps
docker images
```
