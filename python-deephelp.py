# python-deephelp.py

import numpy as np 
import inspect


# remind to fill
def deephelp(m):
    tmpdir = dir(m)

    dic = {"classes":[],"methods":[]}

    for attr in tmpdir:
        if attr[0] == "_":
            continue

        tmpm = getattr(m,attr)
        if inspect.isclass(tmpm):
            tmpdic = {attr:deephelp(tmpm)}
            dic["classes"].append(attr)
        else:
            dic["methods"].append(attr)

    return dic