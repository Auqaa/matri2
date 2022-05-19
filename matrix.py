import random 


q = 0
w = random.randint(8,15)
a = int(input("Введите число: "))

m = []
m.append([a]*w)
while q < w-2:
    q = q + 1
    mm = [0]*w #создание вертикали
    mm[0] = a  #замена певого 
    mm[-1] = a #замена последнего
    mm[q]= a
    mm[-q-1] = a
    m.append(mm)
    
    
m.append([a]*w)

for aa in m:
    print(aa)