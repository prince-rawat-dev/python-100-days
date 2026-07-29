# Bonus program(combines functions+loops+conditions)
def even_odd_count(*args):
 odd_count = 0
 even_count = 0
 for i in args:
        if(i % 2 == 0):
            even_count += 1
        else:
            odd_count += 1
 print("Their are",odd_count,"odd numbers")
 print("Their are",even_count,"even numbers")

even_odd_count(1)
# even_odd_count(1,2,3,4,5,6)
even_odd_count(1,34, 65,676)
even_odd_count(0)

