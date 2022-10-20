from audioop import reverse


def main():
    listing=input().split(' ')
    n=int(listing[0])
    y=int(listing[1])

    for i in reversed(range(y//10000+1)):
        for j in reversed(range((y-10000*i)//5000+1)):
            if i*10000 + j*5000 + (n-i-j)*1000 == y:
                print(i, j, n-i-j)
                return
    print(-1,-1,-1)

if __name__=="__main__":
    main()