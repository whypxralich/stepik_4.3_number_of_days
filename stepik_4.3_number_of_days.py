days = int(input())

if days == 2:
    print (28)
elif days <= 7:          
    print(30 + days%2 )
elif days > 7:
    print(31 - days%2 )