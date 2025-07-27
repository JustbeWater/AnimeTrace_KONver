#!/usr/bin/env python3
"""
批量转换图片格式
批量修改文件名
"""
import os
from pathlib import Path
from PIL import Image

# 其他转换为jpg
def convert_images_to_jpg(directory):
    print(f"Processing directory: {directory}")
    files = os.listdir(directory)
    print(f"Found {len(files)} files in the directory.")
    for filename in files:
        file_path = os.path.join(directory, filename)
        print(f"Processing file: {file_path}")
        if os.path.isfile(file_path) and filename.lower().endswith(('.png', '.bmp', '.gif', '.tiff', '.webp')):
            try:
                img = Image.open(file_path)
                img = img.convert('RGB')
                new_filename = os.path.splitext(file_path)[0] + '.jpg'
                img.save(new_filename, 'JPEG', quality=90)
                print(f"Converted {filename} to {os.path.basename(new_filename)}")
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")

# 批量修改文件名
def rename_files(directory):
    # 获取指定目录下的所有文件
    files = os.listdir(directory)
    # 按文件名排序（可选，确保文件顺序一致）
    files.sort()
    # 初始化计数器
    counter = 1
    for filename in files:
        # 获取文件的完整路径
        file_path = os.path.join(directory, filename)
        # 检查是否是文件
        if os.path.isfile(file_path):
            # 获取文件的扩展名
            file_extension = os.path.splitext(filename)[1]
            # 生成新的文件名，格式为 01, 02, 03 等
            new_filename = f"{counter:02d}{file_extension}"
            # 生成新的文件路径
            new_file_path = os.path.join(directory, new_filename)
            # 重命名文件
            os.rename(file_path, new_file_path)
            print(f"Renamed {filename} to {new_filename}")
            # 增加计数器
            counter += 1

# 设置要处理的目录
os.chdir('./bg') #修改工作目录到bg文件夹
directory = "."
# rename_files(directory)             # 重命名文件名字为 2 位宽整数
# convert_images_to_jpg(directory)    # 其他转换为jpg