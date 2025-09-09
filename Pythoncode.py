class Pythoncode():
    def Subfields():
        print("Subfields in AI are:\n")
        tuple=('Machine Learning','Neural Network','Vision','Robotics','Speech Processing','Natural Language Processing')
        for items in tuple:
            print(items)
        
        
    def oddeven():
        data=int(input("Enter your choice"))
        if(data%2)==0:
            print("Your data is even number")
            choice="even"
        else:
            print("Your data is odd number")
            choice="odd"
        return(choice)


    def eligibilitycheck():
        Gender=str(input("Enter your gender:"))
        Age=int(input("Enter your age"))
        if(Gender=='Male' and Age>25):
            print("Eligible")
        elif(Gender=='Female' and Age>21):
            print("Eligible")
        else:
            print("Not Eligible")
        
    
    def Percentage():
            sub1=int(input("Enter Sub1 Mark:"))
            sub2=int(input("Enter Sub2 Mark:"))
            sub3=int(input("Enter Sub3 Mark:"))
            sub4=int(input("Enter Sub4 Mark:"))
            sub5=int(input("Enter Sub5 Mark:"))
            total=sub1+sub2+sub3+sub4+sub5
            percentage=int((total/500)*100)
            print("Total:",total)
            print("Percentage:",percentage)
    
    
    def Triangle(h1,h2,b1):
        Area=((h1*b1)/2)
        Perimeter=(h1+h2+b1)
        print("Area of the Triangle:",Area)
        print("Perimeter of the Triangle:",Perimeter)