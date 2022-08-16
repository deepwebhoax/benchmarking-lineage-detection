

def hamming(str1, str2):
    l = min(len(str1), len(str2))
    miss = 0

    for i in range(l):
        if str1[i] != str2[i]:
            miss += 1

    return miss / l

def hamming_fasta(filename1, filename2):
    h = []
    with open(filename1, 'r') as f1, open(filename2, 'r') as f2:
        while True:
            line1 = f1.readline()
            line2 = f2.readline()

            if line1 == '' or line2 == '':
                break

            if line1[0] == '>' or line2[0] == '>':
                continue

            h.append(hamming(line1, line2))

    return sum(h) / len(h)


import sys

if __name__ == '__main__':
    # checking if arguments are fasta or fastq files
    if len(sys.argv) != 3:
        print('Usage: ham.py file1.fasta file2.fasta')
        sys.exit(1)
    elif not sys.argv[1].endswith(('.fasta', '.fastq')) or not sys.argv[2].endswith(('.fasta', '.fastq')):
        print('Usage: ham.py file1.fasta file2.fasta')
        sys.exit(1)
    print(hamming_fasta(sys.argv[1], sys.argv[2]))
    
