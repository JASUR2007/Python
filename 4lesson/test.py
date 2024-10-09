question_1 = int(input('How many regions in Uzb? '))
question_2 = input('The capital of Russia: ')
question_3 = int(input('how many presidents have there been in the USA? '))
question_4 = int(input('what is 20*5?'))
question_5 = int(input('what is 20*5?'))

nums = 0
if question_1 == 12:
    nums += 1
if question_2 == "Moscow":
    nums += 1
if question_3 == 46:
    nums += 1
if question_4 == 100:
    nums += 1
if question_5 == 100:
    nums += 1

if nums == 5:
    print('you won a prize')
elif nums == 4:
    print("you did a great job")
elif nums == 3:
    print("Almost got it")
elif nums == 2:
    print("OoPs")
elif nums == 1:
    print("ok")    
else:
    print("Next Time")