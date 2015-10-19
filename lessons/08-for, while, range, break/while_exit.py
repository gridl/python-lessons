text = ""
while text != "стоп":
    text = input("Введите число или стоп для выода: ")
    if text == "стоп":
        print("Выход из программы! До встречи!")
    elif text == '1':
        print("Число 1")
    else:
        print("Что это?!")
