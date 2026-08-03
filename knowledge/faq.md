# Summer School FAQ

## What is the difference between a virtual machine and a container?

A virtual machine includes a complete guest operating system. A container normally shares the host operating-system kernel while isolating the application process and its dependencies.

## Which service should store images and Markdown files?

Cloud Storage is the most appropriate of the services covered because these are objects rather than relational records.

## When should I choose Cloud SQL?

Choose Cloud SQL when the application requires a relational schema, SQL queries, transactions, constraints, or joins.

## When should I choose Bigtable?

Choose Bigtable for very large, high-throughput datasets with access patterns that can be expressed through well-designed row keys.

## What is a Kubernetes pod?

A pod is Kubernetes' smallest deployable unit. It contains one or more tightly related containers that share networking and can share storage.

## What does a Kubernetes Service do?

A Service provides stable network access to a selected group of pods, even when individual pod instances are replaced.

## What is GKE?

GKE is Google Cloud's managed Kubernetes service.

## Why are we building an AI agent?

The final project combines a language model with tools and an external knowledge source. The agent can decide when to list, search, or read documents before composing an answer.
