def initial(s):
    l=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    if s[0] in l:
            print(s[0],end=".")
    for i in range(len(s)):
        
        if s[i] == " " and s[i+1] in l:
            print (s[i+1],end=".")

s="Iman KALYAN Dutta"
initial(s)
