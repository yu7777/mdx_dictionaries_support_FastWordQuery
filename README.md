# FastWordQuery mdx dictionaries support   
A collection of files for mdx dictionaries support   


# Ldoce5++   
Tested on LDOCE5++ V 2-15

## Usage.  
You need put corresponding py files to FastWordQuery's serivce/dict folder.    
Find corresponding mdx and mdd files. (LDOCE5++ V 2-15.mdx and LDOCE5++ V 2-15.mdd).  
Then modify DICT_PATH in LDOCE5.py
```python
DICT_PATH = u'/Users/brian/Documents/LDOCE5++ V 2-15/LDOCE5++ V 2-15.mdx'
```

## Features
Extract word pronunciation (audio, Bre and Ame)

Extract sentence examples (example audio + English text)   

## Screen Shot
<img src="https://github.com/yu7777/Ldoce5--/blob/master/Screen%20Shot%202019-09-16%20at%2011.37.49%20am.png">




## Other mdx dictionaries    
lgmcw_Sound++   
Sound   
The Little Dict     
牛津高阶双解(第9版)  

## To do list.  
I am planning to work on 韦氏,牛津10,朗文6++ next.  
waiting for mw_core.mdd file.:smiley::smiley::smiley:
      
      
#            
- - -
- - -
```python
The following script is only for Wordquery addon
```
- - -

# WordQuery-dict.   
简明英汉字典   
欧陆例句词典    
    
        
EPFD2017.mdx 词组词频词典。  

Usage:    
put EPFD2017.py file into     
```python
Anki2/addons/wquery/service/
```
Note that this path is for wordquery add-on, not for fastwq add-on.   
You need change dictionary path yourself in this file.  

Feature:    
extract frequency of word group and put it into designated anki card field.
