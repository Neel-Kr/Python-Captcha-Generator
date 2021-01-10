from captcha.image import ImageCaptcha
import pyfiglet
import time
info = pyfiglet.figlet_format('Python-Captcha Generator')
print(info)
image = ImageCaptcha()
captcha_data = str(input('Enter the data which you want to convert into captcha: '))
image.write(captcha_data, 'captcha.png')
print('Your captcha is generated successfully!!!')
time.sleep(20)