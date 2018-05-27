def countAndSay( n):
        # write your code here
        if n==1:
            return "1"
        if n==2:
            return "11"
        s="11"
        for i in range(3,n+1):
            count=1
            res=""
            for j in range(1,len(s)):
                if s[j]==s[j-1]:
                    count+=1
                if j==len(s)-1 and s[j]!=s[j-1]:
                    res+=str(count)+s[j-1]
                    res+=str(1)+s[j]
                else:
                    res+=str(count)+s[j-1]
                    count=1
            s=res

        print(s)
111221
212111221211

countAndSay(6)
