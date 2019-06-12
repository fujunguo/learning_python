import requests
from bs4 import BeautifulSoup
import time
import pdfkit
import os

def parse_url_to_html(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    body = soup.find_all(class_="entry-content")
    html = str(body)
    with open('makeblock.html', 'w', encoding='utf-8') as f:
        f.write(html)
    return 'makeblock.html'


def save_pdf(htmls ,file_name):
    """
    把所有HTML文件转换成PDF文件
    :param htmls: html文件名
    :param file_name: pdf文件名
    :return:
    """
    options = {
    'page-size': 'Letter',
    'encoding': 'UTF-8',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'custom-header':[
        ('Accept-Encoding', 'gzip')
        ],
    'outline-depth': 10,
    }
    config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
    pdfkit.from_file(htmls, file_name, options=options, configuration=config)


def main():
    electronics = ['mini-gripper', 'megapi-pro-encoder-dc-motor-driver','megapi-pro-esc-driver', 'megapi-pro', 'megapi-pro-4dc-motor-driver', 'megapi-pro-shield-rj25', 'bluetooth-controller', 'smart-servo-ms-12a','mbot-li-polymer-battery', 'me-audio-player', 'rgb-line-follower', 'me-color-sensor-v1', 'me-pm2-5-sensor', 'dc-frame-type-solenoid-hcne1-0530', 'me-shutter', 'me-ir-remote-controller', 'me-potentiometer', 'me-joystick', 'me-4-button', 'led-rgb-strip-addressable-sealed-0-5m1m', 'me-led-matrix-8x16', 'me-tft-lcd-screen-2-2-inch', 'me-rgb-led', 'me-7-segment-display', 'bluetooth-moduledual-mode', 'bluetooth-moduledual-mode', 'me-usb-host', 'me-wifi', 'me-infrared-reciver-decode', 'me-bluetooth-moduledual-mode', 'me-micro-switch-ab', 'me-gas-sensormq2', 'me-temperature-and-humidity-sensor', 'me-flame-sensor', 'temperature-sensor-waterproofds18b20', 'me-compass', 'me-touch-sensor','me-ultrasonic-sensor', 'me-sound-sensor','me-pir-motion-sensor', 'me-line-follower', 'me-light-sensor', 'me-3-axis-accelerometer-and-gyro-sensor', '2h-microstep-driver', 'me-encoder-motor-driver', 'me-stepper-driver', 'me-dual-motor-driver','me-130-dc-motor', 'mcore','makeblock-orion','me-auriga','me-high-power-encoder-motor-driver','megapi','me-micro-switch-a','usb-2-0-a-male-to-micro-b-male-cable','shutter-cable-c1-c3-n1-n3-for-canon','rj25-to-dupont-wire','6p6c-rj25-cable','battery-holder-for-6-aa','ac-to-dc-12v-3a-wall-adapter-power-supply-for-arduino','water-pump-motor-dc-12v-370-04pm','air-pump-motor-dc-12v-3202pm','micro-peristaltic-pump-dc12-0v','air-pump-motor-dc-12v-370-02pm','555-high-speed-cnc-motor-24v-10000rpm','dc-encoder-motor-25-6v-185rpm','tt-geared-motor-dc-6v-200rpm','mini-metal-gear-motor-n20-dc-12v','36-dc-geared-motor-12v240rpm','mg995-standard-servo','meds15-servo-motor', '9g-micro-servo','820-coreless-motor','42byg-geared-stepper-motor','57byg-stepper-motor','42byg-stepper-motor','dc-motor-37-12v','dc-motor-25-6v','me-uno-shield','me-shield-for-raspberry-pi','me-rj25-adapter']
    for i in electronics:
        start = time.time()
        url = "https://www.makeblock.com/project/" + i
        file_name = i + "_User_Manual.pdf"
        htmls = parse_url_to_html(url) 
        save_pdf(htmls, file_name)
        os.remove(htmls)

        total_time = time.time() - start
        print(u"总共耗时: %f 秒" % total_time)


if __name__ == '__main__':
    main()
