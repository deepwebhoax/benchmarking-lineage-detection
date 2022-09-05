import os

ref_folder = 'datasets/variant_references'
save_folder = 'datasets/spike_for_gen'

i1, i2 = 21563, 25384
trim = 50

# list of all files in the reference folder
files = [f for f in os.listdir(ref_folder) if os.path.isfile(os.path.join(ref_folder, f))]

if os.path.exists(os.path.join(save_folder)):
    os.system('rm -rf ' + os.path.join(save_folder))
os.mkdir(os.path.join(save_folder))
for file in files:
    with open(os.path.join(ref_folder, file)) as f:
        title = f.readline()
        seq = f.read()
        spike = seq[i1+trim:i2-trim]
    
        with open(os.path.join(save_folder, 'spike_gen_' + file), 'w') as f_spike:
            f_spike.write(title)
            f_spike.write(spike)
