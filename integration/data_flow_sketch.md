# Data Flow Sketch (Week 1)

**Upload → S3 → Text Extraction → Review Interface**

1. User uploads PDF to the web app.  
2. File is stored in **AWS S3**.  
3. A record is logged in `upload_logs.csv`.  
4. Nerea’s OCR module extracts text and saves JSON following `extracted_text_schema.json`.  
5. Extracted text is reviewed by the QA interface.  
6. Duplicate check runs to prevent re-uploads.
