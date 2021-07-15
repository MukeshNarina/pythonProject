Dictionary = {
    'A': 'Hello',
    'B': 'World',
    'C': 'Buddy',
    'D': 'Welcome'
}


Input = input()

if Input == "A and B":
   print((Dictionary.get('A')) + (Dictionary.get('B')))
elif Input == "A and C":
   print((Dictionary.get('A')) + (Dictionary.get('C')))
elif Input == "D or B":
   print((Dictionary.get('B')))
elif Input == "A or B":
    print(Dictionary.get('A'))
elif Input == "A and B and C":
    print((Dictionary.get('A')) + (Dictionary.get('B')) + (Dictionary.get('C')))
elif Input == "A and (B or C)":
    print((Dictionary.get('A')) + (Dictionary.get('B')))
elif Input == "A and (C or D)":
    print((Dictionary.get('A')) + (Dictionary.get('c')))
elif Input == "A and (B or C) and D":
    print((Dictionary.get('A')) + (Dictionary.get('B')) + (Dictionary.get('D')))