# randomWallpaper

[简体中文](https://github.com/ruxia-TJY/randomWallpaper/blob/master/README_cn.md)

[![](https://img.shields.io/badge/language-Python3-blue)](https://www.python.org/) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ruxia-TJY/randomWallpaper) ![linux](https://img.shields.io/badge/-ubuntu-yellow?logo=ubuntu) ![Windows](https://img.shields.io/badge/-windws-blue?logo=windows) ![License](https://img.shields.io/badge/License-MIT-blue)


Randomly select a picture from the folder list as wallpaper.

## install

### clone and run
clone this repositories use python3 or pack it.

*Notes:* if you run it in Windows,you need install packages with requirements.txt first, if you run in Linux,just run it.


### executable in release
I just use pyinstaller to pack it on Ubuntu20.04 x64.
you can download file from release,unzip and run `install.sh`. it will copy executable file to `~/.local/bin/` and create randomWallpaper.desktop file to `~/.local/share/applications/`

## how to use
run it without arguments. program will run as config.json.

Although the program supports running all the time and switching wallpapers at intervals, I recommend using `cron` in linux.

### argments

`-a,--add`, add folder which program choose in when it run. split by ',' or space

`-c,--config`,  config it by console

`-d,--delete`, delete wallpaper folder,split by ',' or space.

`--desktop`, create randomWallpaper.desktop to ~/.local/share/applications

`-h,--help`, show help

`-k,--keep`,run and keep not quit,change Wallpaper by 'keep-time'(s) in config.json,

`-l,--list`, print forder list

`-n,--clean`,clean wallpaper folder

`-q,--quit`, quit,only in use `-k,--keep` need it

`-r,--run`, run with config.json

`-v,--version`, version

## License
MIT,Thanks!