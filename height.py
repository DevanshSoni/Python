print("Enter height of the person \n")
a=int(input())
if a<150:
    print("Dwarf")
elif a>=150 and a<=165:
    print("Average height")
elif a>165 and a<=195:
    print("Taller")
elif a>195:
    print("Abnormal Height")