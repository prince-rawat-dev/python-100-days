# Here taking no.'s from user inside a list and the using single function - count even and odd no.'s in that list


lst = []
for i in range(5):
    lst.append(int(input(f"Enter marks for subject {i+1}: ")))

print(f"\nNumbers List: {lst}\n")


def even_odd_count():
 '''even_odd_count() = Counts both even and odd no.'s in a list\n'''
 print(even_odd_count.__doc__)
 
 even_count = 0
 odd_count = 0

 for i in lst:
     if(i%2 == 0):
        even_count += 1
     else:
        odd_count += 1

 return even_count, odd_count

even, odd = even_odd_count()
print(f"Even and odd count of this list: {even, odd}\n")