java -jar -Xmx2048m SimSeqNBProject/store/SimSeq.jar -1 100 -2 100 \
    --error examples/hiseq_mito_default_bwa_mapping_mq10_1.txt \
    --error2 examples/hiseq_mito_default_bwa_mapping_mq10_2.txt \
    --insert_size 3000 --insert_stdev 300 \
    --mate_pair --mate_frag 500 --mate_frag_stdev 50 \
    --mate_pulldown_error_p 0.3 --read_number 3000 \
    --read_prefix alpha_ --reference tests/covid/alpha.fasta \
    --duplicate_probability 0.01 --out tests/covid/res/alpha.sam

java -jar -Xmx2048m SimSeqNBProject/store/SimSeq.jar -1 100 -2 100 \
    --error examples/hiseq_mito_default_bwa_mapping_mq10_1.txt \
    --error2 examples/hiseq_mito_default_bwa_mapping_mq10_2.txt \
    --insert_size 3000 --insert_stdev 300 \
    --mate_pair --mate_frag 500 --mate_frag_stdev 50 \
    --mate_pulldown_error_p 0.3 --read_number 2500 \
    --read_prefix beta_ --reference tests/covid/beta.fasta \
    --duplicate_probability 0.01 --out tests/covid/res/beta.sam

java -jar -Xmx2048m SimSeqNBProject/store/SimSeq.jar -1 100 -2 100 \
    --error examples/hiseq_mito_default_bwa_mapping_mq10_1.txt \
    --error2 examples/hiseq_mito_default_bwa_mapping_mq10_2.txt \
    --insert_size 3000 --insert_stdev 300 \
    --mate_pair --mate_frag 500 --mate_frag_stdev 50 \
    --mate_pulldown_error_p 0.3 --read_number 2000 \
    --read_prefix delta_ --reference tests/covid/delta.fasta \
    --duplicate_probability 0.01 --out tests/covid/res/delta.sam

java -jar -Xmx2048m SimSeqNBProject/store/SimSeq.jar -1 100 -2 100 \
    --error examples/hiseq_mito_default_bwa_mapping_mq10_1.txt \
    --error2 examples/hiseq_mito_default_bwa_mapping_mq10_2.txt \
    --insert_size 3000 --insert_stdev 300 \
    --mate_pair --mate_frag 500 --mate_frag_stdev 50 \
    --mate_pulldown_error_p 0.3 --read_number 1500 \
    --read_prefix lambda_ --reference tests/covid/lambda.fasta \
    --duplicate_probability 0.01 --out tests/covid/res/lambda.sam

java -jar -Xmx2048m SimSeqNBProject/store/SimSeq.jar -1 100 -2 100 \
    --error examples/hiseq_mito_default_bwa_mapping_mq10_1.txt \
    --error2 examples/hiseq_mito_default_bwa_mapping_mq10_2.txt \
    --insert_size 3000 --insert_stdev 300 \
    --mate_pair --mate_frag 500 --mate_frag_stdev 50 \
    --mate_pulldown_error_p 0.3 --read_number 1000 \
    --read_prefix omicron_ --reference tests/covid/omicron.fasta \
    --duplicate_probability 0.01 --out tests/covid/res/omicron.sam

