"""
http://forsk.in/images/Forsk_logo_bw.png"

Download the image from the url above and store in your workking diretory with the same
name as the image name.

Do not hardcode the name of the image


"""
from io import BytesIO
from PIL import Image
import requests
url="http://forsk.in/images/Forsk_logo_bw.png"
response=requests.get(url).content
img=Image.open(BytesIO(response))
img.save("forsk.png")
