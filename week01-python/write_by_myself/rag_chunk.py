from pathlib import Path
from rag_def import read_chunks_file,split_by_blank_line,clean_chunks,search_chunks,prompt_demo
from chat_def import chat




# 退到 week01-python 文件夹
FILE_DIR = Path(__file__).resolve().parent.parent
# 文档
file_path = FILE_DIR.parent / "knowledge" / "林冲.md"

def main():
    text = read_chunks_file(file_path)
    if text == None:
        print("文件不存在")
        return
    if text == False:
        print("请检查路径是否正确")
        return
    chunks = split_by_blank_line(text)
    chunks = clean_chunks(chunks,min_len = 30)
    # show all chunks
    # for i,c in enumerate(chunks):
    #     print(f"chunk{i + 1}|len={len(c)}")
    #     print(c[:15])
    key_words_score = search_chunks(chunks,"林冲的妻子是谁？",top_n=3)
    prompt_test = prompt_demo(key_words_score, '林冲的妻子是谁？')
    answer_test = chat(prompt_test)
    print(answer_test)

if __name__ == "__main__":
    main()