#6
a=int(input("Enter the principle amount: "))
b=float(input("Enter the time period in years: "))
c=float(input("Enter the rate in percentage: "))
i = a*b*c*0.01
print("The simple intrest is : ",i)

#7.
a=float(input("\n\n\nEnter the number: "))
if a > 0:
    print("This is an positive number ")
elif a == 0:
    print("Zero")
else:
    print("This is a negative number")

#8.
a=float(input("\n\n\nEnter the numerator : "))
b=float(input("Enter the denominator : "))
c = a%b
print("The remainder is ",c)

#9.
a=float(input("\n\n\n9.Enter the value of a "))
b=float(input("ENter the value of b "))
a=a+b
b=a-b
a=a-b
print(f"The value of new a is {a} and new b is {b}") 

#10
a=int(input("\n\n\nEnter the number : "))
if a//2 ==0 :
      print("The numer is even")
else :
    print("The number is odd")
