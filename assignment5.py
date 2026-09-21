def lcs(x, y):
    m = len(x)
    n = len(y)

    # Create DP table
    lcs_table = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table
    for i in range(m + 1):
        for j in range(n + 1):

            if i == 0 or j == 0:
                lcs_table[i][j] = 0

            elif x[i - 1] == y[j - 1]:
                lcs_table[i][j] = lcs_table[i - 1][j - 1] + 1

            else:
                lcs_table[i][j] = max(
                    lcs_table[i - 1][j],
                    lcs_table[i][j - 1]
                )

    # Length of LCS
    index = lcs_table[m][n]

    # Store LCS characters
    lcs_chars = [""] * index

    i = m
    j = n

    # Construct LCS by tracing backwards
    while i > 0 and j > 0:

        if x[i - 1] == y[j - 1]:
            index -= 1
            lcs_chars[index] = x[i - 1]

            i -= 1
            j -= 1

        elif lcs_table[i - 1][j] > lcs_table[i][j - 1]:
            i -= 1

        else:
            j -= 1

    return "".join(lcs_chars)


# Main program
x = input("Enter first sequence: ")
y = input("Enter second sequence: ")

result = lcs(x, y)

print("Longest Common Subsequence:", result)
print("Length of LCS:", len(result))
