#consonant or vowel program
print("Vowel or consonant finder \n =============" )
letter= input("Enter any alphabet :\n")

#checking if its conosnant or a vowel
if( (letter=="a") | (letter=="e") | (letter =="i" ) | (letter =="o") | (letter =="u") ):
    print(letter, "is a vowel")
else:
    print(letter,"is a consonant")
