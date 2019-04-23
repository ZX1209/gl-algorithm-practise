eights = [0 for _ in range(25)]
p10 = [0 for _ in range(25)]
def main():
    p10[0] = 1
    for i in range(1,18+1):
        eights[i] = eights[i-1]*10+8
        p10[i] = p10[i-1]*10



if __name__ == '__main__':
    main()