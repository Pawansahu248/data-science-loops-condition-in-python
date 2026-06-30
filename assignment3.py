#Q..........................1
#without built in function
number=[1,2,3,4,5,6,7,8,9,11]
for num in number:
    cout=0
    for i in range(1,num+1):
        if num%i==0:
            cout+=1
    if cout==2:
        print(num)  
        
#Q.....................2
for i in range(1,11):
    for j in range(1,11):
     print(i*j,end="\t")
    print()
    
#Q........................3
def check_num(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=i
    return even,odd
print(check_num([1,2,3,5,7,8,9]))
#Q.................4

# Function with default arguments
def simple_interest(principal, rate=5, time=1):
    si = (principal * rate * time) / 100
    return si

# Using positional arguments
print("Simple Interest =", simple_interest(1000))

# Using positional arguments with all values
print("Simple Interest =", simple_interest(1000, 8, 2))

# Using keyword arguments
print("Simple Interest =", simple_interest(principal=1000, rate=10, time=3))

# Using mixed arguments
print("Simple Interest =", simple_interest(2000, time=2))

#Q.......................5
class student:
    name="pawan"
    marks=int(input("enter marks"))
    if marks>=90:
        print("grade A")
    elif marks>=80:
        print('grad B')
    elif marks>=70:
        print('grad C')
    else:
        print('fail')
    
print(student.name)
print(student.marks)
#Q...................6
# with help of function..................
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def grade(self):
        if self.marks>=90:
            return 'A'
        elif self.marks>=80:
            return 'B'
        elif self.marks>=70:
            return 'c'
        else:
            return 'fail'
        
s1=student("pawan",55)
s2=student("rahul",99)
print(s1.name,"grade",s1.grade())
print(s1.marks,s2.marks)
print(s2.name,"grade",s2.grade())

#Q............................7
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # Private attribute

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Current Balance:", self.__balance)


# Create object
account = BankAccount(5000)

# Deposit money
account.deposit(2000)

# Withdraw money
account.withdraw(1500)

# Display balance
account.show_balance()

# Direct access not allowed
# print(account.__balance)   # Error

#Q.......................8
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2
    print("Result =", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Invalid input. Please enter numbers only.")

#Q.....................9
file=open("student.txt","w")
file.write("name:pawan\n")
file.write("marks:88")
file.close()

file=open("student.txt","r")
data=file.read()
print(data)
file.close()

#Q......................10
try:
    file=open("numbers.txt","r")
    numbers=file.read().split()
    print(numbers)
    total=0
    count=0
    for num in numbers:
        total+=int(num)
        count+=1 
        avg=total/count
        print(total)
        print(avg)  

        file.close()
except FileNotFoundError:
    print("file does not exist:")