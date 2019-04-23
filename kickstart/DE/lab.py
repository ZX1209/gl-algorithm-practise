def rg(tmps, dis):
	index = dis.index(min(dis))
    dis[index]+=10

    if tmps[index] == "0":
            tmps = changestr(tmps,index,'1')
        else:
            tmps = changestr(tmps,index,'0')
    yeild tmps

    rg(tmps,dis)


def rg_test(l):
	yield l
	yield from rg_test(l+1)