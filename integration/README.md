# Week 1: Cloud Integration Setup (Alyssa Cintron)

## Overview
Initial setup for the data pipeline and upload integration.

### 1. Upload Logging
- File: `upload_logs.csv`
- Tracks file name, upload time, user, S3 URL, and upload status.

### 2. Duplicate Detection
- File: `duplicate_check.py`
- Prevents re-uploading of the same file based on file name.

### 3. OCR Text Schema
- File: `extracted_text_schema.json`
- Defines structure for Nerea’s OCR output (file name, upload time, extracted text, etc.).

### 4. Data Flow Sketch
- File: `data_flow_sketch.md`
- Shows the process from Upload → S3 → Extraction → Review Interface.

---

**Next Week Preview:** JSON validation, test cases, and database migration plan.
---

## Week 2: Validation & Database Prep

### 1. JSON Validation
- Created `validate_json.py` to check OCR output against `extracted_text_schema.json`.

### 2. Upload Log Enhancement
- Added `Extraction_Status` column to `upload_logs.csv`.

### 3. Testing
- Created `tests.py` for duplicate detection and upload log validation.

### 4. Database Migration Plan
- Added `database_plan.md` outlining transition from CSV to SQLite.

