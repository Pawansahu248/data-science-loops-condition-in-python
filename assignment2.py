#Q.............1
temp=int(input("enter first number"))
larg_number=temp
sec_larg=temp
smallest_number=temp
for i in range(9):
    num=int(input("enter number "))
    
    if num>larg_number:
        sec_larg=larg_number
        larg_number=num
    elif num>sec_larg and num!=larg_number:
        sec_larg=num
    if num<smallest_number:
        smallest_number=num
        
print(larg_number)
print(sec_larg)
print(smallest_number)

#q..................2
s=input("enter your string: ")
vowel=consonent=digit=special=0

for ch in s:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowel+=1
        else:
            consonent+=1
    elif ch.isdigit():
        digit+=1
    elif not ch.isspace():
        special+=1
        
print(vowel)
print(consonent)
print(digit)
print(special)
        
#Q.................3
n = int(input())
s = sum(int(i) ** len(str(n)) for i in str(n))
print("Armstrong" if s == n else "Not Armstrong")

#Q.................4
t = (1, 2, 3, 2, 4, 1, 1)
for i in set(t):
    if t.count(i) > 1:
        print(i, ":", t.count(i))
        
#Q...................5
students = (("Pawan", 85), ("Karan", 92), ("JP", 88))
topper = max(students, key=lambda x: x[1])
print("Topper:", topper[0], topper[1])

#Q....................6
s = input().split()
d = {}
for word in s:
    d[word] = d.get(word, 0) + 1
print(d)

#Q..................7
marks = {"Pawan": 80, "Karan": 90, "JP": 70}
avg = sum(marks.values()) / len(marks)
for k, v in marks.items():
    if v > avg:
        print(k, v)
        
#Q....................8
products = {}

while True:
    print("\n1. Add Product")
    print("2. Update Product")
    print("3. Delete Product")
    print("4. View Products")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter product name: ")
        price = float(input("Enter price: "))
        products[name] = price

    elif choice == 2:
        name = input("Enter product name to update: ")
        if name in products:
            products[name] = float(input("Enter new price: "))
        else:
            print("Product not found")

    elif choice == 3:
        name = input("Enter product name to delete: ")
        if name in products:
            del products[name]
        else:
            print("Product not found")

    elif choice == 4:
        print("Products:")
        for name, price in products.items():
            print(name, ":", price)

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice")         
    
#Q....................9
a, b, c = map(int, input().split())
if a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")
    
#Q.........................10
students = {}
while True:
    ch = int(input("1.Add 2.View 3.Exit: "))
    if ch == 1:
        name = input("Name: ")
        marks = int(input("Marks: "))
        students[name] = marks
    elif ch == 2:
        print(students)
    else:
        break