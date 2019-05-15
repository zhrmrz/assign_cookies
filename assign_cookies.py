class Sol:
    def assign_cookies(self,g,s):
        g.sort()
        s.sort()
        j=1
        c=0
        for i in range(1,len(g)+1):
            if g[-i]>s[-j]:
                continue
            else:
                c+=1
                j+=1
        return c

if __name__ == '__main__':
    p1=Sol()
    print(p1.assign_cookies([1,2],[1,2,3]))
