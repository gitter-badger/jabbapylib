#!/usr/bin/env python

"""
Configuration part.

# import jabbapylib.config as cfg
"""

import os

# portability tip: in ~/.mozilla/firefox put a symbolic link on 
# ~/.mozilla/firefox/XXXXXXXX.default/cookies.sqlite
COOKIE_DB = "{home}/.mozilla/firefox/cookies.sqlite".format(home=os.path.expanduser('~'))
ESPEAK = '/usr/bin/espeak'
MPLAYER = '/usr/bin/mplayer'
WGET = '/usr/bin/wget'
XSEL = '/usr/bin/xsel'
TIDY = '/usr/bin/tidy'
LYNX = '/usr/bin/lynx'

required_files = (
    COOKIE_DB,      # to get webpages that are protected with cookies
    ESPEAK,         # text to speech
    MPLAYER,        # play audio/video
    WGET,           # get webpages
    XSEL,           # copy to clipboard
    TIDY,           # tidy up HTML source
    LYNX,           # for converting HTML to text
)

USER_AGENT = 'Mozilla/5.0 (Ubuntu; X11; Linux x86_64; rv:9.0.1) Gecko/20100101 Firefox/9.0.1'
COOKIES_TXT = '{home}/tmp/cookies_jabbapylib_tmp.txt'.format(home=os.path.expanduser('~'))

TEST_ASSETS_DIR = os.path.dirname(__file__) + '/../tests/_assets'
TEST_TMP_DIR = os.path.dirname(__file__) + '/../tests/_tmp'
TEST_TMP_FILE = os.path.dirname(__file__) + '/../tests/_tmp/test.tmp'

TMP_DIR = '/tmp/jabbapylib_20120119_tmp'
TMP_FILE = '/tmp/jabbapylib_20120119_tmp.txt'

if __name__ == "__main__":
    print TEST_ASSETS_DIR