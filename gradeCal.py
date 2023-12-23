sub = int(input("Enter your total subject number : "))
latterGrade=[]
gradePoint=[]
subName=[]
for i in range(0,sub):
    subj = input("Enter Subject Name : ")
    subName.append(subj)
    mark = float(input("Enter mark of " + str(subName[i]) + " : "))
    if mark<0 or mark >100:
        print("You Entered wrong !")
        continue
    if mark>=80 and mark<=100:
        latterGrade.append("A+")
        gradePoint.append(5)
    elif mark>=70 and mark<=79:
        latterGrade.append("A")
        gradePoint.append(4)
    elif mark>=60 and mark<=69:
        latterGrade.append("A-")
        gradePoint.append(3.5)
    elif mark>=50 and mark<=59:
        latterGrade.append("B")
        gradePoint.append(3)
    elif mark>=40 and mark<=49:
        latterGrade.append("C")
        gradePoint.append(2)
    elif mark>=33 and mark<=39:
        latterGrade.append("D")
        gradePoint.append(1)
    elif mark>=0 and mark<=32:
        latterGrade.append("F")
        gradePoint.append(0)


print("\n\nSubject\t \tLatter Grade \t     Grade Point\n")  
for i in range(0,sub):
    print(subName[i], "   \t  " ,latterGrade[i], "   \t    ",gradePoint[i]) 
    print("\n") 
        
                
        
    