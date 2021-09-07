number_1 = 0
number_2 = 1
result = 1
for number_1 in range(1,10,1) :
  for number_2 in range(1,10,1) :
    result = number_1 * number_2
    print(number_1, "*", number_2, "=", result)