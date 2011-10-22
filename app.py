import re
from django.conf import settings
from rapidsms.apps.base import AppBase

class App(AppBase):
    def start(self):
        keyword = getattr(settings, 'USHAHIDI_KEYWORD', '')
        self.default_response = getattr(settings, 'USHAHIDI_RESPONSE', 'Thank you for your report.')
        self.pattern = re.compile(r"^\s*(?:%s)(?:[\s,;:]+(.+))?$" % (keyword))
    
    def handle(self, msg):
        match = self.pattern.match(msg.text)
        if match is None:
            return False
        else:
            # TODO: POST message to Ushahidi
            return msg.respond(self.default_response)