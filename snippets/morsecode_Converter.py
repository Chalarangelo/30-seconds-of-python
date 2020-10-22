# Python program to implement Morse Code Translator 

# Dictionary representing the morse code chart 
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-'} 

# Function to encrypt the string 
# according to the morse code chart 
def encrypt(message): 
	cipher = '' 
	for letter in message: 
		if letter != ' ': 
			# morse codes for different characters 
			cipher += MORSE_CODE_DICT[letter] + ' '
		else: 
			# 1 space indicates different characters and 2 indicates different words 
			cipher += ' '
	return cipher 

# Function to decrypt the string 
# from morse to english 
def decrypt(message): 
	# extra space added at the end to access the last morse code 
	message += ' '
	decipher = '' 
	citext = '' 
	for letter in message: 
		# checks for space 
		if (letter != ' '): 
			i = 0
			# storing morse code of a single character 
			citext += letter 
		# in case of space 
		else: 
			# if i = 1 that indicates a new character 
			i += 1

			# if i = 2 that indicates a new word 
			if i == 2 : 

				# adding space to separate words 
				decipher += ' '
			else: 

				# accessing the keys using their values (reverse of encryption) 
				decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT 
				.values()).index(citext)] 
				citext = '' 
	return decipher 
print("From English word to morse coded text----------------->")
message = "THIS IS GITHUB-HACKTOBERFEST"
toMorseCode = encrypt(message.upper()) 
print("The original message is", message, "and the morsecode meassge is", toMorseCode) 

print()
print("From morse coded text to English word----------------->")
morseCodeMessage = "- .... .. ...  .. ...  --. .. - .... ..- -... -....- .... .- -.-. -.- - --- -... . .-. ..-. . ... -"
toEnglishWord = decrypt(morseCodeMessage)
print("The morse-coded message is", morseCodeMessage, "and the English word is", toEnglishWord)
print("\n\n")

choice = input("Wanna try out this? Enter Yes/No : ")
if choice == "Yes":
  word = input("Enter any english word with only alphabets and numbers  :  ")
  print("Morse coded text = ")
  print(encrypt(word.upper()))
else:
  print("Ok for more details, checkout the docs related to morse code that is uploaded")





