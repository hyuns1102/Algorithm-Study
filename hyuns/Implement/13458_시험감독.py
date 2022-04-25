
if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    B, C = map(int, input().split())
    answer = 0
    for num in arr:
        num -= B
        if num > 0:
            answer += 1
            answer += num // C + (1 if num % C > 0 else 0)
        else:
            answer += 1

    print(answer)