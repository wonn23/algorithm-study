def main():
    n = int(input())
    # print(fibo(n))

def fibo(n):
    if n==2 or n==1:
        # 탈출 조건을 작성해 주세요.
        return 1
    else:
        # 핵심 기능을 작성해 주세요.
        return fibo(n-2)+fibo(n-1)

print(fibo(n))
# def main():
#     n = int(input())
#     print(fibo(n))

# if __name__ == "__main__":
#     main()

