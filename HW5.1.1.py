def computation_raiting(md):
   return md
while True:
  print("Введитее жанр для которого вы хотите узнать средний рейтинг\nмне известны лишь :\nфантастика\nдрама\nфэнтази\nкриминал")
  md = str(input())
  computation_raiting = [ratings[k] for k in shows if shows[k] == md]
  computation_raiting = sum(computation_raiting)/len(computation_raiting)
  print("для жанра", md, "средний рейтинг состовляет", computation_raiting)
  continue
def genre_series(genre):
   return genre
while True:
 print("Введитее жанр для которого вы хотите узнать рекомендуемые сериалы\nмне известны лишь :\nфантастика\nдрама\nфэнтази\nкриминал")
 result = []
 genre = str(input())
 for key, value in shows.items():
  if genre in value:
   result.append(key)
   print(result)
  continue
