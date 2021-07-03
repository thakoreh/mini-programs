#18003569377->1800flowers



def whatwordpresent(number,listOfWords):
    returningList=[]
    for eachWord in listOfWords:
        #foo
        num=convertor(eachWord)
        print(num)
        if str(num) in str(number):
            returningList.append(eachWord)
    return returningList
    

def convertor(word):
    mainList=[
        {
        "abc":'2',
        },
        {
        "def":'3',
        },
        {
        "ghi":'4',
        },
        {
        "jkl":'5',
        },
        {
        "mno":'6',
        },
        {
        "pqrs":'7',
        },
        {
        "tuv":'8',
        },
        {
        "wxyz":'9',
        }
    ]
    tempList=[]
    for char in word:
        for each in mainList:
            if char in ('').join(list(each.keys())):
                tempList.append(('').join(list(each.values())))
            else:
                continue
    return int(float(('').join(tempList)))
    


if __name__=="__main__":
    phonenumber="3662277"
    words=['foo','bar','baz','foobar','emo','cap','car','cat']
    answer=whatwordpresent(phonenumber,words)
    print(answer)