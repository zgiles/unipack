unipack
=======

Packs ASCII characters into Unicode to be able to tweet longer.

If a system, like Twitter, supports 140 characters, they're not supporting 140 bytes, but rather 140 characters which could be single byte or double byte. We can take advantage of this and pack single byte characters into double byte characters to fit 280 characters of text. There are many reasons this could be useful .. such as longer tweets without a foreign site .. such as enough space to encrypt some text .. etc. 

This takes something such as "Lorem ipsum dolor sit amet, consect" and packs it in to this "驯쁥묠띰셵묠뉯멯쀠셩술꽭덴稠녯뱳덣숊". 

The algorithm for this is to pack the characters together, such as 0x34, 0x76 into 0x3476. Then we (for fun) push this into a character range that is readable by adding 19928 (or 0x4E00) to push us into somewhere in the "Yijing Hexagram Symbols", or a pile of asian characters. Technically, all characters are readable, but if we hit something like a backspace character or a strange right-to-left character, it could be hard to copy and paste.

Since it's ASCII only input, I think we would only be in the range 0x4E00-0x4EFF for now.. though, we should be able to go into the 0x9XXX and higher. Up in the 0xa and b it might get a little funny.

You can use it like so:
[gilesz01@localhost unipack]$ echo "Lorem ipsum dolor sit amet, consect" | python ./plainpack.py 
驯쁥묠띰셵묠뉯멯쀠셩술꽭덴稠녯뱳덣숊
[gilesz01@localhost unipack]$ echo "驯쁥묠띰셵묠뉯멯쀠셩술꽭덴稠녯뱳덣숊" | python ./plainunpack.py 
Lorem ipsum dolor sit amet, consect

[gilesz01@localhost unipack]$

More Sample Text:
$ python plainpack.py 
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
驯쁥묠띰셵묠뉯멯쀠셩술꽭덴稠녯뱳덣쉥쉵쀠꽤띰띳띣띮딠덬띴稠셥눠뉯湥띵셭뵤湴덭빯쀠띮녩뉩뉵뱴湵술멡끯쁥湥술뉯멯쁥湭꽧뱡湡멩뽵꼮湕술덮띭湡눠뭩뱩묠쑥뱩꽭稠뽵띳湮뵳쉲썤湥왥쁣띴꽴띯밠썬멡뭣봠멡끯쁩선뱩셩湵술꽬띱썩븠델湥꼠녯뭭뵤봠녯뱳덱썡숮堀


Some known bugs:
* It tends to add a "newline" at the end of the decode.. but it depends on how many words you had at the input. It's because of my 0xXX00 from the "if in the packing. I might need to put a "if ord(s[count])==0, then don't print it" in there
* Input to plainpack.py must be ASCII Characters numbers 0-255. If not, it will crash.
* Input to plainunpack.py must be "PlainPacked unicode characters" in the appropriate range. If not, it will crash.
* You probably need to do "python ./plainpack.py" instead of "./plainpack.py" depending on your shell. Some really don't like expecting unicode input and try to launch xwindows etc
* May have trouble on mac python because it is a "narrow build" only supporting a limited number of characters. Seems to be OK for characters I'm using now (Below 0xFFFF). See [1]

Working on:
* Testing all input cases
* Testing if this is the right offset range to be in (0x4E00)
* Adding Encryption (via several methods)
* error reporting etc
* Command line arguments
* one executable instead of 2

Useful sites for debugging:
http://textmechanic.com/ASCII-Hex-Unicode-Base64-Converter.html
http://www.utf8-chartable.de/unicode-utf8-table.pl
http://docs.python.org/2/howto/unicode.html
[1] http://wordaligned.org/articles/narrow-python
