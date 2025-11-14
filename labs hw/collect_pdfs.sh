#!/bin/bash

# Script to collect all PDFs from labs hw subdirectories into a pdfs folder

# Create pdfs directory if it doesn't exist
mkdir -p pdfs

# Find and copy all PDF files to pdfs directory (excluding pd2752 pattern)
find . -name "*.pdf" -type f -not -path "./pdfs/*" -not -name "pd2752*" -exec cp {} pdfs/ \;

echo "All PDFs have been copied to the pdfs folder"
ls -lh pdfs/
