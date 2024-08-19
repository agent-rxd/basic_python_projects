num=int(input("Enter the number of scores "))
scores=[]
for i in range(num):
    scrr=input()
    scores.append(scrr)

highest=scores[0]
for scr in scores:
    if (scr>highest):
        highest=scr

print("The highest is : ",highest)

