def count_substring(s,sb):
    l=len(sb)
    c=0
    sr=[]
    if len(s)<=200 and len(s)>=1:
        for i in range(len(s)):
           if s[i]==sb[0]:
               sr.append(i)
    if s.find(sb)!=-1:
        for j in sr:
            try:
                a=s[j:j+l]
                if a==sb:
                    c=c+1
            except:
                break
    return c
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)       
