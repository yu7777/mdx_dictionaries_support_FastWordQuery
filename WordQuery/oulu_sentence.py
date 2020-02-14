#-*- coding:utf-8 -*-
import re
import random


from aqt.utils import showInfo, showText

from .base import export, with_styles, register, MdxService

path = u'/Users/shengbingyu/Documents/english study/mdx/欧路例句词典 MI/欧路例句词典MI(revised).mdx'


@register(u'本地词典-欧陆句子随机')
class Ldoce611111(MdxService):

    def __init__(self, dict_path):
        super(Ldoce611111, self).__init__(path)

    @property
    def unique(self):
        return self.__class__.__name__

    @property
    def title(self):
        return self.__register_label__


    @export(u'audio', 1)
    def fld_phonetic(self):
        html = self.get_html()
        m = re.search(r'<span class="audio">(.*?)</span audio>', html)
        if m:
            return re.sub('<img.*?></img>','',m.groups()[0])
        return ''

    @export(u'en_sentence', 2)
    def fld_voicebre(self):
        html = self.get_html()
        m = re.search(r'<span class="en_sentence">(.*?)</span en_sentence>', html)
        if m:
            return m.groups()[0]
        return ''
		
    @export(u'cn_sentence', 3)
    def fld_voiceame(self):
        html = self.get_html()
        m = re.search(r'<span class="cn_sentence">(.*?)</span cn_sentence>', html)
        if m:
            return m.groups()[0]
        return ''

    @export(u'audio_PLUS_en_sentence', 4)
    def fld_sentence(self):
        html = self.get_html()
	m = re.search(r'<span class="audio">(.*?)</span en_sentence>', html)
        if m:
            return re.sub('<img.*?></img>','',m.groups()[0])
        return ''

    @export(u'source_PLUS_cn_sentence', 5)
    def fld_cnsentence(self):
        html = self.get_html()
	m = re.search(r'<span class="source">(.*?)</span cn_sentence>', html)
        if m:
            return m.groups()[0]
        return ''		

    @export(u'random_audio_PLUS_en_sentence', 6)
    def fld_randomsentence(self):
        html = self.get_html()
	m = re.findall(r'<span class="audio">(.*?)</span en_sentence>', html)
        if m:
            index = random.randrange(0,len(m)-1,1)
            return re.sub('<img.*?></img>','',m[index])
        return ''

