#This is a simple Calculator program made by Ostad-Batch2_Md_Al_Imran_Tonmoy

def add(takein1,takein2):
    return takein1+takein2

def sub(takein1,takein2):
    return takein1-takein2

def mul(takein1,takein2):
    return takein1*takein2

def div(takein1,takein2):
    return takein1/takein2

def modu(takein1,takein2):
    return takein1%takein2
try:
    op=int(input("Select operation:\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Modulus\nEnter choice (1/2/3/4/5):"))
    try:
        takein1 = float(input("Enter First Number:"))
        takein2 = float(input("Enter Second Number:"))
    except ValueError:
        print ("Error: Invalid Input. Please enter valid number.")

    if (op==1):
        print (f"{takein1}+{takein2}= {add(takein1,takein2)}")
    elif (op==2):
        print (f"{takein1}-{takein2}= {sub(takein1,takein2)}")
    elif (op==3):
        print (f"{takein1}*{takein2}= {mul(takein1,takein2)}")
    elif (op==4):
        try:
            print (f"{takein1}/{takein2}= {div(takein1,takein2)}")
        except ZeroDivisionError:
            print ("Error: Division by zero is not allowed.")
    elif (op==5):
        try:
            print (f"{takein1}%{takein2}= {modu(takein1,takein2)}")
        except ZeroDivisionError:
            print ("Error: Modulus by zero is not allowed.")
    else:
        print ("Invalid Operator")

except Exception as e:
    print(f"Unexpected Error: {e}")
