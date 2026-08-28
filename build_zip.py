"""
Automated LOC Verification & Project Packaging Tool
OmniSolve EduClear - Academic Doubt Clarification Platform
"""

import os
import zipfile

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_ZIP_NAME = "EduClear_Student_Doubt_Website.zip"
OUTPUT_ZIP_PATH = os.path.join(PROJECT_DIR, OUTPUT_ZIP_NAME)

VALID_EXTENSIONS = {'.py', '.js', '.css', '.html', '.md', '.json'}
EXCLUDE_DIRS = {'.git', '__pycache__', 'staticfiles', 'media', 'node_modules', '.idea', '.vscode'}
EXCLUDE_FILES = {OUTPUT_ZIP_NAME, 'db.sqlite3'}

def count_and_package():
    print("=" * 70)
    print("       OmniSolve EduClear - LOC Verification & Packaging Tool        ")
    print("=" * 70)

    total_lines = 0
    file_counts = {}

    with zipfile.ZipFile(OUTPUT_ZIP_PATH, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(PROJECT_DIR):
            # Exclude directories in-place
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

            for file in files:
                if file in EXCLUDE_FILES or file.endswith('.zip') or file.endswith('.pyc'):
                    continue

                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, PROJECT_DIR)

                # Add file to zip archive
                zipf.write(full_path, rel_path)

                # Count lines for valid code files
                ext = os.path.splitext(file)[1].lower()
                if ext in VALID_EXTENSIONS:
                    try:
                        with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                            lines = f.readlines()
                            line_count = len(lines)
                            total_lines += line_count
                            file_counts[rel_path] = line_count
                    except Exception as e:
                        print(f"Warning: Could not count lines in {rel_path}: {e}")

    print("\nFile Breakdown (Top Contributors):")
    sorted_files = sorted(file_counts.items(), key=lambda x: x[1], reverse=True)
    for rel_path, count in sorted_files[:15]:
        print(f"  - {rel_path}: {count:,} LOC")

    print("-" * 70)
    print(f"Total Code File Count  : {len(file_counts)} files")
    print(f"Total Lines of Code    : {total_lines:,} LOC")
    print(f"Deliverable Zip File   : {OUTPUT_ZIP_PATH}")
    print(f"Zip File Size          : {os.path.getsize(OUTPUT_ZIP_PATH) / (1024*1024):.2f} MB")
    print("=" * 70)

    if total_lines >= 50000:
        print(" SUCCESS: Total Lines of Code strictly EXCEEDS 50,000 LOC requirement!")
    else:
        print(f" WARNING: LOC count is {total_lines}, which is below 50,000 LOC target.")

if __name__ == '__main__':
    count_and_package()
