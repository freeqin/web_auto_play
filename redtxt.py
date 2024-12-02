# 确定文件路径，这里以Windows系统为例，你需要根据实际情况修改
import os



desktop = os.path.join(os.path.expanduser("~"), "Desktop")
print(desktop)

try:
    # 打开文件，'r'表示以只读模式打开
    with open(desktop + "\\uid.txt") as file:
        # 读取文件内容并打印
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"文件 {desktop + '\\uid.txt'} 未找到，请检查路径是否正确。")
except Exception as e:
    print(f"读取文件时发生错误：{e}")