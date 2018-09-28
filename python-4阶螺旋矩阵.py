for k in range(3,0,-2):
    # 缺圈
    for dr,dc,dk in ((0,1,k),(1,0,k),(-1,0,k),(-1,0,k-1)):
        for _ in range(k):
            r+=dr
            c+=dc

            pass
    # 最后一步??
    #(0,1,1)