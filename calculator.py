
print("Hello dosto Im back after a long break")
def Operation():
    A=int(input("Enter the First value:"))
    B=int (input("Enter the second Value:"))
    C=int(input("Select 1 for addtion ,2 for Subtraction, 3 for Multiplication, 4 for division:"))
    if C==1:
        print("Addition of Given numbers:",A+B)
    if C==2:
        print("Subtraction of Given numbers:",A-B)
    if C==3:
        print("Multiplication of Given numbers:",A*B)       
    if C==4:
        print("division of Given numbers:",A/B)
    print("Opration End:") 
    another=input("Want to Do another operation say yes or no:")
    if another=='yes':
        Operation()
    if another=='no':
      print("Thank You, have a great day ahead!") 
        
Operation()
  