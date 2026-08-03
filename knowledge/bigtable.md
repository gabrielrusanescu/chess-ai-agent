# Bigtable

Bigtable is a managed wide-column database designed for very large datasets and low-latency access.

## Important concepts

- Data is organized by row key.
- Row-key design strongly affects performance and access patterns.
- Column families group related columns.
- Applications should be designed around the queries they need to execute.
- Bigtable is suitable for high-throughput and time-series-style workloads.

## Typical use cases

- IoT telemetry
- Time-series data
- Personalization and recommendation features
- Financial or operational event data
- Large analytical and serving workloads requiring predictable access

## Comparison with Cloud SQL

Cloud SQL provides relational modelling, transactions, joins, and SQL. Bigtable provides large-scale key-based access and requires deliberate row-key and schema design.
