#ASSIGNMENT.....................1
#Q.1

name="pawan"
print(name)
print(name[0])
print(name[4])
print("len of string is:-",len(name))
print(name.upper())
name2="PAWAN"
print(name2.lower())
print("<<<<<slicing>>>>🐒🐒")
print(name[::-1])


#Q..................2

name3="shubham"
print(name3[0:4])
print(name3[2:5])
print(name3[::-1])

#Q...................3
list=[1,2,3,4,5,6,7,8,9]
list.append(100)
print(list)
list.insert(2,44)
print(list)
#list.remove(1)
print(list)
list.pop(3)
print(list)
print(list[::-1])
list.sort()
print(list)
print(len(list))
print(list.count(2))

#Q..................4
tpl=(1,2,3,3,4)
print(tpl)
print(tpl[0])
print(tpl[4])
print(len(tpl))
print(tpl[0:3])
#sum
print(tpl[0]+tpl[1]+tpl[2]+tpl[3]+tpl[4])
#sum
print(sum(tpl))
print(max(tpl))
print(min(tpl))

#q................................5
#UNPACKING
a,b,c,d=(5,6,7,8)
print(a,b,c,d)
#a=5
#b=6
#c=7
#d=8
#PACKING
TPL=(a,b,c,d)
print(TPL)

#Q................................6
student={
    "name":"pawan",
    "age":21,
    "course":"btech",
    "address":"jaipur"
    
}
print(student)
print(student.keys())
print(student.values())
print(student.items())
student.update({"address":"udypur"})
print(student)
student['branch']="cs"
print(student)

#Q....................7
lat=[1,2,3,4,[2,5],7]
print(lat)
print(lat[4][1])

#Q.....................8
mn=int(input("enter the number"))
mn+=10
print(mn)

#Q.......................9
mb=(input("enter the number"))
mc=(input("enter the number"))
print(type(mb))
mb=int(mb)
mc=int(mc)
print(type(mc))
print(mb*mc)

#Q........................10
student={
    "name":"pawan",
    "age":21,
    "course":"btech",
    "address":"jaipur"
    
}
print(student)
print(student.keys())
print(student.values())
print(student.items())
print(student.get('name'))

#Q......................11
ldt=[0,0,0,0]
lft=ldt.copy()
print(ldt,lft)