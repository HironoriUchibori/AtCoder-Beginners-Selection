import numpy as np
import itertools

def main():
    s=input()

    #print("組み合わせ文字列の最大数：",int(len(s)//5))
    listing=sets(int((len(s)-1)//5)) #文字列組み合わせリスト
    
    if s in listing:
        print("YES")
    else:
        print("NO")

    

#n個の文字列の結合してできる文字列の全ての組み合わせ
def sets(n):
    word_list1=["dream", "dreamer", "erase", "eraser"] #ここに追加していく
    word_list2=["dream", "dreamer", "erase", "eraser"]
    final_list=[] #全ての組み合わせを格納した1次元配列

    for j in range(n):
        #word_list1とword_list1の組み合わせリスト（各要素はタプル）
        product=list(itertools.product(word_list1,word_list2))
        
        for i in range(len(product)):
            word_list1.append(wordsets(list(product[i])))
    
    #print(word_list1)
    return word_list1

#配列に格納された文字列を結合する
def wordsets(listing):
    return ''.join(listing)


if __name__=="__main__":
    main()