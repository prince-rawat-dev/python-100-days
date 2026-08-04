lst = []
for i in range(5):
    lst.append(int(input(f"Enter marks for subject {i+1}: ")))
print(f"\n Your marks list: {lst}")

def total_marks():
    '''\ntotal_marks() = Generate total marks'''
    print(total_marks.__doc__)

    total = 0
    for i in lst:
        total += i
    return total

def average_marks(totl):
    '''average_marks(totl) = Generate average'''
    print(average_marks.__doc__)

    average = totl/5
    return average

submation = total_marks()
avg = average_marks(submation)
print(f"\nTotal marks: {submation}\nAverage: {avg}\n")