import random
import pyinputplus as pypi
while True:
    min = 1
    max = 100
    count = 0
    target = random.randint(1,100)
    print(target)
    print("=================猜數字===================\n")
    while True:
        count += 1
        keyin = pypi.inputInt(f"猜數字範圍{min}到{max}:",min=min,max=max)
        if keyin == target:
            print(f"猜中了答案是{keyin}")
            print(f"猜了{count}次")
            break
        elif keyin > target:
            print("小一點")
            max = keyin-1
        elif keyin < target:
            print("大一點")
            min = keyin+1
        print(f"你猜了第{count}次")
    is_play = pypi.inputYesNo("還要繼續嗎?(yes/no)")
    if is_play == "no":
        break
print("程式結束")
