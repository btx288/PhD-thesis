#!/usr/bin/env Rscript
#passing arguments
args = commandArgs(trailingOnly=TRUE)
#importing data
chromosomes_annotation_gff3 <- read.delim(args[1], header = F, comment.char="#")
transposable_annotation_gff3 <- read.delim(args[2], header = F, comment.char="#")
chromosome_gff <- subset(chromosomes_annotation_gff3, chromosomes_annotation_gff3$V1==args[3])
transposable_gff <- subset(transposable_annotation_gff3, transposable_annotation_gff3$V1==args[3])
transposable_gff <- na.omit(transposable_gff)
chromosome_gff <- na.omit(chromosome_gff)
if (length(args)==4) {
  chromosome_gff <- chromosome_gff[chromosome_gff[,3]==args[4],]
}
min=100000000000
minus=0
minimum=c()
num_1=0
num_2=0
for (i in 1:nrow(transposable_gff)){
  print(i)
  trans_start <- transposable_gff$V4[i]
  trans_end <- transposable_gff$V5[i]
  min=10000000000000
  min_1=10000000000000
  min_2=10000000000000
  for (n in 1:nrow(chromosome_gff)){
    genes_start<- chromosome_gff$V4[n]
    genes_end<- chromosome_gff$V5[n]
    minus_1= genes_start - trans_end
    minus_2= trans_start - genes_end
    if (minus_1 < min_1){
      if (minus_1 >0){
        min_1=minus_1
        num_1 = n
      }
    }
    if (minus_2 > 0){
      if (minus_2 < min_2){
        min_2=minus_2
        num_2 = n
      }
    }
    if(min_1 < min_2){
      min=min_1
      num=num_1
    }else{
      min=min_2
      num=num_2}
  }
  print(paste0(i, " ",min," ", num," ", chromosome_gff$V9[num]))
  minimum <- rbind(minimum, c(transposable_gff[i, ],min, num, chromosome_gff[num,]))
}
write.csv(minimum, paste0("minumum_chromosome_",args[3],"_", args[2],".csv"))
