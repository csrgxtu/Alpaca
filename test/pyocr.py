#!/usr/bin/env python
from PIL import Image
import sys

path = ['',
 '/usr/local/bin',
 '/usr/lib/python2.7',
 '/usr/lib/python2.7/plat-x86_64-linux-gnu',
 '/usr/lib/python2.7/lib-tk',
 '/usr/lib/python2.7/lib-old',
 '/usr/lib/python2.7/lib-dynload',
 '/home/archer/.local/lib/python2.7/site-packages',
 '/home/archer/.local/lib/python2.7/site-packages/pyocr-0.4.1-py2.7.egg',
 '/usr/local/lib/python2.7/dist-packages',
 '/usr/local/lib/python2.7/dist-packages/SimpleCV-1.3-py2.7.egg',
 '/usr/local/lib/python2.7/dist-packages/pyocr-0.4.1-py2.7.egg',
 '/usr/lib/python2.7/dist-packages',
 '/usr/lib/python2.7/dist-packages/PILcompat',
 '/usr/lib/python2.7/dist-packages/gtk-2.0',
 '/usr/lib/pymodules/python2.7',
 '/usr/lib/python2.7/dist-packages/ubuntu-sso-client',
 '/usr/local/lib/python2.7/dist-packages/IPython/extensions',
 '/home/archer/.ipython']

sys.path.extend(path)

print sys.path

import pyocr
import pyocr.builders

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
# The tools are returned in the recommended order of usage
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))
# Ex: Will use tool 'libtesseract'

langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))
lang = langs[0]
print("Will use lang '%s'" % (lang))
# Ex: Will use lang 'fra'

txt = tool.image_to_string(
    Image.open('test.png'),
    lang=lang,
    builder=pyocr.builders.TextBuilder()
)
# word_boxes = tool.image_to_string(
#     Image.open('test.png'),
#     lang="eng",
#     builder=pyocr.builders.WordBoxBuilder()
# )
# line_and_word_boxes = tool.image_to_string(
#     Image.open('test.png'), lang="fra",
#     builder=pyocr.builders.LineBoxBuilder()
# )
#
# # Digits - Only Tesseract (not 'libtesseract' yet !)
# digits = tool.image_to_string(
#     Image.open('test-digits.png'),
#     lang=lang,
#     builder=pyocr.tesseract.DigitBuilder()
# )
