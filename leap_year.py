def Leapyear(year):  
  if((year % 400 == 0) or  
     (year % 100 != 0) and  
     (year % 4 == 0)):   
    print (f"the year {year} is a leap Year")  
  else:  
    print (f"the year {year} is not a leap Year")  
year = int(input("Enter the year: "))    
Leapyear(year)  