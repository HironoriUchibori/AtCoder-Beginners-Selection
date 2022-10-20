def main():
    listing=[]
    n=int(input())

    for i in range(n):
        listing.append(int(input()))

    dan=0
    for j in range(n):
        if len(listing)!=0:
            dan+=1
            big=max(listing)
            listing=rm(big,listing)
    
    print(dan)

#長さnのリスト内の特定の値を全て削除
def rm(num,listing):
    newlist=[]
    for i in range(len(listing)):
        if listing[i]!=num:
            newlist.append(listing[i])
    return newlist

if __name__ == '__main__':
    main()