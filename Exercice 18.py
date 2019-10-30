#création de la fonction avec 3 paramètres
def trouverLeCoupableIte(suspect, brin1, brin2):
	brin1in = False
	brin2in = False
	i = 0
	tmp = []

	#tant que brin1in ou brin2in sont faux et i est inférieur au nombre d'éléments de suspect moins le nombre d'éléments de brin1
	while ((not brin1in or not brin2in) and i < len(suspect) - len(brin1)):

		tmp = suspect[i:]#supprime les i éléments de la liste
		tmp = tmp[:-(len(suspect) - len(brin1) - i)] #laisse 4 éléments dans la liste

        #si tmp = brin 1 et que brin1in est faux
		if (brin1 == tmp and brin1in == False):
			i += 4 #on incrémente i de 4
			brin1in = True #brin1in devient vrai
        #si tmp = brin 2 et que brin2in est faux
		elif (brin2 == tmp and brin2in == False):
			i += 4 #on incrémente i de 4
			brin2in = True #brin1in devient vrai
		#si brin1in = brin2in = True
		elif (brin1in == brin2in == True):
			return (brin1in and brin2in) #on renvoie leur valeur
		#sinon on incrémente i de 1
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





