a=int(input("คะแนนเก็บของนักเรียน"))
b=int(input("คะแนนสอบกลางภาคของนักเรียน"))
c=int(input("คะแนนสอบปลายภาคของนัก้รียน"))
d=a+b+c
if(d>=80):
    print("Grade:A")
elif(d>=75 and d<=79):
    print("Grade:B+")
elif(d>=70 and d<=74):
    print("Grade:B")
elif(d>=65 and d<=69):
    print("Grade:C+")
elif(d>=60 and d<=64):
    print("Grade:C")
elif(d>=55 and d<=59):
    print("Grade:D+")
elif(d>=50 and d<=54):
    print("Grade:D")
elif(d>=0 and d<=49):
    print("Grade:F")