def is_A_in_B(A, B):
    if len(A) <= 0:
        return True
    
    if A[0] in B:
        # A[0]을 확인했다면, 다음 순서로 무엇을 확인해야 할까요?
        return is_A_in_B(A[1:], B)
    else:
        return False


def main():
    A, B = input().split()
    print(is_A_in_B(A, B))

if __name__ == "__main__":
    main()