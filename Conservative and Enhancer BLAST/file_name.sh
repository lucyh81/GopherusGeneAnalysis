#!/bin/bash
# chaning file name into the format "_um_blast.txt"
echo "Searching for files..."
files=$(find . -maxdepth 2 -type f -name '*_um_blast.txt')

if [ -z "$files" ]; then
  echo "No files founds."
else
  for file in $files;
    do
      echo "Files found:"  echo "Files found:"
      cat "$file"
      echo "--------------------------------------------"
    done
fi