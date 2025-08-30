#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    :2025/07/10 09:39:03
# @Author  :小 y 同 学
# @公众号   :小y只会写bug
# @CSDN    :https://blog.csdn.net/weixin_64989228?type=blog
# @Discript:改版自：


# 适用于isce2.5及以上版本
import os
import time
from datetime import datetime
import subprocess

# =====>2025/07/09 09:32:55 参数设置 <=====
start = 1  # todo 设置起始步骤

log_file = "auto_run.txt"
# if os.path.exists(log_file):
#     os.remove(log_file)


def add_wait(script_path):
    # =====>2025/07/08 17:47:49 在每个runfile后面添加wait，gpt编写 <=====
    content = ""
    with open(script_path, "r") as f:
        content = f.read().strip()
    if not content.endswith("wait"):
        content += "\nwait\n"
        with open(script_path, "w") as f:
            f.write(content)


def PrintInfo(message):
    s = f"{datetime.now().strftime('%Y.%m.%d-%H:%M:%S').ljust(30,'-')}{message}"
    with open(log_file, "a") as f:
        f.write(s + "\n")
    print(s)


def execute_script(script_path):
    start_time = time.time()
    PrintInfo(f"开始执行: {script_path}")
    try:
        subprocess.run(["bash", script_path, "wait"], check=True)
    except subprocess.CalledProcessError as e:
        PrintInfo(f"执行失败: {script_path}---错误: {e}")
    finally:
        end_time = time.time()
        PrintInfo(f"执行完毕: {script_path}---用时: {end_time - start_time:.2f} 秒")


start_time = time.time()
PrintInfo("读取文件")
# todo 读取run_files文件夹下的所有文件并挨个执行命令
fileList = os.listdir("./run_files")
for j in range(start, len(fileList) + 1):
    # for j in range(11, len(fileList) + 1):
    script = [i for i in fileList if f"{j:02d}" in i][0]
    add_wait(f"./run_files/{script}")
    execute_script(f"./run_files/{script}")

m, s = divmod(time.time() - start_time, 60)
PrintInfo("使用时间: {:02.0f} mins {:02.1f} secs".format(m, s))
PrintInfo(f"完成处理")
