#paint can calculator
def paintcalc(length,width):
    area=length*width
    numcans=area/5   #5 suqare meters can be covered with 1 can of paint
    print(f"{numcans} cans of paint is needed")
l=int(input("Enter the length in meters : "))
w=int(input("Enter the width in meters : "))
paintcalc(l,w)
