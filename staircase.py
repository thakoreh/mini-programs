def staircase(n=0):
    if n==0:
        print("Please enter N greater than 0")
    i=1
    while i!=n+1:
        print(f"{' '*(n-i)}{'#'*i}")
        i+=1

staircase(n=6)