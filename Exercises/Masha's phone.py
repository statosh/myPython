price = int(input("Цена телефона: "))
nakop_day = int(input("Машины карманные деньги на день: ")); print("")
cur_day = 0
day_sum = 0

for nakop in range(price):
  while nakop < price:
    cur_day += 1
    day_sum += 1
    if 0 <= cur_day <= 6:
      nakop += nakop_day
      print("День: "+str(day_sum)+". Накопления Маши: "+str(nakop)+" руб.")
    elif cur_day == 7:
      cur_day = 0
      print("День: "+str(day_sum)+". Накопления Маши: Не изменились, т.к. она пошла в кино.\n")
  print("\nМаша накопила на телефон! Это заняло у неё "+str(day_sum)+" дней.")
  break
