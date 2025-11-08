import os
from vars import OWNER, CREDIT
from settings_persistence import get_setting

processing_request = False
cancel_requested = False
caption = get_setting('caption', '/cc1')
endfilename = get_setting('endfilename', '/d')
thumb = get_setting('thumb', '/d')
CR = get_setting('credit', f"{CREDIT}")
cwtoken = os.environ.get('CWTOKEN', '')
cptoken = os.environ.get('CPTOKEN', '')
pwtoken = os.environ.get('PWTOKEN', '')
vidwatermark = get_setting('vidwatermark', '/d')
raw_text2 = get_setting('raw_text2', '480')
quality = get_setting('quality', '480p')
res = get_setting('res', '854x480')
topic = get_setting('topic', '/d')
