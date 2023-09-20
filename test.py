# -*- coding: utf-8 -*-
import sys

def preprocess(text):
    # 去除标点符号和转换为小写字母
    text = text.replace(",", "").replace(".", "").replace("!", "").replace("?", "").lower()
    return text

def calculate_plagiarism_rate(orig_path, copy_path, answer_path):
    # 检查命令行参数数量
    

    with open(orig_path, 'r', encoding='utf-8') as orig_file, \
         open(copy_path, 'r', encoding='utf-8') as copy_file, \
         open(answer_path, 'w', encoding='utf-8') as answer_file:

        orig_text = orig_file.read()
        copy_text = copy_file.read()

        orig_text = preprocess(orig_text)
        copy_text = preprocess(copy_text)

        orig_words = [char for char in orig_path]#将句子分割成单个字
        copy_words = [char for char in copy_path] #将句子分割成单个字
        
        total_words = len(copy_words)
        same_words = 0
        print("orig_words:",orig_words)
        print("copy_words:",copy_words)
        for word in copy_words:
            if word in orig_words:
                same_words += 1

        plagiarism_rate = round(same_words / total_words, 2)

        answer_file.write(str(plagiarism_rate))


def main():
    if len(sys.argv) < 3:
        print("Please provide the required command line arguments.")
        return 
    orig_file = sys.argv[1]#原文文件的路径
    orig_add_file = sys.argv[2]#抄袭文件的路径
    ans_file=sys.argv[3]
    calculate_plagiarism_rate(orig_file,orig_add_file,ans_file)
    

if __name__ == "__main__":
    main()
