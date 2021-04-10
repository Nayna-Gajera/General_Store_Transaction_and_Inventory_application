import random
import urllib.request


def download_image(url):
    name = random.randrange(1, 100)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)


download_image("https://wonderfulengineering.com/wp-content/uploads/2016/02/Rose-Wallpaper-10-1024x576.jpg")
