def getPhoneNumber(s):
    main_key={'one':'1', 'two':'2', 'three':'3','four':'4', 'five':'5', 'six': '6','seven':'7', 'eight':'8','nine':'9','zero':'0'}
    triple={'one':'11', 'two':'22', 'three':'33','four':'44', 'five':'55', 'six': '66','seven':'77', 'eight':'88','nine':'99','zero':'00'}
    number = s.split()
    for i in number:
        if i == 'double':
            number[number.index(i)]=main_key[number[number.index(i)+1]]
        elif i == 'triple':
             number[number.index(i)]=triple[number[number.index(i)+1]]
        else:
            number[number.index(i)]=main_key[i]
    number=''.join(number)
    return number

print(getPhoneNumber("five one zero six triple eight nine six four"))
