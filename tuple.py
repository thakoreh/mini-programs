def create_tuple(*args,**kwargs):
    print(tuple(*args,*kwargs))
    return tuple(*args,*kwargs)
        
    
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(create_tuple(integer_list)))
    