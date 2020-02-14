#-*- coding:utf-8 -*-
import re

from aqt.utils import showInfo, showText

from .base import export, with_styles, register, MdxService

path = u'/Users/shengbingyu/Documents/english study/mdx/简明英汉字典增强版/简明英汉字典增强版.mdx'


@register(u'本地词典-简明英汉')
class Ldoce611(MdxService):

    def __init__(self, dict_path):
        super(Ldoce611, self).__init__(path)

    @property
    def unique(self):
        return self.__class__.__name__

    @property
    def title(self):
        return self.__register_label__

    @export(u'no entry word', 1)
    def fld_phonetic(self):
        html = self.get_html()
        m = re.search(r'<span class="content"><br />(.*?)</span content>', html)
        if m:
            return m.groups()[0]
        return ''
