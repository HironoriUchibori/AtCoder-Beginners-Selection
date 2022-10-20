'''
N 枚のカードがあります. 
i 枚目のカードには, aiという数が書かれています.Alice と Bob は, これらのカードを使ってゲームを行います. ゲームでは, Alice と Bob が交互に 1 枚ずつカードを取っていきます. Alice が先にカードを取ります.2人がすべてのカードを取ったときゲームは終了し, 取ったカードの数の合計がその人の得点になります. 2 人とも自分の得点を最大化するように最適な戦略を取った時, Alice は Bob より何点多く取るか求めてください.
'''

def main():
    n = int(input())
    listing = input().split(' ')
    numlist = list(map(int, listing))
    alice = 0
    bob = 0

    for i in range(n):
        if i % 2 == 0:
            alice += numlist.pop(numlist.index(max(numlist)))
        else:
            bob += numlist.pop(numlist.index(max(numlist)))

    print(alice-bob)


if __name__ == "__main__":
    main()
