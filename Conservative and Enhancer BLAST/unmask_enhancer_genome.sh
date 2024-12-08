#!/bin/bash
# Change all the lower case to upper case (unmasking)
directory="/home/lhyun/Desktop/Capstone/Enhancer Data2"

for file in "$directory"/*.txt;
do
   base_name=$(basename "$file" .txt)
   output_file="${base_name}_unmasked.fasta"
   tr '[:lower:]' '[:upper:]' < "$file" > "$output_file"
done