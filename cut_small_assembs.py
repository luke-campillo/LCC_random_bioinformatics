import os

seqs = "for file in *.FNA ; do grep '^>' $file | wc -l | sed 's/^[ \t]*//'; done > seq_count.txt"
 
files = "ls *.FNA > file_names.txt"

combine = "paste file_names.txt seq_count.txt | column -s ',' -t > count_aligns.txt"

os.system(seqs)
os.system(files)
os.system(combine)

with open ("count_aligns.txt") as f:
	for line in f:
		line = line.strip()
		line = line.split("\t")
		if int(line[1]) <= 3:
			os.remove(line[0])