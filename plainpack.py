import codecs
import sys

i=sys.stdin.readlines()
a=''
for l in i:
        a+=l
s=a
u=u''
count = 0
while (count < len(s)):
        if count == len(s)-1:
                u += unichr(19968+(ord(s[count])*16*16))
                count = count + 1
        else:
                u += unichr(19968+(ord(s[count])*16*16)+(ord(s[count+1])))
                count = count + 2
UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)
print u
