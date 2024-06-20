file = open('text.txt', 'a')
file.write("Вас приветствует команда Компьютерной Академии ШАГ! Дневник студента доступен по ссылке https://mystat.itstep.kz Учетные данные к аккаунту Копеев Арман: LOGIN:Kopee_ek46 PASSWORD: u#4D*cW")
file.close()

print("sdadasdsadsaddas", file=test)
test.close()


with open('text.txt','r', endcoding='utf-8') as file:
    info = file.()
    print(info)