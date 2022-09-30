# Write a python script to take the month value in numeric format and display the number of days in it.
a=int(input("Enter a month in numeric format: "))
if a==2:
    print("number of days is 28")
elif a>12:
    print("You enterd wrong month number...not month")
elif a==8:
    print("number of days is 31")
elif a==9:
    print("Number of days is 30")
elif a==10:
    print("number of days is 31")    
elif a==11:
    print("number of days is 30")
elif a==12:
    print("number of day is 31")
elif a%2==0:
    print("number of days is 30")
elif a%2!=0:
    print("number of days is 31")
       
