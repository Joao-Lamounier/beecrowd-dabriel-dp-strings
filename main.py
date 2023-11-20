import argparse


def init_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Strings Dabriel')
    parser.add_argument('--debug', '-d', help='Exibe a matriz DP', action='store_true')
    return parser.parse_args()

def smallest_string_subsequences(x, y):
    size1, size2 = len(x), len(y)
    dp = []

    for i in range(size1 + 1):
        dp.append([0] * (size2 + 1))
    for i in range(size1 + 1):
        if args.debug:
            print()

        for j in range(size2 + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])

            if args.debug:
                print(dp[i][j], end=' ')
    return dp[size1][size2]


if __name__ == '__main__':
    args = init_args()
    smallest = smallest_string_subsequences(input(), input())
    print(f'\n{smallest}')
