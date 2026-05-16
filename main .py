import random
words=["apple","mango","grapes","orrange","banana"]
word=random.choice(words)
guessed=[]
attempts=6
print("Welcome to Hangman Game")
while attempts>0:
    display=""
    for letter in word:
        if letter in guessed:
            display+=letter +""
        else:
            display+="_"
    print("word/n:",display)
    if"_"not in display:
            print("You Won!")
            break
    guess=input("Enter a letter:")
    if guess in word:
       guessed.append(guess)
       print("Correct!")
    else:
       attempts==1
       print("Wrong!attempts left:",attempts)
    if attempts==0:                
        print("You lost!The word  was:",word)
            
            
            
                
          

     
