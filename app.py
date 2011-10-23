import re
from urllib import urlopen, quote_plus
from django.conf import settings
from rapidsms.apps.base import AppBase

class App(AppBase):
    def start(self):
        keyword = getattr(settings, 'USHAHIDI_KEYWORD', '')
        self.default_response = getattr(settings, 'USHAHIDI_RESPONSE', 'Thank you for your report.')
        self.error_response = getattr(settings, 'USHAHIDI_ERROR', "Due to some error, we're unable to process your message. Please resend.")
        self.pattern = re.compile(r"^\s*(?:%s)(?:[\s,;:]+(.+))?$" % (keyword))
        self.trigger_url = re.sub('\$\{sender_number\}', '%(sender)s', getattr(settings, 'USHAHIDI_TRIGGER_URL'))
        self.trigger_url = re.sub('\$\{message_content\}', '%(message)s', self.trigger_url)
    
    def handle(self, msg):
        match = self.pattern.match(msg.text)
        if match is None:
            return False
        else:
            trigger_url = self.trigger_url % ({'message': quote_plus(msg.text), 'sender': quote_plus(msg.peer)})
            try:
                urlopen(trigger_url)
            except IOError:
                return msg.error(self.error_response)
            return msg.respond(self.default_response)