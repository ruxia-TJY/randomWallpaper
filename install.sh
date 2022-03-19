echo Start Install randomWallpaper

# copy file
echo copy randomWallpaper to ~/.local/bin

cp randomWallpaper ~/.local/bin

echo copy Wallpaper.png to ~/.local/bin
cp randomWallpaper_logo ~/.local/bin


echo create randomWallpaper.desktop to ~/.local/bin/randomWallpaper
~/.local/bin/randomWallpaper --desktop

echo Install successful
