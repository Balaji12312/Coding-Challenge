def word_break(s, dictionary):
    dp = [True] + [False] * len(s)
    for i in range(1, len(s) + 1):
        dp[i] = any(dp[j] and s[j:i] in dictionary for j in range(i))
    return int(dp[len(s)])

s = input("Enter the string: ")
dictionary = set(input("Enter dictionary words separated by space: ").split())

print(word_break(s, dictionary))
