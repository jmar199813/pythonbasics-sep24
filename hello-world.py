#simple
print("Hello, World! 1")

#Using a variable
message = "Hello, World! 2"
print(message)

#string concatenation
print("Hello, " + "World" + "!" + " 3")

#f string
name = "World"
print(f"Hello, {name}! 4")

#format 
name1 = "Hello"
name2 = "World"
formatted_string = "{}, {}! 5".format(name1, name2)
print(formatted_string)

#loop
for phrase in ["Hello, World! 6"]:
  print(phrase)

#loop2
slogans = ["Hello", "World", "!", "#7"]
for slogan in slogans:
  print(slogan)

#range loop
for i in range(4):
  print(i)

#while loop
count = 0
while count < 5:
  print(count)
  count += 1

#skips over the number 2
for i in range(7):
  if i == 2:
    continue
  print(i)  

#nested loops  
for i in range(3):
  for j in range(2):
    print(f"i: {i}, j: {j}")

#nested loop string example
colours = ["red", "green", "blue"]
numbers = ["1", "2", "3"]

for colour in colours:
  for number in numbers:
    print(f"{colour} {number}")

#nested loop pattern
for i in range(7): # rows
  for j in range(i + 1): # columns
    print("*", end="")
  print() # moves to a new line after each row

#nested loop patter backwards
rows = 7

for i in range(rows, 0, -1):
  for j in range(i):
    print("*", end="")
  print()

#time for a new Hello, Woorld so I can remeber how I got here
print("Hello, World!")
print("Hello, World!")
print("Hello, World!")
  