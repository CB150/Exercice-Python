#création de la fonction avec 2 paramètres
def distance_hamming(str1,str2):
	#mise à 0 du compteur
	cpt=0
	#si la taille d premier mot n'est pas égale à celle du deuxième
	if (len(str1)!=len(str2)):
		#le programme renvoie la phrase ci-dessous et met fin au programme.
		return("Les mots ne sont pas de la même longueur")
	#sinon pour i = a la taille du premier paramètre
	else:
		for i in range(len(str1)):
			#si l'itérateur de la boucle du premier paramètre est différent de l'itérateur du second paramètre
			if str1[i]!=str2[i]:
				#incrémentation du compteur
				cpt+=1
				#on nous retourne la valeur du compteur.
	return(cpt)


mm1=input("entrer le premier mot")
mm2=input("entrer le deuxieme mot")
print(distance_hamming(mm1,mm2))

