score=0
print("Question 1:What is the capital of France?")
answer1=input("a)Paries\nb)Rose\nc)Marid\nYour answer:")
if answer1=='a':
    score+=1

print("Questions 1: which fruit has the highest oil contant?")
answer2=input("a) avacado\nb) tomato\nc) pumpkin\nYour answer:")
if answer2=='a':
    score+=1

print("where was the kiwi fruit first grown?")
answer3=input("a)china\nb rome\nc) america\nYour answer:")
if answer3=='a':
    score+=1


print("\nQuiz completed")
print("You got score out of 3 questions correct.",score)