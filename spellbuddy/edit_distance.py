def edit_distance(s1, s2):
    """Calculate the distance between two strings using Levenshtein's edit distance function."""
    m, n = len(s1), len(s2)

    # 2d matrix
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # transforming to/from empty string
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                cost = 0
            else:
                cost = 1
            
            dp[i][j] = min(
                dp[i - 1][j] + 1, # deletion
                dp[i][j - 1] + 1, # insertion
                dp[i - 1][j - 1] + cost  # substitution
            )
    
    # bottom right holds final edit distance
    return dp[m][n]