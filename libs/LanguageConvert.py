# -*- coding:utf-8 -*-
# @Author: Pupper.cheng
# @Email : pupper.cheng@gmail.com
import json

from zhconv import convert


def convert_tw_cn(tw_file, cn_file):
    """
    繁简转换
    :param tw_file: 繁体文件
    :param cn_file: 简体文件
    """
    with open(tw_file, "r+", encoding="utf-8") as f_tw, open(cn_file, "w", encoding="utf-8") as f_zh:
        tw_str = f_tw.read()
        zh_str = convert(tw_str, "zh-cn")

        zh_dict = json.loads(zh_str)
        zh_dict["languageOption"]["label"] = "简体中文"
        zh_dict["languageOption"]["value"] = "zh-CN"
        f_zh.truncate(0)
        f_zh.write(json.dumps(zh_dict, ensure_ascii=False))


if __name__ == '__main__':
    convert_tw_cn("../tw/strings7.5.0.json", "../strings.json")
