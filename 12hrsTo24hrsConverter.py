def timeConversion(s):
    a=s[0:8]
    b=''
    if s[8:]=='AM':
        if s[0:2]=='12':
            b='00'+a[2:]
        else:
            return a
    else:
        if s[0:2]=='01':
            b='13'+a[2:]
        elif s[0:2]=='02':
            b='14'+a[2:]
        elif s[0:2]=='03':
            b='15'+a[2:]
        elif s[0:2]=='04':
            b='16'+a[2:]
        elif s[0:2]=='05':
            b='17'+a[2:]
        elif s[0:2]=='06':
            b='18'+a[2:]
        elif s[0:2]=='07':
            b='19'+a[2:]
        elif s[0:2]=='08':
            b='20'+a[2:]
        elif s[0:2]=='09':
            b='21'+a[2:]
        elif s[0:2]=='10':
            b='22'+a[2:]
        elif s[0:2]=='11':
            b='23'+a[2:]
        else:
            return a
        
    return b
            
              
            
            
s = input("Enter the time in 12hrs as HH:MM:SSAM/PM ,Ex: 12:45:54PM\n12hrs>")
result = timeConversion(s)
print("24HRS Format:",result)
