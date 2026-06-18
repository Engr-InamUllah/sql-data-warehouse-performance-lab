# SQL Data Warehouse Performance Lab

A hands-on SQL laboratory for measuring query plans and improving warehouse workloads through indexing, partitioning, and rewrites.

## Architecture

`	ext
Baseline query -> Measure -> Tune -> Compare -> Document
`

## Technology stack

SQL Server, T-SQL, execution plans

## Repository blueprint

- project.yaml — scope, pipeline stages, and quality expectations
- src/ — ingestion and transformation implementation
- 	ests/ — unit, integration, and data-quality tests
- docs/ — architecture decisions and operational guidance

## Implementation roadmap

1. Create representative source data and document its contract.
2. Implement the pipeline stages with idempotent processing.
3. Add automated schema, null, duplicate, and business-rule checks.
4. Capture run metadata, rejected records, and performance metrics.
5. Add CI validation and publish screenshots or sample outputs.

## Definition of done

- Reproducible setup with no embedded credentials
- Incremental and restart-safe processing
- Automated tests and documented quality thresholds
- Observable runs with clear failure handling
- Architecture diagram and demonstration results

## Status

Portfolio scaffold created. Implementation milestones are tracked in the roadmap above.