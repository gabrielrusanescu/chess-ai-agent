# Cloud Storage

Cloud Storage stores data as objects inside buckets.

## Structure

- A bucket is the top-level container.
- An object contains data and metadata.
- Object names can include slashes to create a folder-like organization, although the underlying model remains object storage.

## Typical use cases

- Images, video, and static website assets
- Backups and archives
- Data-lake ingestion
- Model artifacts and datasets
- Knowledge documents for an AI assistant

## Important design choices

- Bucket name
- Location
- Storage class
- Access control
- Retention and lifecycle policies

## In this project

The local Markdown knowledge files will later be uploaded to a Cloud Storage bucket. The agent tools will read the same documents through a cloud-backed knowledge provider.
