import sys

string = input()
cnt_arr = [0] * 26 # lower alpha
for char in string:
    cnt_arr[ord(char) - 97] += 1
    if cnt_arr[ord(char) - 97] == 2:
        print("Yes")
        sys.exit(0)
print("No")