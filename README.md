emailutil
=========

imap utils can be used to get the latest email from specified sender

usage: 

from mailbox import util

host = 'imap.126.com'
user = ('****@126.com', '***')
sender = '****@example.com'
email_message = util.get_email(host, user, sender)
email_body = util.get_first_text_block(email_message)
