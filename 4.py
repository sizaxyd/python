import urllib.request
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
num = '8022'


def fetch():
    global num
    with urllib.request.urlopen(url + num) as response:
        html = response.read()
    num = bytes.decode(html).split()[-1]
    print(num)
    return

while True:
    fetch()
