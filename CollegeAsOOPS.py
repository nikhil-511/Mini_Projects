class Office():
    ClgStrength=1000
    st_tempid=10536
    t_tempid=14515
    t_intsalary=50000
    
    def __init__(self,name,num,bran):
        self.st_name=name
        self.st_phnum=num
        self.st_branch=bran
    def Details():
        Id=print("Enter the ID:")
        brn=print("Enter the branch:")
        return Id,brn
        
    def FeeDue():
        Id,brn=Details()
        FeesDetails(brn)
        
            
    def FeeList(brn):
        tut_fee=0
        if brn=="CSE":
            tut_fee=50000
        elif brn=="EEE":
            tut_fee=49000
        elif brn=="ECE":
            tut_fee=55000
        elif brn=="MECH":
            tut_fee=54000
        else:
            print("Branch Not avaliable!!!")
        lib_fee=500
        exam_fee=2500
        total_fee=tut_fee+lib_fee+exam_fee
        return tut_fee,lib_fee,exam_fee,total_fee

    def FeesDetails(brn):
        Tfee,Lfee,Efee,TotalFee=Office.FeeList(brn)
        print("Tution fee:{0} \nExam fee:{1} \nLibrary fee:{2}\nTotal fees:{3}".format(Tfee,Lfee,Efee,TotalFee))


    def AddMember():
        print("Enter the details of student:")
        name=input("Enter the name:")
        phnum=input("Enter the mobile number:")
        branch=input("Enter the branch:")
        prof=input("Student or Teacher:")
        if prof=="Student":
            if input("To know fees details, Enter 1:"):
                Office.FeesDetails(branch)
            print("Temporary student ID:",Office.st_tempid,"\nAdimission successful!!\nWelcome to NEON INSTITUTE OF ENGINEERING AND TECHNOLOGY!!!")
            Office.st_tempid+=1
            
        elif prof=="Teacher":
            print("Initial Salary: ",Office.t_intsalary)
            print("The faculty has been assigned to the department of",branch)
            print("Temporary faculty ID:",Office.t_tempid,"\nRecrutting successful!!\nWelcome to NEON INSTITUTE OF ENGINEERING AND TECHNOLOGY!!!")
            Office.t_tempid+=1
            
    def RemoveMember():
        print("Enter the details to remove the member:")
        Id=input("Enter the ID:")
        proff=input("Student or Teacher:")
        reason=input("Enter the reason for removing the member:")
        rmby=input("Enter your ID:")
        print(proff,"of id",Id,"has been successfully removed by",rmby)


class Library(Office):
    MDueDate="15 Days"
    Fine="10/- per day after due date"
    def __init__(self):
        self.cseBooks=252
        self.mechBooks=526
        self.eeeBooks=460
        self.eceBooks=166
        self.TBooks=1951

    def BookEntry():
        Id,brn=Office.Details()
        Bid=input("Scan the barcode:")
        print("Scanning is successful!!\nDue Date:",Library.MDueDate,"If late to submit before due date, Fine is ",Library.Fine)

    def TBooks():
        print("CSE books present in library are:",self.cseBooks)
        print("EEE books present in library are:",self.eeeBooks)
        print("ECE books present in library are:",self.eceBooks)
        print("MECH books present in library are:",self.mechBooks)
        print("Total books in library are:",self.TBooks)

    def LibraryOpt():
        print("Welcome to NIET Library!!!")
        print("Enter 1 to entry a book \nEnter 2 to get total books in the library")
        opt=int(input("Enter your option"))
        if opt==1:
            Library.BookEntry()
        elif opt==2:
            Library.TBooks()
        else:
            print("Wrong Option!!")
    
print("Welcome to NEON INSTITUTE OF ENGINEEERING AND TECHNOLOGY!!!!\nEnter 1 for Adding a Student/Faculty\nEnter 2 to remove a Student/Faculty\nEnter 3 to get fees details\nEnter 4 to go to library portal")
def opt():
    opt=int(input("Enter your option:"))
    if opt==1:
        Office.AddMember()
    elif opt==2:
        Office.RemoveMember()
    elif opt==3:
        Id,brn=Office.Details()
        Office.FeesDetails(brn)
    elif opt==4:
        Library.LibraryOpt()
    
    else:
        print("Invalid option try again!!!")
        opt()

opt()    
    
