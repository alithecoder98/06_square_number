def sq():
    num=float(input("Enter your desired Number for square:"))
    exp=float(input("Enter the number"))
    res=num**exp
    print(f"The {num} powers to the {exp} is {res}")
    sq()
if __name__=="__main__":
    sq()


