import os
import datetime

def shell(command):
    """
    Run a shell command and return the output.
    """
    return os.popen(command, 'r').read()


def simulate_mixture(ref_folder):
    """
    Simulate a mixture of reads from reference genomes. Uses SImSeq on each reference file and then concatenates the results.
    """
    output_dir_taged = output_dir + str(len(os.listdir('datasets')))
    os.mkdir(output_dir_taged)
    # get fasta files 
    refs = [f for f in os.listdir(ref_folder) if f.endswith('.fasta')]

    for i, ref in enumerate(refs):
        read_num = int(proportions[i%len(proportions)] * reads_total)
        out_path = os.path.join(output_dir_taged, ref[:-6]+'.sam')
        ref_path = os.path.join (ref_folder, ref)

        sim_command = f"""java -jar -Xmx2048m {SimSeq} -1 100 -2 100 \
        --error {error_paths[0]} \
        --error2 {error_paths[1]} \
        --insert_size 3000 --insert_stdev 300 \
        --mate_pair --mate_frag 500 --mate_frag_stdev 50 \
        --mate_pulldown_error_p 0.3 --read_number {read_num} \
        --read_prefix beta_ --reference {ref_path} \
        --duplicate_probability 0.01 --out {out_path}"""
        
        console_out = shell(sim_command)
        print(console_out)

        # concatenate resulting .sam files
        # if i == 0:
        #     os.system(f'cat {out_path} > {res_path}')
        # else:
        #     os.system(f'cat {out_path} >> {res_path}')


        
        


proportions = [0.3,0.25,0.2,0.15,0.1]
reads_total = 15000
SimSeq = "SimSeq/SimSeqNBProject/store/SimSeq.jar"
error_paths = ["SimSeq/examples/hiseq_mito_default_bwa_mapping_mq10_1.txt", "SimSeq/examples/hiseq_mito_default_bwa_mapping_mq10_2.txt"]
ref_folder = "datasets/spike_for_gen"
output_dir = "datasets/reads_spike"



if __name__ == "__main__":
    simulate_mixture(ref_folder)