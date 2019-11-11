#-*- coding:utf-8 -*-
import re
import random

from aqt.utils import showInfo, showText
from base import MdxService, export, register, with_styles

path = u'/Users/brian/Documents/EPFD2017/EPFD2017.mdx'


@register(u'EPFD2017')
class EPFD2017(MdxService):

    def __init__(self, dict_path):
        super(EPFD2017, self).__init__(path)

    @property
    def unique(self):
        return self.__class__.__name__

    @property
    def title(self):
        return self.__register_label__

    @export(u'Freq', 1)
    def fld_phonetic(self):
        #tmp = re.split('[^a-zA-Z]', self.word.strip())[0]
        self.word = self.word.replace('something','').replace('somebody','').replace('/',' ').replace('↔',' ').strip()
        self.word = re.sub('[^a-zA-Z]',' ',self.word)
        self.word = re.sub(' +',' ',self.word).strip()
        #self.word = self.word.rsplit(' ', 1)[0]
        
        html = self.get_html()
        m = re.search(r'freq\.</font></b></span>\s?(\d*)', html)
        if m:
            return m.groups()[0]
