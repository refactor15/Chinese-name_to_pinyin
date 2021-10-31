from pypinyin import lazy_pinyin


def name_to_pinyin(str, order=0, caps=0, sep=""):
    """
	必选参数为汉字的字符串，可选参数切换输出的格式。
	order默认为0，姓在前，名在后，order设为1，姓在后，名在前
	caps默认为0，姓和名首字母大写，caps设为1，姓全字母大写
	caps设为2，姓和名全字母大写
	sep为名中各汉字之间的分隔符，默认为空
	"""
    every_word = lazy_pinyin(str)  # 每个汉字的全小写拼音
    han_fuxing = """百里 北堂 北野 北宫 辟闾 淳于 成公 陈生 褚师 端木 东方 东郭 东野 东门 第五 
	大狐 段干 段阳 带曰 第二 东宫 公孙 公冶 公羊 公良 公西 公孟 高堂 高阳 公析 公肩 
	公坚 郭公 谷梁 毌将 公乘 毌丘 公户 公广 公仪 公祖 皇甫 黄龙 胡母 何阳 夹谷 九方 
	即墨 梁丘 闾丘 洛阳 陵尹 冷富 龙丘 令狐 林彭 南宫 南郭 女娲 南伯 南容 南门 南野 
	欧阳 欧侯 濮阳 青阳 漆雕 亓官 渠丘 壤驷 上官 少室 少叔 司徒 司马 司空 司寇 士孙 
	申屠 申徒 申鲜 申叔 夙沙 叔先 叔仲 侍其 叔孙 澹台 太史 太叔 太公 屠岸 唐古 闻人 
	巫马 微生 王孙 无庸 夏侯 西门 信平 鲜于 轩辕 相里 新垣 羊舌 羊角 延陵 於陵 伊祁 
	吾丘 乐正 诸葛 颛孙 仲孙 仲长 钟离 宗政 主父 中叔 左人 左丘 宰父 长儿 仉督""".split()
    shao_fuxing = """单于 叱干 叱利 车非 独孤 大野 独吉 达奚 哥舒 赫连 呼延 贺兰 黑齿 斛律 斛粟 
	贺若 夹谷 吉胡 可频 慕容 万俟 抹捻 纳兰 普周 仆固 仆散 蒲察 屈突 屈卢 钳耳 是云 
	索卢 厍狄 拓跋 同蹄 秃发 完颜 宇文 尉迟 耶律 长孙""".split()
    if str[:2] in han_fuxing + shao_fuxing and len(str) > 2:
        every_word[0] += every_word.pop(1)
    if len(every_word) == 3:
        every_word[1] += sep + every_word.pop()
    elif len(every_word) == 4:
        every_word[1] += sep + every_word.pop(2)
        every_word[1] += sep + every_word.pop()
    assert len(every_word) == 2
    list0 = [w.capitalize() for w in every_word]
    if caps == 1:
        list0[0] = list0[0].upper()
    elif caps == 2:
        list0 = [x.upper() for x in list0]
    if order == 1:
        list0.reverse()
    return " ".join(list0)

with open("name_example.txt", "r", encoding="utf-8") as f:
    mingzi = [x.strip("\n") for x in f.readlines()]
with open("pinyin_example.txt", "w", encoding="utf-8") as g:
    for y in mingzi:
        g.write(name_to_pinyin(y, sep="-") + "\n")

