import RPi.GPIO as gpio 
import picamera 
import time 
import smtplib 
from email.MIMEMultipart import MIMEMultipart 
from email.MIMEText import MIMEText 
from email.MIMEBase import MIMEBase 
from email import encoders 
from email.mime.image import MIMEImage 
from gpiozero import Buzzer 
fromaddr = "embedmssr@gmail.com"    # change the email address accordingly 
toaddr = "embedprojmssr@gmail.com" 
subject="INTRUDER ALERT!!!" 
mail = MIMEMultipart() 
mail['From'] = fromaddr 
mail['To'] = toaddr 
mail['Subject'] = subject 
body="Intruder in your house" 
pir=18 
buzz=Buzzer(22) 
HIGH=1 


LOW=0 
gpio.setwarnings(False) 
gpio.setmode(gpio.BCM) 
#gpio.setup(buzz,gpio.OUT)            # initialize GPIO Pin as outputs 
gpio.setup(pir, gpio.IN)            # initialize GPIO Pin as input 
data="" 
def sendMail(data): 
    mail.attach(MIMEText(data,'plain')) 
    mail.attach(MIMEText(body)) 
    print body 
    dat='%s.jpg'%data 
    print dat 
    attachment = open(dat, 'rb') 
    image=MIMEImage(attachment.read()) 
    attachment.close() 
    mail.attach(image) 
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.starttls() 
    server.login(fromaddr, "mssrembed1234!") 
    text = mail.as_string() 
    server.sendmail(fromaddr, toaddr, text) 
    server.quit() 
def capture_image(): 
    data= time.strftime("%d_%b_%Y|%H:%M:%S") 
    camera.start_preview() 
    time.sleep(5) 
    print data 
    camera.capture('%s.jpg'%data) 
    camera.stop_preview() 
    time.sleep(1) 


    sendMail(data) 
buzz.off() 
camera = picamera.PiCamera() 
camera.rotation=180 
camera.awb_mode= 'auto' 
camera.brightness=55 
while(1): 
    if gpio.input(18): 
        buzz.on() 
        time.sleep(1) 
        buzz.off() 
        time.sleep(1) 
        capture_image() 
        while(gpio.input(18)): 
            time.sleep(1) 
    else: 
        buzz.off() 
        time.sleep(1) 
    time.sleep(0.2) 
    time.sleep(0.2) 

 

 

 

 

 

 
