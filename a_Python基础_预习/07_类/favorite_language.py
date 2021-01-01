# 作者：蔡不菜
# 时间：2020/10/11 13:20

from collections import OrderedDict

favorite_languages = OrderedDict()
favorite_languages["jack"] = "汉语"
favorite_languages["may"] = "英语"
favorite_languages["张三"] = "日语"
favorite_languages["李四"] = "俄语"

for name, language in favorite_languages.items():
    print(name.title() + " 最喜欢的语言是：" + language.title())
