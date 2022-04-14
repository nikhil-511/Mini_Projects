class maths:

    def __inti__(self,a,b):
        self.a=a
        self.b=b
        
    def add(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            return a+b+c
        elif a!=None and b!=None:
            return a+b
        else:
            return a
 

s1=maths()
print(s1.add(1,2))
print(s1.add(1,2,3))
