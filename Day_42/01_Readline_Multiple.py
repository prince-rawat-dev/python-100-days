# Starting (Day 42)Lecture - 50(read(), readlines() and other methods)

# Basic File Write, it covers[open(),w,write(),text mode,with,newline,encoding]


# first we make a txt file and store data their:-

# lines = ["Java\n","Python\n","C++\n"]

# with open("data.txt","w",encoding = "utf-8")as file:
#     file.writelines(lines)
#     print("data stored")


# Main Program :-
# Program 1 — readline() Multiple Times
# Its about file pointer / reading position:-
with open("data.txt","r",encoding = "utf-8")as file:
    line1 = file.readline()
    line2 = file.readline()
    line3 = file.readline()

print("Line1:", line1.strip())
print("Line2:", line2.strip())
print("Line3:", line3.strip())


# Practice (Day 42)Lecture 50(read(), readlines() and other methods):-

# using readline() using loop(to print all lines from the file):-
# f = open('myfile.txt', 'r')
# i = 0
# while True:
#   i = i + 1
#   line = f.readline()
#   if not line:
#     break
#   m1 = int(line.split(",")[0])
#   m2 = int(line.split(",")[1])
#   m3 = int(line.split(",")[2])
#   print(f"Marks of student {i} in Maths is: {m1*2}")
#   print(f"Marks of student {i} in English is: {m2*2}")
#   print(f"Marks of student {i} in SST is: {m3*2}")

#   print(line)



# using writelines:-
# f = open('myfile2.txt', 'w')
# lines = ['line 1\n', 'line 2\n', 'line 3\n']
# f.writelines(lines)
# f.close()



# using read() :-
# with open("myfile2.txt", "r")as f:
#   data = f.read()
# print(data)


# using writelines:-
# with open("myfile2.txt", "w")as f:
#   line =['line 1\n', 'line 2\n', 'line 3\n']
#   f.writelines(line)



# using readline() (to print only single line):-
# f = open("myfile2.txt","r")
# data = f.readline()
# f.close()
# print(data)



# using readlines() (it prints all lines in an iterable form like list/tuple):-
# f = open("myfile2.txt","r")
# value = f.readlines()
# f.close()
# print(f"these are the lines:- {value}")


# using write() +  (newline) (to print lines(from file) seperately from each other):-
# f = open('myfile.txt', 'w')
# lines = ['line 1', 'line 2', 'line 3']
# for line in lines:
#     f.write(line + '\n')
# f.close()

# using readlines() (read the text using index and assign it to variables and then reading all lines):-
# with open("myfile2.txt", "r")as f:
#   line = f.readlines()
  
#   m1 = line[0]
#   m2 = line[1]
#   m3 = line[2]
  
#   print(f"the 1st line is: {m1}")
#   print(f"2nd line is: {m2}")
#   print(f"3rd one is: {m3}")
#   print(line)

