print("Hello welcome to MANY QUIZ")

ans = input("Are your ready to start? (Y/N): ")
score = 0
totalques = 10

if ans.lower() == "yes":
    ans = input("1. What is the most popular Programming language in the world?: ")
    if ans.lower() == "python":
        score+= 1 
        print("Yes! the correct answer is python")
    else:
        print("Its not" +ans)    

ans = input("2.What does Roblox studio use for its programming languages?:  ")
if ans.lower() == "lua":
    score+=1
    print("Yes! the programming language that Roblox studio use is lua")
else:
    print("No its not" +ans)


ans = input("3. What is 10 x 10?: ")
if ans.lower() == "100":
    score+=1
    print("Yes! the answer is 100")
else:
    print("No its not" +ans)   


ans = input("4. What 7x7?: ")
if ans.lower() == "49":
    score+=1
    print("Yes! the answer is 49")
else:
    print("Not its not" +ans)


ans = input("5. What is the square root of 49?: ")
if ans.lower() == "7":
    score+=1
    print("Yes! the answer is 7")
else:
    print("Not its not" +ans) 


ans = input("6. What is Hippopotomonstrosesquippedaliophobia?: ")
if ans.lower() == "fear of long words":
    score+=1
    print("Yes! the answer is Fear of long words!")
else:
    print("No its not" +ans)

ans = input("7. Help me: ")
if ans.lower() == "no":
    score+=1
    print("Yes! the answer is no!")
else:
    print("No its not" +ans)

ans = input("8.What is 8x8?: ")
if ans.lower() == "64":
    score+=1
    print("Yes! the answer is 64!")
else:
    print("Not its not" +ans)


ans = input("9.What is 9x9?: ")
if ans.lower() == "81":
    score+=1
    print("Yes! the answer is 81!")
else:
    print("Not its not" +ans)


ans = input("9.Lastly what is the meaning of life? ")
if ans.lower() == "uhhh":
    score+=1
    print("Yes! the answer is uhhh")
else:
    print("Not its not" +ans)


print("Thanks for playing!, your total right answers were: ", score)
mark = (score / totalques) * 100 
print("Marks: ", mark,"% ")

if mark > 80:
    print("Great job your reward is nothing!")
elif mark > 60 and mark <= 80:
    print("You did well but try better")
else:
    print("Im sorry but you have to try again")
