# rgb2hsv(Travis).py

# rgb (r,g,b)


def rgb2hsvPoint(RGB):
    minV = min(RGB)
    maxV = max(RGB)

    R,G,B = RGB

    V = maxV
    S = (maxV-minV)/maxV

    if S == 0:
        H = 0
    else:
        R1 = (maxV-R)/(maxV-minV)
        G1 = (maxV-G)/(maxV-minV)
        B1 = (maxV-B)/(maxV-minV)

    if R == maxV and G == minV:
        H = 5+B1
    elif R == maxV and G != minV:
        H = 1-G1
    elif G == maxV and B == minV:
        H = R1+1
    elif G == maxV and B != minV:
        H = 3-B1
    elif R == maxV:
        H = 3+G1
    else:
        H = 5-R1

    H = H*60

    return (H,S,V)

if __name__ == '__main__':
    RGB = (255,255,255)

    # r = rgb2hsvPoint(RGB)

    # print(r)