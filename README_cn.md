# randomWallpaper

[English](https://github.com/ruxia-TJY/randomWallpaper/blob/master/README.md)

[![](https://img.shields.io/badge/language-Python3-blue)](https://www.python.org/) 
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ruxia-TJY/randomWallpaper) 
![linux](https://img.shields.io/badge/-ubuntu-yellow?logo=ubuntu)
![Windows](https://img.shields.io/badge/-windws-blue?logo=windows)
![License](https://img.shields.io/badge/License-MIT-blue)

从文件夹列表中随机选择一张图片作为壁纸。

## 安装
我在Ubuntu20.04 x64环境下使用Pyinstaller打包。
你可以直接从release界面下载，解压并运行install.sh，会将文件复制到`~/.local/bin`文件夹下，在`~/.local/share/applications`文件夹下创建randomWallpaper.desktop文件

或者直接clone本仓库，使用python3运行或者自己打包。

代码仅使用Python3标准库

## 使用

无命令行参数，会按照config.json的配置进行运行

虽然程序支持一直运行并每隔一段时间更换壁纸，但我还是推荐在Linux上使用`cron`进行管理。

### 参数列表

`-a,--add`, 添加壁纸文件夹到程序运行的选择列表中，输入多个文件夹通过`,`和空格分割。

`-c,--config`, 在命令行中运行

`-d,--delete`,删除壁纸文件夹，输入多个文件夹通过','和空格分割

`--desktop`, 在~/.local/share/applications路径下创建randomWallpaper.desktop文件

`-h,--help`, 显示帮助

`-k,--keep`, 保持程序运行，并根据config.json的`keep-time`(s)切换壁纸

`-l,--list`, 输出壁纸文件夹列表

`-n,--clean`, 清空壁纸文件夹

`-q,quit`, 退出程序，仅在运行`-k,--keep`时才需要此选项进行退出

`-r,--run`, 按照config.json配置运行

`-v,--version`, 版本号

## 开源协议
MIT，感谢使用！