

from Bio import pairwise2



if __name__ == '__main__' :
	filename = "fluB_Yam_Vic.txt"
	f = open(filename)
	Seqs = []
	for line in f:
		aRow = line.split('\t')
		aRow2 = aRow[1]
		sq = aRow2.replace("\n", "")
		Seqs.append(sq)
	#mutMatrix = []
	for i in range(1,len(Seqs)):		
		s1 = Seqs[i-1]
		s2 = Seqs[i]
		alignments = pairwise2.align.globalms(s1, s2,2,-1,-5,-5)
		news1 = alignments[0][0]
		news2 = alignments[0][1]
		print news1
		print news2
		flags = list(i[0] != i[1] for i in zip(news1, news2))
		#flags = list(i[0] != i[1] for i in zip(s1, s2))
		aRow = []
		for i in range(1,len(flags)):
			aRow.append(int(flags[i-1]))
		print aRow
		#mutMatrix.append(aRow)
	fw = open("fluB_YamVic_diff.txt",'w+')
	dSeq = ','.join(str(v) for v in aRow)
	fw.write("%s\n" % (dSeq))
	fw.close()	