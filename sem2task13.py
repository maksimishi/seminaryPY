import random

today = 0
days = []
counter = 0
max_counter = 0

for i in range(1, 30):
  today += random.randint(-3,3)
  days.append(today)

  if today > 0:
    counter += 1
    if counter > max_counter:
      max_counter = counter
  else: counter = 0

print(days)
print(max_counter)