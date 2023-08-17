# -*- coding:utf-8 -*-
# @Author: Pupper.cheng
# @Email : pupper.cheng@gmail.com

import json
import time

import translators as ts
from libs.TranslateYoudao import youdaoTranslate


def fileComparison(en_file, standard_file, zh_file):
    """
    中英文 文件对比
    :param en_file: 英文文件
    :param standard_file: 基准文件
    :param zh_file: 中文文件
    """
    with open(en_file, "r", encoding="utf-8") as en, open(standard_file, "r", encoding="utf-8") as standard:
        en_str = en.read()
        en_dict = json.loads(en_str)

        standard_str = standard.read()
        standard_dict = json.loads(standard_str)

    en_dict["languageOption"]["label"] = "简体中文"
    en_dict["languageOption"]["value"] = "zh-CN"

    for i in en_dict.keys():
        for j in en_dict[i].keys():
            if j not in standard_dict[i].keys():
                print(f"原始数据：【{j} : {en_dict[i][j]}】")
                zh_str = translate(en_dict[i][j])
                # zh_str = youdaoTranslate(en_dict[i][j])
                en_dict[i][j] = zh_str
                print(f"翻译后数据：【{j} : {en_dict[i][j]}】")
            else:
                en_dict[i][j] = standard_dict[i][j]

    with open(zh_file, "w", encoding="utf-8") as zh:
        zh.truncate(0)
        zh.write(json.dumps(en_dict, ensure_ascii=False))


def translate(string, translator="baidu", from_language="en", to_language="zh"):
    time.sleep(1)
    try:
        return ts.translate_text(string, translator=translator, from_language=from_language, to_language=to_language)
    except Exception as e:
        print(f"翻译程序错误：{e}")
        return string


if __name__ == '__main__':
    fileComparison("../data/strings-7.1.0.json", "../strings-9.7.1-zh.json", "../strings-7.1.0-zh.json")
