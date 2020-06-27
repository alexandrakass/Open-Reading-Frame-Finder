from Bio import SeqIO
start_codon = ["a","t","g"]
stop_codon = [["t","a","g"],["t","g","a"],["t","a","a"]]
dafterstart = []; dafterstop = []

# This function reads in the FASTA file and returns a list of seq objects
def parse_fasta(file_name):
    alist = []
    try:
        for seq_record in SeqIO.parse(file_name, "fasta"):
            alist.append(seq_record)

    except IOError:
        print("The file does not exist")

    return alist


def quickView(seq_list):
    for index, record in enumerate(seq_list):
        print("index %i, ID = %s, length %i, with %i features"
              % (index, record.id, len(record.seq), len(record.features)))



def has_start_codon(seq):
    start_codon = ["a", "t", "g"]
    for j in range(len(seq)):
        a = 0  # we will use a to iterate through the start_codon list
        b = j  # we will use b to store the index of our iterator

        # We are comparing the nucleotide at position b in the
        # sequence (seq) to the nucleotide at position a in the start_codon list
        if (seq[b] == start_codon[a]):
            a += 1  # incrementing start_codon list by 1
            b += 1  # incrementing the index in seq by 1 or just moving to the next base pair

            # We are now checking that the base pair at position b is the same
            # as position a in start_codon list
            if (seq[b] == start_codon[a]):
                a += 1
                b += 1

                # We are doing a check on the third base pair from the position
                # we started in and checking if it matches position a in our
                # startcodon list
                if (seq[b] == start_codon[a]):
                    # We are saving the first position that we started at if all
                    # three base pairs in our sequence matched our start codon
                    dafterstart.append(j)

    dafterstart.sort()
    return dafterstart


def has_stop_codon(seq):
    stop_codon = [["t", "a", "g"], ["t", "g", "a"], ["t", "a", "a"]]
    for i in range(len(stop_codon)):
        for j in range(len(seq) - 1):
            a = 0
            b = j

            if (seq[b] == stop_codon[i][a]):
                a += 1
                b += 1

                if (seq[b] == stop_codon[i][a]):
                    a += 1
                    b += 1

                    if (seq[b] == stop_codon[i][a]):
                        dafterstop.append(j)

    dafterstop.sort()
    return dafterstop

def find_orf(startList, stopList, frame):
    frame = frame - 1  # Subtracting 1 b/c the user will input 1,2,3 and index starts at 0
    orf_list = []  # Create a list to store the ORFs in
    i = 0; j = 0; a = 0; b = 0;

    for i in range(len(startList)):
        a = i
        for j in range(len(stopList)):
            b = j
            if (stopList[j] > startList[i]):

                if ((startList[i] % 3) == frame):

                    if ((stopList[j] % 3) == frame):
                        orf = (dafterstart[i], dafterstop[j])
                        orf_list.append(orf)
                        break
                    else:
                        j += 1
                else:
                    i += 1
                    break
            else: j += 1
        j = b
    i = a

    return orf_list
