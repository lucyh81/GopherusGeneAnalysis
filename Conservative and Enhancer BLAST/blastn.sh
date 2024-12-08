#!/bin/bash
#blasting enhancers and Gopherus agassizii genome 

blast_dir="/home/lhyun/Desktop/Capstone/Enhancer Data2"
blast_db="../Gaga_nucdb"

num_threads=4
evalue=100000

for file in *.fasta; do
  base_name=$(basename "$file" .fasta)
  new_base_name=${base_name/_unmasked/_um}

  blastn -query "$file" \
        -db "$blast_db" \
        -outfmt "7 qseqid sseqid length qlen slen qstart qend sstart send evalue" \
        -out "${blast_dir}/${new_base_name}_blast.txt" \
        -num_threads "$num_threads" \
        -evalue "$evalue"
done