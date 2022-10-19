def main():
    y500_num = int(input())
    y100_num = int(input())
    y50_num = int(input())
    yen = int(input())
    count=0

    for i in range(y500_num+1):
        for j in range(y100_num+1):
            for k in range(y50_num+1):
                if judge(i,j,k,yen):
                    #print("500円：{0}，100円：{1}，50円：{2}".format(i,j,k))
                    count+=1
    
    print(count)


# 合計金額がX円になるか判定する
def judge(y500_num, y100_num, y50_num, yen):
    if 500*y500_num+100*y100_num+50*y50_num == yen:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
