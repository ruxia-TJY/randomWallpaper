# randomWallpaper

[English](https://github.com/ruxia-TJY/randomWallpaper/blob/master/README.md)

[![](https://img.shields.io/badge/language-Python3-blue)](https://www.python.org/) 
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ruxia-TJY/randomWallpaper) 
![linux](https://img.shields.io/badge/-ubuntu-yellow?logo=ubuntu)  
![License](https://img.shields.io/badge/License-MIT-blue)

从文件夹列表中随机选择一张图片作为壁纸。

主要使用的命令
```shell
DISPLAY=:0 GSETTINGS_BACKEND=dconf gsettings set org.gnome.desktop.background picture-uri  'file://image-path'
```

## 安装
我在Ubuntu20.04 x64环境下使用Pyinstaller打包。
你可以直接从release界面下载。
运行install.sh。作用是将文件复制到~/.local/bin文件夹下，在~/.local/share/applications文件夹下创建randomWallpaper.desktop文件

或者直接clone本仓库，使用python3运行或者自己打包。

本代码使用标准库

## 使用
无命令行参数，会按照config.json的配置进行运行

### 参数列表

``-r,--run``, 按照config.json配置运行

``-c,--config``, 在命令行中运行

``-a,--add``, 添加壁纸文件夹到程序运行的选择列表中，输入多个文件夹通过`,`和空格分割。

``-d,--delete``,删除壁纸文件夹，输入多个文件夹通过','和空格分割

``--desktop``, 在~/.local/share/applications路径下创建randomWallpaper.desktop文件

``-n,--clean``, 清空壁纸文件夹

``-v,--version``, 版本号

``-l,--list``, 输出壁纸文件夹列表

``-h,--help``, 显示帮助

## 开源协议
MIT，感谢使用！