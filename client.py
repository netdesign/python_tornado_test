import tornado.httpclient
#url.header contains the HTTP header of the requested Url (fetched with Curl) 
url = "http://forums.mysql.com/read.php?10,146117,146155"
http = tornado.httpclient.HTTPClient()
res = http.fetch(url)
