#création de la fonction avec 1 paramètre
def palindrome(str):
	print("message", str)
	#si la taille du 1er paramètre tombe a 1 ou à 0, alors on renvoie True car le mot est palindrome
	if str == [] or len(str) == 1:
		return True
	else:
		#sinon, si le premier caractère du paramètre est égale au dernier caractère,
		if str[0] == str[len(str) - 1]: alors on enlève le premier et le dernier caractère de la liste et on relance la fonction
			str = str[1:]
			str = str[:-1]
			return (palindrome(str))
		else:
			#si la condition d'avant est fausse, alors on renvoie False
			return False

mot=input("entre le mot ")
print(palindrome(mot))