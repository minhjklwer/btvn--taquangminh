def get_even_list(n):
    for e in n:
     if e % 2 !=0:
          n.remove(e)
    print(n)
    
    return(n)
get_even_list([1,2,3,4,5,6,7,8])

even_list = get_even_list([1, 2, 5, -10, 9, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
