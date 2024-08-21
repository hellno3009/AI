class Myclass:
    @classmethod
    def get_status_message(cls,bmi: float) -> str:
        '''
        #param bmi:傳入bmi值
        #return:傳出bmi的狀態
        '''
        if bmi < 18.5:
            return "體重過輕"
        elif bmi < 24:
            return "正常範圍"
        elif bmi < 27:
            return "過重"
        elif bmi < 30:
            return "輕度肥胖"
        elif bmi < 35:
            return "中度肥胖"
        else:
            return "重度肥胖"
        

while True:
    try:
        name = input("請輸入姓名: ")
        height = float(input('請輸入身高（cm）: '))
        weight = float(input('請輸入體重（kg）: '))
        bmi = weight / ((height * 0.01) ** 2)
        grade = Myclass.get_status_message(bmi)
        print(f"{name} 的 BMI 為 {bmi:.2f}, 為 {grade}")

    except ValueError:
        print("格式錯誤")
        continue

    stuff = input("是否繼續輸入資料?(q: 離開,其他鍵:繼續)")

    if stuff == 'q':
        break

print("程式結束")