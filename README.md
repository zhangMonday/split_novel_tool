# split_novel_tool
一个将你的txt格式小说按章节拆分的工具 A tool for splitting your txt format novel by chapters.

将小说(txt格式)与程序放在同一目录下，编辑最后一行代码修改为小说文件名
确保原文本中包含关键字”第n章“（中文+阿拉伯数字），软件将自动按章节拆分小说并输出至同一目录下，并将文件命名为关键词”第n章“所在的同一行内容

例如，小说原文件里是这样的：
第1章 序言
xxxxx(第一章正文)

第2章 hallo world
xxxxx(第二章正文)

那么，第1章的文件名就应该是"第1章 序言"
第2章的文件名就应该是"第2章 hallo world"
