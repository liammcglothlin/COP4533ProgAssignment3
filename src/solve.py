def HVLCS(A, B, val):
    n = len(A)
    m = len(B)

    # create DP[0..n][0..m]
    DP = [[0] * (m + 1) for _ in range(n + 1)]

    # for i = 0 to n: DP[i][0] = 0
    for i in range(n + 1):
        DP[i][0] = 0

    # for j = 0 to m: DP[0][j] = 0
    for j in range(m + 1):
        DP[0][j] = 0

    # for i = 1 to n:
    for i in range(1, n + 1):
        # for j = 1 to m:
        for j in range(1, m + 1):

            if A[i - 1] == B[j - 1]:  # A[i] == B[j]
                DP[i][j] = max(
                    DP[i - 1][j],
                    DP[i][j - 1],
                    DP[i - 1][j - 1] + val[A[i - 1]]
                )
            else:
                DP[i][j] = max(
                    DP[i - 1][j],
                    DP[i][j - 1]
                )

    return DP, DP[n][m]


def reconstruct(A, B, val, DP):
    i = len(A)
    j = len(B)
    result = []

    while i > 0 and j > 0:
        if (
            A[i - 1] == B[j - 1]
            and DP[i][j] == DP[i - 1][j - 1] + val[A[i - 1]]
        ):
            result.append(A[i - 1])
            i -= 1
            j -= 1
        elif DP[i][j] == DP[i - 1][j]:
            i -= 1
        else:
            j -= 1

    result.reverse()
    return "".join(result)

def solve():
    import sys

    lines = [line.strip() for line in sys.stdin if line.strip()]
    idx = 0

    K = int(lines[idx])
    idx += 1

    val = {}
    for _ in range(K):
        ch, v = lines[idx].split()
        val[ch] = int(v)
        idx += 1

    A = lines[idx]
    idx += 1
    B = lines[idx]

    DP, max_value = HVLCS(A, B, val)
    subseq = reconstruct(A, B, val, DP)

    print(max_value)
    print(subseq)


if __name__ == "__main__":
    solve()