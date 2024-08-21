import widght#或是用from widght import tools直接抓檔案
while True:
    try:
        name = input("請輸入姓名: ")
        height = float(input('請輸入身高（cm）: '))
        weight = float(input('請輸入體重（kg）: '))
        bmi = weight / ((height * 0.01) ** 2)
        grade = widght.tools.get_status_message(bmi)
        print(f"{name} 的 BMI 為 {bmi:.2f}, 為 {grade}")

    except ValueError:
        print("格式錯誤")
        continue

    stuff = input("是否繼續輸入資料?(q: 離開,其他鍵:繼續)")

    if stuff == 'q':
        break

print("程式結束")