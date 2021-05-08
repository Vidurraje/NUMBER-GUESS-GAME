print("*"*100)
text= "WELCOME TO NUMBER GUESS GAME "
a=text.center(100)
print(a)
print("*"*100)
x = 20
limit = 0
try:
    print("You have 8 Guess only : ")
    print("*" * 100)
    while limit < 8:
        guess_no = int(input("Enter the guess number:  "))
        if guess_no < 20:
            print("**** Number is low , try higher one****  ")
        elif guess_no > 20:
            print("**** Number is high , try lower one****   ")
        else :
            print("*"*45,"YOU WON","*"*45)
            print(" Yeahh !!! You guess the correct one " )
            print("*" * 100)
            print("You take ",limit,"Guess")
            break
        print("geuses left",7-limit)
        limit=limit+1

    if limit>8:
        print("You exceed the limit of guesses ")
except:
    print("Please enter any valid number ")
