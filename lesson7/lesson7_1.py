print("輸入q離開")
while True:
    try:
        name_input = input("請輸入姓名:")
        if name_input.lower() == 'q':
            break
        name = str(name_input)
        
        height_input = input("請輸入身高(cm):")
        if height_input.lower() == 'q':
            break
        height = float(height_input)
        
        weight_input = input("請輸入體重(kg):")
        if weight_input.lower() == 'q':
            break
        weight = float(weight_input)
        
        bmi = weight / (height * 0.01) ** 2
        if bmi < 18.5:
            grade = "體重過輕"
        elif bmi < 24:
            grade = "正常範圍"
        elif bmi < 27:
            grade = "過重"
        elif bmi < 30:
            grade = "輕度肥胖"
        elif bmi < 35:
            grade = "中度肥胖"
        else:
            grade = "重度肥胖"
        print(f"{name} 的 BMI 為 {bmi:.2f}, 屬於 {grade}")
    except ValueError:
        print("格式錯誤，請輸入正確的數字。")
print("應用結束")