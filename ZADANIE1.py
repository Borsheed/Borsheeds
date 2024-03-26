A = open("students.csv",encoding="utf8").readlines()
A.pop(0)
for i in range(len(A)):
    A[i] = A[i].strip().split(",")



for i in range(len(A)):
    if "Хадаров Владимир" in A[i][1]:
        print(f"Ты получил: {A[i][4]}, за проект - {A[i][2]}")
        break
d = {}
for i in range(len(A)):
    if A[i][4] != "None":
        clas = A[i][3]
        score = int(A[i][4])
        if clas not in d:
            d[clas] = [score]
        else:
            d[clas] += [score]

for clas in d:
    d[clas] = sum((d[clas])/len(d[clas]),3)
print(d)

for i in range(len(A)):
    if A[i][4] == "None":
        A[i][4] = str(d[A[i][3]])

