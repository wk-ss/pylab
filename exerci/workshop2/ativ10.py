while True:
    n=int(input())
    if n!=0 and n%2!=0:
        x=int((n+1)/2)
        print(f"{x**2} - {(x-1)**2}")
    else:
        break