import re

str = {
"rtsp://127.0.0.1/1.mp4",
"rtsp://127.0.0.1:9999/1.mp4",
"rtsp://vod.test.com/",
"rtsp://vod.test.com",
"rtsp://vod.test.com/aa12.mp4",
"rtsp://liv12-ww.sfe1.co.kr:3939/",
"http://liv12-ww.sfe1.co.kr:3939/test.html",
"http://liv12-ww.sfe1.co.kr:3939/test.html?id=123",
"http://liv12-ww.sfe1.co.kr:3939/test.html?id=123&pw=123",
"https://liv12-ww.sfe1.co.kr:3939/test.html?id=123&pw=123",
"ftp://liv12-ww.sfe1.co.kr:3939",
}

for item in str:
	print "=> parsing " + item
	match = re.search("^([a-z]+)://([a-zA-Z0-9-.]+):?([0-9]+)?/?([a-zA-Z0-9-.]+)?\??(.+)?", item)
	if match:
		print "protocol : " + match.group(1) 
		print "host : " + match.group(2)
		print "port : " + "None" if match.group(3) is None else match.group(3)
		print "path : " + "None" if match.group(4) is None else match.group(4)
		print "query : " +"None" if match.group(5) is None else match.group(5)

