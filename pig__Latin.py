#Ask the user to input a word in English.

print("Welcome to Pig Latin")
word  = input("Enter a word in english or in french:")
word  = word.lower()
kalima =len(word)


#the restart function
def restart():

        word  = input("Enter a word in english or in french:")
        kalima =len(word)
        if kalima >0 and word.isalpha():
            if word[0] == 'a' or word[0]== 'e' or word[0]=='i' or word[0]=='o' or word[0]=='u' :
                kalma =word + "yay"
                kalma = kalma.title()
                print(kalma)#Convert the word from English to Pig Latin.
                print("")
                restart()
            else :
                word = word[1:]+ word[0] +"ay"
                word = word.title()
                print(word)
                print("")
                restart()
            
        elif word.isnumeric() :
             print("no numbers")
             print("")
             restart()
        else :
            print("you have entered 0 words =< TRY AGAIN >=")
            print("")
            restart()
#Make sure the user entered a valid word.


if kalima >0 and word.isalpha():
       
       if word[0] == 'a' or word[0]== 'e' or word[0]=='i' or word[0]=='o' or word[0]=='u' :
          kalma =word + "yay"
          kalma = kalma.title()
          print(kalma)     
       else :
          word = word[1:]+ word[0] +"ay"
          word = word.title()
          print(word)#Convert the word from English to Pig Latin.
       print("")
       restart()
elif word.isnumeric() :
    print("No numbers")
    print("")
    restart()
else :
       print("you have entered 0 words =< TRY AGAIN >=")
       print("")
       restart()
