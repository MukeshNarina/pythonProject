amount = int(input())

one_million = 0
one_lakh = 0
one_thousand = 0
one_hundred = 0
ten = 0
one = 0

#Billion
if (amount/1000000) == 1000:
    print("one billion")

#Million Count
if amount >= 1000000:
    one_million = (amount/1000000)
    amount = (amount%1000000) 
    
    million = int(one_million)
    length = len(str(million))
    
    if (length ==  1):
        if million == 1:
           print("one million")
        elif million == 2:
           print("Two million")
        elif million == 3:
           print("Three million")
        elif million == 4:
           print("Four million")
        elif million == 5:
           print("Five million")
        elif million == 6:
           print("Six million")
        elif million == 7:
           print("Seven million")
        elif million == 8:
           print("Eight million")
        elif million == 9:
           print("Nine million") 
            
        
    
#Lakhs Count   
if amount >= 100000:
    one_lakh = (amount/100000)
    amount = (amount%100000)
    if int(one_lakh) == 1:
        print("one lakh")
    elif int(one_lakh) == 2:
        print("Two lakh")
    elif int(one_lakh) == 3:
        print("Three lakh")
    elif int(one_lakh) == 4:
        print("Four lakh")
    elif int(one_lakh) == 5:
        print("Five lakh")
    elif int(one_lakh) == 6:
        print("Six lakh")
    elif int(one_lakh) == 7:
        print("Seven lakh")
    elif int(one_lakh) == 8:
        print("Eight lakh")
    elif int(one_lakh) == 9:
        print("Nine lakh") 
    

#Thousands Count    
if amount >= 1000:
    one_thousand = (amount/1000)
    amount = (amount%1000)
    
    Thousand  = int(one_thousand)
    output = str(Thousand)

    if int(output[0]) == 2:
        print("Twenty")
    elif int(output[0]) == 3:
        print("Thirty")  
    elif int(output[0]) == 4:
        print("fourty") 
    elif int(output[0]) == 5:
        print("Fifty")    
    elif int(output[0]) == 6:
        print("Sixty")    
    elif int(output[0]) == 7:
        print("Seventy")   
    elif int(output[0]) == 8:
        print("Eighty")  
    elif int(output[0]) == 9:
        print("Ninety") 
        
    if int(output[1]) == 1:
        print("one thousand")
    elif int(output[1]) == 2:
        print("Two thousand")
    elif int(output[1]) == 3:
        print("Three thousand")
    elif int(output[1]) == 4:
        print("Four thousand")
    elif int(output[1]) == 5:
        print("Five thousand")
    elif int(output[1]) == 6:
        print("Six thousand")
    elif int(output[1]) == 7:
        print("Seven thousand")
    elif int(output[1]) == 8:
        print("Eight thousand")
    elif int(output[1]) == 9:
        print("Nine thousand") 
  
#Hundreds Count
if amount >= 100:
    one_hundred = (amount/100)
    amount = (amount%100)
    
    if int(one_hundred) == 1:
        print("one hundred")
    elif int(one_hundred) == 2:
        print("Two hundred")
    elif int(one_hundred) == 3:
        print("Three hundred")
    elif int(one_hundred) == 4:
        print("Four hundred")
    elif int(one_hundred) == 5:
        print("Five hundred")
    elif int(one_hundred) == 6:
        print("six hundred")
    elif int(one_hundred) == 7:
        print("Seven hundred")
    elif int(one_hundred) == 8:
        print("Eight hundred")
    elif int(one_hundred) == 9:
        print("Nine hundred")
#Tens Count     
if amount >= 10:
    ten = (amount/10)
    amount = (amount%10)
    
    if int(ten) == 1:
        print("ten")
    elif int(ten) == 2:
        print("Twenty")
    elif int(ten) == 3:
        print("Thirty")  
    elif int(ten) == 4:
        print("fourty") 
    elif int(ten) == 5:
        print("Fifty")    
    elif int(ten) == 6:
        print("Sixty")    
    elif int(ten) == 7:
        print("Seventy")   
    elif int(ten) == 8:
        print("Eighty")  
    elif int(ten) == 9:
        print("Ninety") 


#Ones Count     
if amount >= 1:
    one = (amount/1)
    amount = (amount%1)
    if int(one) == 1:
        print("one dollars")
    elif int(one) == 2:
        print("Two dollars")
    elif int(one) == 3:
        print("Three dollars")
    elif int(one) == 4:
        print("Four dollars")
    elif int(one) == 5:
        print("Five dollars")
    elif int(one) == 6:
        print("Six dollars")
    elif int(one) == 7:
        print("Seven dollars")
    elif int(one) == 8:
        print("Eight dollars")
    elif int(one) == 9:
        print("Nine dollars")