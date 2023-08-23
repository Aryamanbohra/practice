num=int(input("enter your number"))
if num%2==0:
    print("num is even")
else:
    print("num is odd")

#question2 
num1=int(input("enter a number :" ))
num2=int(input("enter a number :"))
num3=int(input("enter a number :"))
if num1>num2 and num1>num3:
    print("num1 is largest")
elif num2>num1 and num2>num3:
    print("num2 is largest")
else:
    print("num3 is largest")

#question3
year=int(input("enter a year:"))
if year%4==0:
    print("leap year")
else :
    print("no leap year")
    

#question4
num1=int(input("enter a number:"))
num2=int(input("enter a number:"))
num3=int(input("enter a number:"))
num4=int(input("enter a number :"))
if num1==num2 and num1+num2+num3==num4 :
    print("yes it is fibonacci")
else:
    print("no fibonacci")

#question5
num1=int(input("enter a number :"))
num2=int(input("enter a number :"))
if num1==num2:
    print("true")
else:
    print("false")

#question6
radius=int(input("enter radius :"))
if radius>0 :
    circum=2*3.14*radius
    area=3.14*radius*radius
    print("true")
    print("circum,area")

#question7
num1=int(input("enter a number :"))
num2=int(input("enter a number :"))
if num1>num2:
    print("num1 is largest")
elif num2>num1 :
    print(" num2 is largest")
else :
    print ("no one")
    

#question8
num=int(input("enter a number :"))
if num%5==0 or num%10 ==0:
    print("yes it is divisible")
elif num%5==0 or num%10==0:
    print("only one ")
else:
    print("no")
    
#question10
n1=int(input("enter a number:"))
n2=int(input("enter a number :"))
n3=int(input("enter a number"))
if n1>n2 and n1>n3:
    print("n1 is bigger")
elif n1<n2 and n1<n3:
    print("n1 is smaller")
elif n1>n2 or n1>n3:
    if n1>n2:
        print("n1 is greater than n2 only")
    else:
        print("n1 is greater than n3 only")
elif n1<n2 or n1<n3:
    if n1<n2:
        print("n1 is smaller than n2 only")
    else:
        print("n1 is smaller than n3 only")

#question11
subject marks =456
per=subject marks/5
print(" subject marks :" ,subject marks )
print(" percentage :" ,per)

if per >=90:
    print(" distinction")
elif per>=80 and per <90 :
    print(" first class")
elif per>=70 and per < 80:
    print(" second class")
elif per >=60 and per <70:
    print(" third class")
elif per< 60:
    print("fail")






