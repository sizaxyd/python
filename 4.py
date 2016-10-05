import urllib.request
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
num = '12345'

with urllib.request.urlopen(url + num) as response:
    html = response.read()

num = bytes.decode(html)[-5:]
