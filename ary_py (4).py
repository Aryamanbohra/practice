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
if year%400==0 and year%100==0:
    print("year is leap")
elif year%4==0 and year%100!=0:
    print("year is leap")
else:
    print("it is no leap year")
    

#question4
num1=int(input("enter a number:"))
num2=int(input("enter a number:"))
num3=int(input("enter a number:"))
num4=int(input("enter a number :"))
if num1==num2 and num1+num2==num3 and num1 +num2+ num3 ==num4:
    print("yes it is fibonacci")
else:
    print("no fibonacci")

#question5
num1=int(input("enter a number :"))
num2=int(input("enter a number :"))
if num1==num2:
    print(num1,"equals",num2)
else:
    print (num1 ,"not equals",num2)

#question6
radius=int(input("enter radius :"))
if radius>0 :
    circum=2*3.14*radius
    area=3.14*radius*radius
    print("circum=",circum)
    print("area=" ,area)

#question7
num1=int(input("enter a number :"))
num2=int(input("enter a number :"))
if num1>num2:
    print("num1 is largest")
else :
    print ("num2 is largest")
    

#question8
num=int(input("enter a number :"))
if num%5==0 and num%10 ==0:
    print("yes it is divisible by both")
elif num%5==0 and num%10!=0:
    print("only divisible by 5 ")

else:
    print("number not divisible by both")
    
#question10
n1=int(input("enter a number:"))
n2=int(input("enter a number :"))
n3=int(input("enter a number"))
if n1>=n2 and n1>=n3 :
    greater = n1
elif n2>=n1 and n2>=n3 :
    greater = n2
else :
    greater =n3
print ("greater number is"  ,greater)



#question11
sub1=int(input("enter a marks :"))
sub2=int (input("enter a marks :"))
sub3=int(input("enter a marks :"))
sub4=int(input("enter a marks :"))
sub5=int(input("enter a marks :"))
totalmarks=sub1+sub2+sub3+sub4+sub5
per=totalmarks/5
print(" subject marks :" ,totalmarks )
print(" percentage :" ,per)

if per >=90:
    print("distinction")
elif per>=80 and per <90 :
    print(" first class")
elif per>=70 and per < 80:
    print(" second class")
elif per >=60 and per <70:
    print(" third class")
else:
    print("fail")






