# Ошибка при открытии файла
try:
    f = open ('1example_text.txt')
except:
    print ("Error opening file")
finally:
    f.close()
    print ('(Очистка: Закрытие файла)')
