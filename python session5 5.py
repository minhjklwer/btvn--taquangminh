while True:
    string =input("What's the string")

    def remove_dollar_sign(s):
         removed = s.replace("$","")
         print(removed)
         return removed
        
    remove_dollar_sign(string)
     
