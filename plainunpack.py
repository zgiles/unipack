import codecs
import sys

char_stream = codecs.getreader("utf-8")(sys.stdin)
i=char_stream.readlines()
#a=u''
#for l in i:
#        a+=l
s=i[0]
u=''
count = 0
while (count < len(s)-1):
	u += chr((ord(s[count])-19968) >> 8) + chr(ord(s[count])-19968 & 255 )
	count = count + 1
UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)
print u
