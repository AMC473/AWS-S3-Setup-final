# Database Migration Plan (CSV → SQLite)

## Purpose
Replace the flat CSV log with a relational SQLite database for better querying and scalability.

## Proposed Table: uploads
| Column | Type | Description |
|---------|------|-------------|
| id | INTEGER PRIMARY KEY | Unique identifier |
| file_name | TEXT | Name of uploaded file |
| upload_time | TEXT | Timestamp of upload |
| user_id | TEXT | Uploader |
| s3_url | TEXT | Cloud storage location |
| upload_status | TEXT | "Success" / "Failed" |
| extraction_status | TEXT | "Pending" / "Success" / "Failed" |

## Migration Steps
1. Read data from `upload_logs.csv`
2. Create `uploads` table in SQLite
3. Insert CSV rows into database
4. Verify record count and data integrity
5. Deprecate CSV once database fully tested
