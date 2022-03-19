# randomWallpaper

[简体中文](https://github.com/ruxia-TJY/randomWallpaper/blob/master/README_cn.md)

[![](https://img.shields.io/badge/language-Python3-blue)](https://www.python.org/) 
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ruxia-TJY/randomWallpaper) 
![linux](https://img.shields.io/badge/-ubuntu-yellow?logo=ubuntu)  
![License](https://img.shields.io/badge/License-MIT-blue)



Randomly select a picture from the folder list as wallpaper.

I use this command:

```shell
DISPLAY=:0 GSETTINGS_BACKEND=dconf gsettings set org.gnome.desktop.background picture-uri  'file://image-path'
```

## install
I use pyinstaller to pack it on Ubuntu20.04 x64.
you can download file from release,
run install.sh. it will copy executable file to ~/.local/bin/ and create randomWallpaper.desktop file to ~/.local/share/applications/

or clone this repositories use python3 or pack it.

code use the python3 standard library.


## how to use
run it without arguments. program will run as config.json.

### argments
``-r,--run``, run with config.json

``-c,--config``,  config it by console

``-a,--add``, add folder which program choose in when it run. split by ',' or space

``-d,--delete``, delete wallpaper folder,split by ',' or space.

``--desktop``, create randomWallpaper.desktop to ~/.local/share/applications

``-n,--clean``,clean wallpaper folder

``-v,--version``, version

``-l,--list``, print forder list

``-h,--help``, show help

## License
MIT,Thanks!