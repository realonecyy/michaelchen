import re

s = '''最简单易用的谷歌访问助手,为chrome扩展用户量身打造。可以解决chrome扩展无法自动更新的问题，
同时可以访问谷歌google搜索，gmail邮箱，google+等谷歌服务。
'''
l1 = re.findall('谷歌',s)
print(l1)     # ['谷歌', '谷歌', '谷歌']

l2 = re.findall('谷|歌',s)
print(l2)     # ['谷', '歌', '谷', '歌', '谷', '歌']

l3 = re.findall('g.',s)
print(l3)    # ['go', 'gl', 'gm', 'go', 'gl']

l4 = re.findall('[谷歌]',s)
print(l4)    # ['谷', '歌', '谷', '歌', '谷', '歌']

l5 = re.findall('[^ #!A-Z]',s)
print(l5)

l6 = re.findall('^最',s)
print(l6)     # ['最']
l61 = re.findall('^c',s)
print(l61)    # []

l7 = re.findall('Jame$','hi,Jame')   # $表示字符串的结尾位置是Jame
print(l7)    # ['Jame']

l8 = re.findall('^Jame$','Jame')
print(l8)    # ['Jame']

l9 = re.findall('wo*',"wooooo~~w!")
print(l9)    # ['wooooo', 'w']

s = '小明：18，小李：17，李世民：954'
l10 = re.findall('[0-9]*',s)
print(l10)


s = '''1号颜骏凌、2号贺惯、3号石柯、4号李磊、5号张琳芃、6号高准翼、7号武磊、
8号蒿俊闵、9号杨旭、10号郑智、11艾克森、12号张鹭、13号李可、14号池忠国、15号吴曦、
15号姚均晟、17号王刚、18号杨立瑜、19号韦世豪、20号张稀哲、21号李帅、22号朱辰杰、23号王大雷
'''
l11 = re.findall('张[^、]*|李[^、]*',s)
print(l11)


l12 = re.findall('[A-Z]+[a-z]*','Hello World，hello Python')
print(l12)

l13 = re.findall('lo?','Hello World，hello Python')
print(l13)

l14 = re.findall('-?[0-9]+','12 365 -10 -9')
print(l14)

l15 = re.findall('1[0-9]{10}',"Jame:13886495728")
print(l15)


l16 = re.findall('','fe80:0000:0000:0000:b831:c880:43c3:8b26')

# {n}  匹配前面的字符出现n次
l17 = re.findall('[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}','fc:aa:14:37:a9:91')
print(l17)

l18 = re.findall('[1-9][0-9]{4,10}','Dan:158717766')
print(l18)


# \d 匹配任意数字字符，\D 匹配任意非数字字符
l19 = re.findall('\d{1,5}',"Mysql: 3306, http:80")
print(l19)


