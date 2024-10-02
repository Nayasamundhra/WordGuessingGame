import random
title="WordWizard"
s=0
word_bank=[]
f=open("newlist.txt","r")
con=f.readlines()
for word in con:
    a=word.rstrip("\n")
    ab=a.lower()
    word_bank.append(ab)
f.close()
select=random.choice(word_bank)
max_turns=5
cur_turns=1
rem_turns=5
print("Welcome To "+title)
print("You are expected to guess a 5-LETTER WORD")
print("Maximum chances provided are 5")
print("All The Best!!")
print()
misplace=[]
for i in range(0,max_turns,1):
    correct=[]
    
    incorrect=[]
    a=input("what is your guess: ")
    guess=a.lower()
    while(guess.isalpha()!=True or len(guess)!=5):
        a=input("Enter the Guessed word again: ")
        guess=a.lower()
       
    if(guess==select):
        print("Congratulations!! You have won this challenge")
        s=1
        break
    else:
        index=0
        for x in guess:                
            if x in select:
                if(x==select[index]):
                    if x in misplace:
                        misplace.remove(x)
                    if x not in correct:
                        correct.append(x)                        
                else:
                    if x not in misplace:
                        misplace.append(x)                
            else:
                if x not in incorrect:
                    incorrect.append(x)
            index=index+1
        print("Correct Letter(s): ",correct)
        print("Misplaced Letter(s): ",misplace)
        print("Incorrect Letter(s): ",incorrect)
        rem_turns=max_turns-cur_turns
        print("Remaining Turns: ",rem_turns) 
        cur_turns=cur_turns+1
    print("--------------")
if(s==0):
    print("Sorry. Your turns are over.")
    print("Better Luck Next Time!!")
    print("The Guessed Word Is: ",select)


    
