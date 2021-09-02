import random
balanse = 10000
s = 1000
j = []
print("Здравствуйте вы попали в виртуальное казино с прекрасным названием HW2.0")
print(
    "Ваш стартовый дипозит 10000 рублей \nПравила такие играем в угадай число ставка 1000 руб0лей\nКрупье бросает кости максимум может выпасть 12 минимум 2 при совпадении + 1000 не угадал ставка сгорает\nНадеюсь все понятно")
while True:
    number = ("Загадывай число")
    print(number)
    try:
      number = int(input())
      if 2 < number > 12 :
        continue
    except:
        continue
    randomnumb = random.randint(2, 12)
    print("Вы загадали цифру", number)
    print("Число которое выпало у крупье равно", randomnumb)
    if randomnumb == int(number):
        print("Вы выиграли на ваш баланс зачисленно 1000\nВаш баланс сейчас\nПовторите Ваш успех!")
        balanse = (balanse + s)
        print(balanse)
        j.append("Я загадал " + str(number))
        j.append("Игра загадала " + str(randomnumb))
        j.append("Мой баланс после ставки " + str(balanse))
    else:
        print("Вы не угадали число, ставка сгорела\nПопробуйте снова! я уверен Вам повезет\nВаш баланс сейчас")
        balanse = (balanse - s)
        print(balanse)
        j.append("Я загадал " + str(number))
        j.append("Игра загадала " + str(randomnumb))
        j.append("Мой баланс после ставки " + str(balanse))
        if balanse <= 0:
            print("Игра окончена ваш баланс равен 0")
            break

