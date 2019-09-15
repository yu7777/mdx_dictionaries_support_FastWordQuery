#-*- coding:utf-8 -*-
import os
import re
import random
from ..base import *


VOICE_PATTERN = r'href="sound:\/\/([\w\/]+%s\/\w*\.mp3)"'
VOICE_PATTERN_WQ = r'<span class="%s"><a href="sound://([\w/]+\w*\.mp3)">(.*?)</span %s>'
MAPPINGS = [
    ['br', [re.compile(VOICE_PATTERN % r'breProns')]],
    ['us', [re.compile(VOICE_PATTERN % r'ameProns')]]
]
LANG_TO_REGEXPS = {lang: regexps for lang, regexps in MAPPINGS}
DICT_PATH = u'/Users/brian/Documents/LDOCE5++ V 2-15/LDOCE5++ V 2-15.mdx' # u'E:\\BaiduYunDownload\\mdx\\L6mp3.mdx'


@register([u'本地词典-LDOCE5++', u'MDX-LDOCE5++'])
class Ldoce5(MdxService):

    def __init__(self):
        dict_path = DICT_PATH
        # if DICT_PATH is a path, stop auto detect
        if not dict_path:
            from ...service import service_manager, service_pool
            for clazz in service_manager.mdx_services:
                service = service_pool.get(clazz.__unique__)
                title = service.builder._title if service and service.support else u''
                service_pool.put(service)
                if title.startswith(u'LDOCE5'):
                    dict_path = service.dict_path
                    break
        super(Ldoce5, self).__init__(dict_path)

    @property
    def title(self):
        return getattr(self, '__register_label__', self.unique)

    def _fld_voice(self, html, voice):
        """获取发音字段"""
        for regexp in LANG_TO_REGEXPS[voice]:
            match = regexp.search(html)
            if match:
                val = '/' + match.group(1)
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

    @export([u'例句加音频', u'Examples with audios'])
    def fld_sentence_audio(self):
        return self._range_sentence_audio([i for i in range(0, 100)])

    @export([u'随机例句加音频', u'Random example with audio'])
    def fld_random_sentence_audio(self):
        return self._range_sentence_audio()

    @export([u'首2个例句加音频', u'First 2 examples with audios'])
    def fld_first2_sentence_audio(self):
        return self._range_sentence_audio([0, 1])

    # def _fld_audio(self, audio):
    #     val = '/' + audio
    #     name = get_hex_name('mdx-'+self.unique.lower(), val, 'mp3')
    #     name = self.save_file(val, name)
    #     if name:
    #         return self.get_anki_label(name, 'audio')
    #     return ''
    #
    # def _range_sentence_audio(self, range_arr=None):
    #     # m = re.findall(r'<div class="EXAMPLE"><a class="speaker exafile fa fa-volume-up" href="sound:\/\/media\/english\/exaProns\/\S+\.mp3" title="Play Example"> <\/a><span class="english LDOCE_switch_lang switch_children">.*?<div class="cn_txt">.*?<\/div><\/span><\/div>', self.get_html())
    #     m = re.findall(r'<div class="EXAMPLE"><a class=".*?" href="sound:\/\/media\/english\.*?\S+\.mp3".*?> <\/a><span class=.*?>.*?<div class="cn_txt">.*?<\/div><\/span><\/div>', self.get_html())
    #
    #     if m:
    #         range_arr = range_arr if range_arr else [random.randrange(0, len(m) - 1, 1)]
    #         my_str = ''
    #         mp3 = ''
    #         for i, i_str in enumerate(m):
    #             if i in range_arr:
    #                 # sound = re.search(r'href="sound:\/\/([\w\/]+\S*\.mp3)"', i_str)
    #                 # mp3 = self._fld_audio(sound)
    #                 # i_str = re.sub(r'<a class="speaker exafile fa fa-volume-up" href="sound:\/\/[\w\/]+\S*\.mp3" title="Play Example"> <\/a>', '', i_str).strip()
    #                 my_str = my_str + '<li>' + i_str + ' ' + mp3 + '</li>'
    #
    #         return self.get_html()
    #     return ''
