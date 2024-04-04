									#Save the read ID and hit ID, hit length, length of query in HSP, and % identity for top HSP to a file 
									print OUTPUT $id, "\t", $hit->name, "\t", $hit->length, "\t", $hsp->length('query'), "\t", $hsp->percent_identity, "\n";
									#add current query/subject pair to scalar of all read pairs that have been printed to output file
									$all_read_pairs_with_hits .= $current_read_pair_with_hit;
									#print "These are all the read pairs with hits currently stored: '$all_read_pairs_with_hits'\n";
							}		
						}
					}
				}
			}
		#if the current BLAST results contains no hits print message to screen
		} else {
			#print "no hit\n";
		
		#increment counter (number of results that have been parsed)
		++$counter;
			
	}
	
}

   
#close output files
close OUTPUT;

exit;
