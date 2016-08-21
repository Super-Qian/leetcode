#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def calurate(self, str):
        newstr = str.replace("(", "")
        newstr = newstr.replace(")", "")
        newstr = newstr.replace(" ", "")
        if newstr.isalnum():
            return int(newstr)
        a = newstr.split("-")
        d = []
        y = []
        for c in newstr:
            if c == "-" or c == "+":
                y.append(c)
        for i in a:
            if "+" in i:
                c = i.split("+")
                for l in c:
                    d.append(l)
            else:
                d.append(i)
        sum = int(d[0])
        for m in range(len(y)):
            if y[m] == "+":
                sum += int(d[m+1])
            elif y[m] == "-":
                sum -= int(d[m+1])
        return sum


m = Solution()
str = "(1 +2) -3 +(4  -2)"
s = "12345"
h = "1-11"
print m.calurate(str)
print m.calurate(s)
print m.calurate(h)
