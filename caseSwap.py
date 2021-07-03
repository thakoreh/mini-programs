def swap_case(s):
    converted_string=''
    for _ in s:
        if _.lower()==_:
            _=_.upper()
            converted_string+=_
        elif _.upper()==_:
            _=_.lower()
            converted_string+=_
    return converted_string

if __name__ == '__main__':
    this_string=input("What is your string?")
    swap_case(this_string)
    pass