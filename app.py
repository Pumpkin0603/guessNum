import random

answerNum = random.randint(1, 100)
for i in range(1, 8):
    guess = input(f"請在7次內猜出數字({i})：")
    if guess == "" or not guess.isdigit():
        break
    elif int(guess) == answerNum:
        print("讚！答對了^_^ ")
        quit()
    elif int(guess) > answerNum:
        print("> 猜低些試試")
    elif int(guess) < answerNum:
        print("> 猜高些試試")
print("\n正確答案是：" + str(answerNum))
input()
