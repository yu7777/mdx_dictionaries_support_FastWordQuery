# Ldoce5++

Anki addon Fastwq 

Only tested on LDOCE5++ V 2-15.mdx

Extract word pronunciation (Bre and Ame)

Extract sentence examples (example audio + English text)
cn_text is removed by default. Plese comment out the following code if you want to keep cn_txt.
```python
i_str = re.sub(r'(<div class="cn_txt">\s*\S*<\/div>)<\/span>', '', i_str).strip()
```
Screen Shot
<img src="https://github.com/yu7777/Ldoce5--/blob/master/Screen%20Shot%202019-09-16%20at%2011.37.49%20am.png">
