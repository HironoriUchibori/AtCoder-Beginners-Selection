def main():
    str = input().split(' ')
    n = int(str[0])
    a = int(str[1])
    b = int(str[2])
    sum = 0

    for i in range(n):
        if a <= digitSum(i+1) & digitSum(i+1) <= b:
            sum += (i+1)

    print(sum)

# 各桁の和を計算


def digitSum(n):
    # 数値を文字列に変換
    s = str(n)
    # １文字ずつ数値化し配列にする。
    array = list(map(int, s))
    # 合計値を返す
    return sum(array)


if __name__ == "__main__":
    main()
