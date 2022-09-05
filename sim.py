import sys, os


def shell(command):
    """
    Run a shell command and return the output.
    """
    return os.popen(command, 'r').read()


def simulate_mixture(ref_folder):
    """
    Simulate a mixture of reads from reference genomes. Uses SImSeq on each reference file and then concatenates the results.
    """
    refs = os.listdir(ref_folder)
    for i, ref in enumerate(refs):
        read_num = proportions[i%len(proportions)] * reads_total
        out_path = os.path.join(output_dir, str(i)+'.sam')
        ref_path = os.path.join (ref_folder, ref)

        sim_command = f"""java -jar -Xmx2048m {SimSeq} -1 100 -2 100 \
        --error examples/hiseq_mito_default_bwa_mapping_mq10_1.txt \
        --error2 examples/hiseq_mito_default_bwa_mapping_mq10_2.txt \
        --insert_size 3000 --insert_stdev 300 \
        --mate_pair --mate_frag 500 --mate_frag_stdev 50 \
        --mate_pulldown_error_p 0.3 --read_number {read_num} \
        --read_prefix beta_ --reference {ref_path} \
        --duplicate_probability 0.01 --out {out_path}"""
        
        shell(sim_command)

        # concatenate resulting .sam files
        if i == 0:
            os.system(f'cat {out_path} > {res_path}')
        else:
            os.system(f'cat {out_path} >> {res_path}')


        
        


proportions = [0.3,0.25,0.2,0.15,0.1]
reads_total = 15000
SimSeq = "SimSeqNBProject/store/SimSeq.jar"
ref_folder = "datasets/spike_for_gen"
output_dir = "tests/covid/res"
