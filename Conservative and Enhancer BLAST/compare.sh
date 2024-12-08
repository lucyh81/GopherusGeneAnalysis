#!/bin/bash
#To find the matching mutation and the conservative enhancer

id="scaffold_114"
start=749085

end=748722


awk '{if ($1 == "'$id'") {print}}' Goph_FST_SNPS.vcf | awk '{if ($2 > '$start') {print}}' | awk '{if ($2 < '$end') {print}}'