def trouverLeCoupableIte(suspect, brin1, brin2):
	brin1in = False
	brin2in = False

	i = 0
	tmp = []
	while ((not brin1in or not brin2in) and i < len(suspect) - len(brin1)):

		tmp = suspect[i:]
		tmp = tmp[:-(len(suspect) - len(brin1) - i)]

		if (brin1 == tmp and brin1in == False):
			i += 4
			brin1in = True
		elif (brin2 == tmp and brin2in == False):
			i += 4
			brin2in = True
		elif (brin1in == brin2in == True):
			return (brin1in and brin2in)
		else:
			i += 1

	return (brin1in and brin2in)

rose="CTCCTGATGCTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAD"
moutarde="CCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCADN"
pervenche="AAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGTACTCCGCGCGCCGGGACAGAATGCCADN"
leblanc="CTGCAGGAACTTCTTCTGGAAGTACTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAG"

nomcoupable=["rose","moutarde","pervenche","leblanc"]
listeCoupable=[rose,moutarde,pervenche,leblanc]

premier="CATA"
deuxieme="ATGC"


for i in range (len(listeCoupable)):
	print(nomcoupable[i]," ",trouverLeCoupableIte(listeCoupable[i],premier,deuxieme))





