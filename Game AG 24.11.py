
import random
def get_quest():
    #open file with questions
   questions = open("game.txt","r",encoding=("utf-8"))
   #read question list
   question_list = questions.read().splitlines()
   #choose a random question
   questnum = random.randrange (0,len(question_list))
   questline = str (question_list[questnum])
   #searching for ";" in line
   for i in range(0,len(questline)):
       if questline[i]==";":
           question = questline[0:i]
           answer = questline[i+1:len(questline)]
           return answer, question
counter=0
while True:
    initCheck="exit"
    print("The game starts now!Type '",initCheck,"' to exit the game! Enter anything else to continue.")  
    init=input()
    if init==initCheck:
        print("You answered ",counter," questions!")
        break
    answer, question = get_quest()
    print(question)
    print(answer)
    #hiding the answer, but not the whitespace
    view=[]
    check=""
    for i in range (0,len(answer)):
        if answer[i]==" ":
            view.append(" ")
        else:
            view.append("*")
    print("".join(view))
    #giving a 3 tries to guess a character or answer
    k=3
    while k>0:
        ans = input("Enter character or answer")
        if ans.lower() == answer.lower():
            counter=counter+1
            print("Bingo!Загаданное слово было {answer}");
            break
        elif (ans.lower() in answer.lower()):
            print("Right character!")
            for i in range(0,len(answer)):
                if answer[i].lower()==ans.lower():
                    if answer[i].isupper():
                        view[i]=ans.upper()
                        check="".join(view)
                    else:
                        view[i]=ans.lower()
                        check="".join(view)
        else:
            print("There is no such character! You have ",k-1," tries left.")
            k=k-1
        if check.lower()==answer.lower():
            counter=counter+1
            print(f"You guessed all characters! Загаданное слово {answer}");break
        print(check)
       # print(answer)
        if k==0:
            print(f"Game Over! You answered {counter} questions. Загаданное слово было {answer}")
            counter=0