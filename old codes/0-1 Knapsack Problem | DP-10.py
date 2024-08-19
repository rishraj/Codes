n = int(input("Enter the number of items: "))

print("Enter the weights")
wt = []
for i in range(n):
    wt.append(int(input()))
print("Enter the values")
val = []
for i in range(n):
    val.append(int(input()))
max_wt = int(input("Enter the max. weight: "))


# ----------------Bottom up approach-------------------------
dp = [[0 for x in range(max_wt+1)] for y in range(n+1)]

for i in range(n+1):
    for cur_allowed_wt in range(max_wt+1):
        if i == 0 or cur_allowed_wt == 0:
            dp[i][cur_allowed_wt] = 0
        elif wt[i-1] <= cur_allowed_wt:
            dp[i][cur_allowed_wt] = max(dp[i-1][cur_allowed_wt], dp[i-1][cur_allowed_wt-wt[i-1]]+val[i-1])
        elif cur_allowed_wt < wt[i-1]:
            dp[i][cur_allowed_wt] = dp[i-1][cur_allowed_wt]
print(dp[n][max_wt])
# ------------------------------------------------------------


# --------------- Understandable bottom up approach ---------------------------

class Solution:
    def my_Func(value, weight, max_Weight):
        N = len(value)
        dp = [[0] * (max_Weight + 1) for _ in range(N + 1)]
        
        for i in range(N + 1):
            for cur_allowed_wt in range(max_Weight + 1):
                if i and cur_allowed_wt:
                    if cur_allowed_wt >= weight[i - 1]:
                        dp[i][cur_allowed_wt] = max(dp[i - 1][cur_allowed_wt - weight[i - 1]] + value[i - 1],
                                                    dp[i - 1][cur_allowed_wt])
                    else:
                        dp[i][cur_allowed_wt] = dp[i - 1][cur_allowed_wt]
        
        return dp[N][max_Weight]


# ---------------Top down approach----------------------------
cache = [[-1 for _ in range(max_wt+1)] for _ in range(n+1)]


def top_down(val, wt, i_item, cur_allowed_wt, cache):
    if cache[i_item][cur_allowed_wt] >= 0:
        return cache[i_item][cur_allowed_wt]
    if i_item == 0 or cur_allowed_wt == 0:
        cache[i_item][cur_allowed_wt] = 0
    elif cur_allowed_wt >= wt[i_item-1]:
        cache[i_item][cur_allowed_wt] = max(top_down(val, wt, i_item-1, cur_allowed_wt, cache), top_down(val, wt, i_item-1, cur_allowed_wt-wt[i_item-1], cache)+val[i_item-1])
    elif cur_allowed_wt < wt[i_item-1]:
        cache[i_item][cur_allowed_wt] = top_down(val, wt, i_item-1, cur_allowed_wt, cache)
    return cache[i_item][cur_allowed_wt]


print(top_down(val, wt, n, max_wt, m))
# ------------------------------------------------------------

# -------------------- Understandable top down approach----------------------
class Solution:
    def my_Func(value, weight, max_Weight):
        cache = {}
        def knapsack(i, cur_allowed_wt):
            if (i, cur_allowed_wt) in cache:
                return cache[(i, cur_allowed_wt)]
            
            if i == 0 or cur_allowed_wt == 0: # if cur_allowed_wt becomes < 0, loop exits when i becomes 0
                cache[(i, cur_allowed_wt)] = 0
            # if allowed weight is greater than weight of cur_item, take max of either including it or not
            elif cur_allowed_wt >= weight[i - 1]:
                cache[(i, cur_allowed_wt)] = max(value[i - 1] + knapsack(i - 1, cur_allowed_wt - weight[i - 1]),
                                                knapsack(i - 1, cur_allowed_wt))
            # else we can only exclude the item
            elif cur_allowed_wt < weight[i - 1]:
                cache[(i, cur_allowed_wt)] = top_down(i - 1, cur_allowed_wt)
            
            return cache[(i, cur_allowed_wt)]
        
        return knapsack(len(value), max_Weight)

