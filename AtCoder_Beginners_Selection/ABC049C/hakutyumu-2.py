import sys
S = input()
words = ['dream','dreamer','erase','eraser']
#T = ""
while True:
    for i in range(len(words)):
        if words[i] == S[-(len(words[i])):]:
            #T = words[i] + T
            S = S[0:len(S)-len(words[i])]
            #print("Sは：",S)
            if(len(S)==0):
                print("YES")
                sys.exit()
            break
        elif i == len(words)-1:
            print("NO")
            sys.exit()