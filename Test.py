class solution():
    def numtostr(self, N, k):
        strnum=''
        for i in range(max(k-2,1),min(k+3,N+1)):
            strnum = strnum + ' ' + str(i)
        return strnum

    def numtostr1(self, N):
        strnum=''
        for i in range(1,N+1):
            strnum = strnum + ' ' + str(i)
        return strnum

    def pagenumber(self, N, k):
        ans = ''
        if N >= 7 : # 需要省略号
            if k - 3 == 1: # 不需要前省略号
                return str(1)+'' + self.numtostr(N,k) + ' ' + '...' + ' ' + str(N)
            elif k - 3 < 1: # 不需要前省略号，显示数字小于7个
                return self.numtostr(N,k) + ' ' + '...' + ' ' + str(N)
            elif k + 3 == N: # 不需要后省略号
                return str(1) + ' ' + '...' + self.numtostr(N,k) + ' ' + str(N)
            elif k + 3 > N: # 不需要后省略号，显示数字小于7个
                return str(1) + ' ' + '...' + self.numtostr(N,k) 
            else: # 需要前、后省略号
                return str(1) + ' ' + '...' + self.numtostr(N,k) + ' ' + '...' + ' ' + str(N)

        elif N < 7: # 不需要省略号
            return self.numtostr1(N)

def main():
    N,k = 10,7
    ans = solution().pagenumber(N,k)
    print(ans)


if __name__ == "__main__":
    main()
