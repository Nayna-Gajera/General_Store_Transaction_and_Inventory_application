from urllib import request

goog_url = ''


def download_stock_file(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    destination = r'goog.csv'
    fx = open(destination, 'w')
    for l in lines:
        fx.write(l + "\n")
    fx.close()


download_stock_file(goog_url)