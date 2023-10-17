workers = 5
workers_all = [
    ['Иван', '1/10/1995', '25000'],
    ['Геннадий', '2/11/1993', '25000'],
    ['Антон', '3/12/1999', '25000'],
    ['Владимир', '4/1/2000', '25000'],
    ['Алексей', '5/6/1997', '25000']
]

# workers_all = []
# for x in range(0, workers):
#   Name = input("Введите своё имя: ")
#   BrthDay = input("Введите свой день рождения (День/Месяц/Год): ")
#   ZarPlt = input("Введите свою заработную плату: "); print("")

#   worker = [Name, BrthDay, ZarPlt]
#   workers_all.append(worker)

months = ["Января", "Февраля", "Марта", "Апреля",
          "Мая", "Июня", "Июля", "Августа",
          "Сентября", "Октября", "Ноября", "Декабря"]

dir_month = input("Введите месяц: "); print("")
count = 0

for y in range(0, workers):
    count += 1
    if(workers_all[y][1].split("/")[1] == dir_month):
      workers_all[y][2] = round(int(workers_all[y][2]) + (int(workers_all[y][2]) / 100) * 25)
      print("Сотрудник "+"№"+str(count)+": ",
            "\n   Имя: "+str(workers_all[y][0]),
            "\n   Дата рождения: "+str(int(workers_all[y][1].split("/")[0]))+" "+str(months[int(workers_all[y][1].split("/")[1])-1]+" "+str(int(workers_all[y][1].split("/")[2]))+"г."),
            "\n   Зарплата + премия 25%: "+str(workers_all[y][2])+"\n")
    else:
      print("Сотрудник "+"№"+str(count)+": ",
            "\n   Имя: "+str(workers_all[y][0]),
            "\n   Дата рождения: "+str(int(workers_all[y][1].split("/")[0]))+" "+str(months[int(workers_all[y][1].split("/")[1])-1]+" "+str(int(workers_all[y][1].split("/")[2]))+"г."),
            "\n   Зарплата: "+str(workers_all[y][2])+"\n")


