import csv
import os

def is_duplicate(file_name, log_file="upload_logs.csv"):
    if not os.path.exists(log_file):
        return False
    with open(log_file, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["file_name"] == file_name:
                return True
    return False

# Example test
if __name__ == "__main__":
    name = "test_order1.pdf"
    if is_duplicate(name):
        print(f"⚠️  Duplicate found: {name}")
    else:
        print(f"✅  No duplicate: {name}")

