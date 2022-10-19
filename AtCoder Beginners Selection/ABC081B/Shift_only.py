def main():
    num=int(input())
    list=input().split(' ')
    cnt=0

    while judge(num, list):
        cnt+=1
        list=half(num,list)

    print(cnt)

#判定がTrueなら1/2

#リストの全てが偶数か判定
def judge(num, list):
    cnt=0
    for i in range(num):
        if int(list[i])%2!=0:
            break
        else:
            cnt+=1
    if cnt==num:
        #print("判定：True")
        return True
    else:
        #print("判定：False")
        return False

#配列の全てを1/2
def half(num,list):
    for i in range(num):
        list[i]=int(int(list[i])/2)
    return list

if __name__ == "__main__":
    main()
