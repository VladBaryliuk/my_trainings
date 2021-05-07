blanks = 0
detals = 0
all_detals = 0
def detals(N, K, M):
    global blanks, detals, all_detals
    while N >= K:
        help_var = N - K
        blanks += help_var
        N = N - K
        detals = blanks // M
        blanks = detals % M
        print(all_detals)
        all_detals = all_detals + detals
        if blanks != 0:
            N = N + blanks
    print(all_detals)

detals(int(input()), int(input()), int(input()))