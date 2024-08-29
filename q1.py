students_present={}
def mark_present(name,day):
    if name not in students_present[day]:
        students_present[day].append(name)
        print("Updated List:-")
        for name in students_present:
            print(name)

    else:
        print("Student already marked present")

def remove_student(name,day):
    if name in students_present[day]:
        students_present[day].remove(name)
        print("Updated List:-")
        for name in students_present:
            print(name)

def is_present(name,day):
    if name in students_present[day]:
        return True
    else:
        return False

def display_attendance():
    if len(students_present) !=0:
        for name in students_present:
            print(name+1,":")
            for i in students_present[name]:
                print(i)
    else:
        print("No record")

def find_pivot(st,en,attendance):
    piv=attendance[en]
    i=st-1
    j=st
    while j<=en:
        if attendance[j] <=piv:
            i+=1
            tmp=attendance[j]
            attendance[j]=attendance[i]
            attendance[i]=tmp
        j+=1
    return i+1
    
def quicksort(st,en,i):
    if st<en:
      pivot=find_pivot(st,en,i)
      quicksort(st,pivot-1,i)
      quicksort(pivot+1,en,i)


days=int(input("tell no. of days: "))
for j in range(0,days):
    num=int(input(f"tell initial number of students for day {j+1}:"))
    students_present[j]=[]
    for i in range(0,num):
       name=input("Enter student name:")
       students_present[j].append(name)
print("Choose option -")
print("1.Add student in present list.")
print("2.remove student from present list.")
print("3.Check if a student is in present list.")
print("4.View student present list.")
print("5.View sorted list.")
opt=int(input("Type your option here:"))

if opt<1:
    print("wrong option")
elif opt>5:
    print("wrong option")
elif opt<4:
    name=input("Enter student name:")
    days=int(input("tell day: "))
    if opt==1:
        mark_present(name,days)
    elif opt==2:
        remove_student(name,days)
    else:
        if is_present(name,days):
            print("Student is present")
        else:
            print("Student not present")
elif opt==4:
    display_attendance()
else:
   for i in students_present:
        quicksort(0,len(i)-1,i)

    


        