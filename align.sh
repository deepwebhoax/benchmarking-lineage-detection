#!/bin/bash

help=0
helpFunction()
{
   echo ""
   echo "Usage:\n source align.sh -i reads -r ref"
   echo -e "\t-i input reads .sam file"
   echo -e "\t-r reference fasta file"
   help=1
}

while getopts "i:r:" opt
do
   echo "8"
   case "$opt" in
      i ) reads="$OPTARG" ;;
      r ) ref="$OPTARG" ;;
      h ) helpFunction ;;
      ? ) helpFunction ;; # Print helpFunction in case parameter is non-existent
   esac
   echo "9"
done

echo "${ref}1"
echo "${reads}2"

# Print helpFunction in case parameters are empty
if [ -z "$reads" ] || [ -z "$ref" ]
then
   echo "Some or all of the parameters are empty";
   helpFunction
fi

if [ ${help} -eq 0 ]
then
# Begin script in case all parameters are correct
echo "$ref"
echo "$reads"

out_dir="$(dirname ${reads})/res_align"
mkdir ${out_dir}
echo "$out_dir"
samtools view -bS -T "$ref" -o "${out_dir}/out.bam" $reads
samtools sort "${out_dir}/out.bam" -o "${out_dir}/out_sorted.bam"
samtools index "${out_dir}/out_sorted.bam"
samtools tview "${out_dir}/out_sorted.bam" $ref

fi

