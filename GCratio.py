output_file = open( b,'w')
output_file.write('Gene\tA\tC\tG\tT\tLength\tCG%\n')
from Bio import SeqIO
cg_percentage_total = 0
number_sequences = 0
length_total = 0
cg_sum = 0
for cur_record in SeqIO.parse(input_file, "fasta") :
        #count nucleotides in this record...
        gene_name = cur_record.name
        A_count = cur_record.seq.count('A')
        C_count = cur_record.seq.count('C')
        G_count = cur_record.seq.count('G')
        T_count = cur_record.seq.count('T')
        length = len(cur_record.seq)
        length_total = length_total + length
        cg_sum = cg_sum + C_count + G_count
        cg_percentage = float(C_count + G_count) / length
        cg_percentage_total = cg_percentage_total + cg_percentage
        number_sequences = number_sequences + 1
        output_line = '%s\t%i\t%i\t%i\t%i\t%i\t%f\n' % (gene_name, A_count, C_count, G_count, T_count, length, cg_percentage)
        output_file.write(output_line)
output_file.close()
input_file.close()
import os
dirpath = os.getcwd()
foldername = os.path.basename(dirpath)
print ("In cluster /t" + foldername, "/t, total percentage of CG content is : /t", float(cg_percentage_total / number_sequences), "/t, and /t", float(cg_sum)/length_total)
#
#If you run this program on that instead, you will get
#a single line output containing the data for the whole
#genome (genes and all the DNA inbetween).  The GC% for
#this is 31.6% (to one decimal place).
