# To implement "MInetworkcalculate.pl" the MI-STN paper

from random import randint
from Bio import pairwise2
#import numpy as np


def getMutMatrix(tempSeq,nYears) :
	mutMatrix = []
	for i in range(1,len(TempSeq)):
		print i
		if i%nYears == 0:
			continue;
		s1 = TempSeq[i-1]
		s2 = TempSeq[i]
		str1 = s1.split('\t')
		str2 = s2.split('\t')
		s1 = str1[1]
		s2 = str2[1]
		alignments = pairwise2.align.globalms(s1, s2,2,-1,-5,-5)
		news1 = alignments[0][0]
		news2 = alignments[0][1]
		#print news1
		#print news2
		flags = list(i[0] != i[1] for i in zip(news1, news2))
		#aRow = 1*numpy.array(flags)
		aRow = []
		for i in range(1,len(flags)):
			aRow.append(int(flags[i-1]))
		mutMatrix.append(aRow)
		#print aRow
	return mutMatrix



if __name__ == '__main__' :
	Round = 1000 #500 # number of re-sampling: 500 or 1000 or ...
	year1=2000  #1975
	year2=2015
	AllSeq = {} 
	for y in range(year1,year2+1):
		filename = str(y)+".txt"
		f = open(filename)
		Seqs = []
		for line in f:
			#aRow = line.split('\t')
			#aRow2 = aRow[1]
			sq = line.replace("\n", "")
			Seqs.append(sq)
		AllSeq[y] = Seqs;
	
	TempSeq = []
	for i in range(1,Round+1):	
		for y in range(year1,year2+1):
			N = len(AllSeq[y])
			#print y
			r = randint(1,N)
			TempSeq.append(AllSeq[y][r-1])
	
	filename = "TempSeq.txt"
	f = open(filename, 'w+')
	for i in range(1,len(TempSeq)+1):
		s = TempSeq[i-1]
		f.write("%s\n" % (s))
	f.close()
	# f = open("TempSeq.txt")
	# TempSeq = []
	# for line in f:
		# sq = line.replace("\n", "")
		# TempSeq.append(sq)
	
	nY = year2 - year1 +1	
	MutMatrix = getMutMatrix(TempSeq,nY)
	
	filename = "MutMatrix.txt"
	fw = open(filename, 'w+')
	for i in range(1,len(MutMatrix)+1):
		Seq_t = MutMatrix[i-1]
		type(Seq_t)
		#print Seq_t
		Seq = ','.join(str(v) for v in Seq_t)
		#print Seq
		fw.write("%s\n" % (Seq))
	fw.close()
	
	
	