class voter():
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        
    def __ge__(self,num):
        if self.age >= num:
            return True
        else:
            return False
        
    def __add__(self,num):
        a1=self.num1+num.num1
        a2=self.num2+num.num2
        s=voter(a1,a2)
        return s
        

voter1=voter(5,2)
voter2=voter(15,12)
sum1=voter1+voter2
print(sum1.num1,sum1.num2)


