import re

def split_chapters(filename):
    # 打开原始小说文件
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 使用正则表达式找出所有章节的标题
    chapter_titles = re.findall(r'第\d+章.*', content)
    
    # 根据章节标题分割文本
    chapters = re.split(r'(第\d+章.*)', content)[1:]
    
    # 确保章节标题和内容可以成对处理
    assert len(chapters) == len(chapter_titles) * 2, "章节标题和内容数量不匹配"
    
    # 遍历所有章节
    for i in range(0, len(chapters), 2):
        chapter_title = chapters[i].strip()
        chapter_content = chapters[i+1].strip()
        
        # 构建新的文件名，使用章节标题
        new_filename = f"{chapter_title}.txt"
        
        # 将章节内容写入新文件
        with open(new_filename, 'w', encoding='utf-8') as new_file:
            new_file.write(chapter_title + '\n' + chapter_content)
    
    print("所有章节已成功分割并保存。")

# 在这里修改同目录小说文件名
split_chapters("三体.txt")
