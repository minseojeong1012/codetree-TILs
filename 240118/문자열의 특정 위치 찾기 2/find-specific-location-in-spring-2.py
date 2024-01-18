n = input()
arr = ["apple", "banana", "grape", "blueberry", "orange"]
new_arr = []
cnt = 0

# 해당 위치에 주어진 문자가 있는 문자열을 순서대로 한 줄에 하나씩 출력
for i in range(len(arr)):
    if n == arr[i][2] or n == arr[i][3]:
        new_arr.append(arr[i])
        cnt += 1

for word in new_arr:
    print(word)

print(cnt)