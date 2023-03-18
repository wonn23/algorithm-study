def countWord(sentence, word): # 한글은 띄어쓰기 단위로 되어있으므로 in을 사용해서 단어를 찾음.
    count = 0
    a=sentence.split(' ')
    for i in a:
        if word in i:
            count +=1
    return count

def main():
    sentence = input()
    searchingWord = input()
    
    print(countWord(sentence, searchingWord))


if __name__ == "__main__":
    main()

