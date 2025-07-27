#!/usr/bin/env python3
"""
批量转换图片格式
批量修改文件名
"""
import os
from pathlib import Path
from PIL import Image
import subprocess

# 其他 转 jpg
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

# 批量重命名
def rename_files(directory):
    # 获取指定目录下的所有文件
    files = os.listdir(directory)
    # 按文件名排序（确保文件顺序一致）
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
            # 生成新的文件名，格式为 01.xxx、02.xxx 等
            new_filename = f"{counter:02d}{file_extension}"
            # 生成新的文件路径
            new_file_path = os.path.join(directory, new_filename)
            # 检查目标文件名是否已经存在
            while os.path.exists(new_file_path):
                counter += 1
                new_filename = f"{counter:02d}{file_extension}"
                new_file_path = os.path.join(directory, new_filename)
            # 重命名文件
            os.rename(file_path, new_file_path)
            print(f"Renamed {filename} to {new_filename}")
            # 增加计数器
            counter += 1

# 其他 转 mp3
def convert_audio_to_mp3(directory):
    # 获取指定目录下的所有文件
    files = os.listdir(directory)
    # 定义支持的音频文件扩展名
    supported_extensions = {".wav", ".aac", ".flac", ".ogg", ".wma", ".m4a", ".alac"}
    for filename in files:
        # 获取文件的扩展名
        file_extension = os.path.splitext(filename)[1].lower()
        # 检查文件是否是支持的音频文件且不是 .mp3
        if file_extension in supported_extensions:
            # 获取文件的完整路径
            file_path = os.path.join(directory, filename)
            # 生成新的文件名（替换扩展名为 .mp3）
            new_filename = os.path.splitext(filename)[0] + '.mp3'
            new_file_path = os.path.join(directory, new_filename)
            # 构造 ffmpeg 命令
            command = [
                "ffmpeg",
                "-i", file_path,  # 输入文件
                "-codec:a", "libmp3lame",  # 使用 MP3 编码器
                "-qscale:a", "2",  # 设置音频质量（2 是推荐值，数值越小质量越好，文件越大）
                new_file_path  # 输出文件
            ]
            # 执行 ffmpeg 命令
            try:
                subprocess.run(command, check=True)
                print(f"Converted {filename} to {new_filename}")
                # 删除原始文件
                os.remove(file_path)
                print(f"Deleted original file: {filename}")
            except subprocess.CalledProcessError as e:
                print(f"Failed to convert {filename}: {e}")
            except Exception as e:
                print(f"Failed to delete {filename}: {e}")


def image():
    os.chdir('./bg') #修改工作目录到bg文件夹
    directory = "."
    convert_images_to_jpg(directory)
    rename_files(directory)  


def music():
    os.chdir('./music') #修改工作目录到music文件夹
    directory = "."
    convert_audio_to_mp3(directory)
    rename_files(directory)

# 设置要处理的目录
if __name__ == "__main__":
    music()  # 处理音频
    # image()  # 处理图片
