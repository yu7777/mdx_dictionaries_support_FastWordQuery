#-*- coding:utf-8 -*-
import os
import re
import random
from ..base import *

DICT_PATH = u"/Users/brian/Documents/mdx/Sound/Sound.mdx" # u'E:\\BaiduYunDownload\\mdx\\L6mp3.mdx'


@register([u'本地词典-Sound', u'Sound'])
class Sound_mdx(MdxService):

    def __init__(self):
        dict_path = DICT_PATH
        # if DICT_PATH is a path, stop auto detect
        if not dict_path:
            from ...service import service_manager, service_pool
            for clazz in service_manager.mdx_services:
                service = service_pool.get(clazz.__unique__)
                title = service.builder._title if service and service.support else u''
                service_pool.put(service)
                if title.startswith(u'Sound'):
                    dict_path = service.dict_path
                    break
        super(Sound_mdx, self).__init__(dict_path)

    @property
    def title(self):
        return getattr(self, '__register_label__', self.unique)

    def _fld_voice(self, html, voice):
        """获取发音字段"""
        if html:
            soup = parse_html(html)
            sounds = soup.find_all('a')
            if sounds:
                for sound in sounds:
                    if (sound["class"][0] =="us") and (voice == "us"):
                        selected_voice = sound['href'][7:]
                    elif (sound["class"][0] =="uk") and (voice == "br"):
                        selected_voice = sound['href'][7:]
                    else:
                        continue
                    val = selected_voice
                    name = get_hex_name('mdx-'+self.unique.lower(), val, 'mp3')
                    name = self.save_file(val, name)
                    if name:
                        return self.get_anki_label(name, 'audio')
        return ''

    @export('BRE_PRON')
    def fld_voicebre(self):
        return self._fld_voice(self.get_html(), 'br')

    @export('AME_PRON')
    def fld_voiceame(self):
        return self._fld_voice(self.get_html(), 'us')
