def get_even_list(n):
    for e in n:
     if e % 2 !=0:
          n.remove(e)
    print(n)
    
    return(n)
get_even_list([1,2,3,4,5,6,7,8])


    
