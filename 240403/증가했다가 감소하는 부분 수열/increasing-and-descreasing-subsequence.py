n = int(input())

class Sequence:
    def __init__(self, num):
        self.left = []
        self.right = []
        self.num = num
    
    def push_left(self, num):
        if num >= self.num:
            return
        if len(self.left) == 0:
            self.left = [num]
            return
        self.left.append(num)

    def push_right(self, num):
        if num >= self.num:
            return
        if len(self.right) == 0:
            self.right = [num]
            return
        self.right.append(num)
    
    def get_left_len(self):
        l = len(self.left)

        if l == 0:
            return 0

        dp = [1] * l

        for i in range(l):
            cur = self.left[i]
            for j in range(i):
                if self.left[j] < cur:
                    dp[i] = max(dp[i], dp[j] + 1)
            
        return max(dp)

    def get_right_len(self):
        l = len(self.right)

        if l == 0:
            return 0

        dp = [1] * l

        for i in range(l):
            cur = self.right[i]
            for j in range(i):
                if self.right[j] > cur:
                    dp[i] = max(dp[i], dp[j] + 1)
    
        return max(dp)


    def get_len(self):
        
        return self.get_left_len() + self.get_right_len() + 1

sequence_list = list(map(lambda x: Sequence(int(x)), input().split()))

for i in range(n):
    cur = sequence_list[i]
    cur_num = cur.num

    for left_index in range(i):
        left = sequence_list[left_index]
        left.push_right(cur_num)
    
    for right_index in range(i + 1, n):
        right = sequence_list[right_index]
        right.push_left(cur_num)

sequence_len_list = list(map(lambda x: x.get_len(), sequence_list))

print(max(sequence_len_list))