configfile: "config.yaml"

rule add_header:
    input: 
        expand("datasets/reads_spike4/spike_gen_{variants}.fasta", variants=variants),
        fai="datasets/spike_for_gen/spike_gen_lambda_n.fasta.fai"
    output: expand("datasets/reads_spike4/{}.fasta",)
    shell: r'echo "$(samtools view -Ht {input}; cat {output})"> {output}'