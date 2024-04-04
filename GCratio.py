    #
    #The \ character means this command continues on the
    #next line
    output_line = '%s\t%i\t%i\t%i\t%i\t%i\t%f\n' % \
    (gene_name, A_count, C_count, G_count, T_count, length, cg_percentage)

    # 
    output_file.write(output_line)

#Now we have finished all the genes, we can close the output file:
output_file.close()

#and close the input file:
input_file.close()

#If you run this program and then open the output file
#'nucleotide_counts.tsv' in your spreadsheet
#(e.g. Microsoft Excel) you can do things like sort
#the genes by length of GC percentage.
#
#For example, you can see the GC% ranges from 22.8%
#up to 43.3% (to one decimal place) for 'NC_005213.ffn'
#
#You can also download the complete genome's nucleotide
#sequence, file 'NC_005213.fna'.
#
#If you run this program on that instead, you will get
#a single line output containing the data for the whole
#genome (genes and all the DNA inbetween).  The GC% for
#this is 31.6% (to one decimal place).
