__author__ = 'gaojian'
__date__ = '3/5/14'
import util
from bs4 import BeautifulSoup as BS

host = 'imap.126.com'
user = ('****@126.com', '***')
sender = '****@example.com'
email_message = util.get_email(host, user, sender)

email_body = util.get_first_text_block(email_message)
# with open('email.html', 'w') as f:
#     f.write(email_body)
# with open('email.html', 'r') as f:
#     email_body = f.read()


soup = BS(email_body)

body = soup.find('body')
link_array = []
img_link_array = []
for link in body.find_all('a'):
    link_array.append(link)

for img_link in body.find_all('img'):
    img_link_array.append((img_link).get('src'))

for item in [text for text in body.stripped_strings]:
    print item
