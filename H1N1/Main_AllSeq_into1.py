


if __name__ == '__main__' :
	count = 0; # number of not HA1 seq
	
	fw = open("AllSeq_H1N1.txt", 'w+')
	
	year1 = 1976
	year2 = 2015
	for y in range(year1,year2+1):
		filename = str(y)+".txt"
		f = open(filename)
		Seqs = []
		for line in f:
			count = count+1
			aRow = line.split('\t')
			ID = str(y) +"_"+ aRow[0]
			sq = aRow[1].replace("\n", "")
			#Seqs.append(sq)
			fw.write("%s\t%s\n" % (ID,sq))
		#AllSeq[y] = Seqs;
	fw.close()	
	print count		
	
	
	
