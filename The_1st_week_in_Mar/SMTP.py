from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart, MIMEBase
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


# 输入email地址和口令
from_addr = input('From: ')
password = input('Password: ')

# 输入收件人地址
to_addr = input('To: ')
# 输入SMTP服务器地址
stmp_server = input('SMTP server: ')

msg = MIMEMultipart()
msg['From'] = _format_addr('Python爱好者 <%s>'% from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候！', 'utf-8').encode()

# 邮件正文
# 插入纯文本
# msg.attach(MIMEText("Hello, send by Python...\nFrom William's computer", 'plain', 'utf-8'))

# 正文中嵌入图片
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
                    '<p><img src="cid:0"></p>' +
                    '</body></html>', 'html', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片
with open('D:\Download\Pictures\RGB巡线.jpg', 'rb') as f:
    # 设置附件的MIME和文件名，这里是jpg类型:
    mime = MIMEBase('image', 'jpeg', filename='test.jpg')
    # 加上必要的头信息
    mime.add_header('Content-Dispositon', 'attachment', filename='test.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来
    mime.set_payload(f.read())
    # 用base64编码
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart
    msg.attach(mime)


try:
    # server = smtplib.SMTP(smtp_server, 25)
    # SMTP协议默认端口是25
    server = smtplib.SMTP_SSL(stmp_server, 465)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    print('发送成功!')
except:
    print('发送失败!')

finally:
    server.quit()
