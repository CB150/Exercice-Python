def palindrome(str):
	print("message", str)
	if str == [] or len(str) == 1:
		return True
	else:
		if str[0] == str[len(str) - 1]:

			str = str[1:]
			str = str[:-1]
			return (palindrome(str))
		else:
			return False

ant=input("entre le mot ")
print(palindrome(ant))
#print(palindrome("kayak"))