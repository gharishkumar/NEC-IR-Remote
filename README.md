# NEC-IR-Remote
1. Install `keyboard` module 
    ```
    sudo pip3 install keyboard
    ```
1. Install `colour emoji`
    ```
    mkdir ~/tmp
    cd tmp
    wget https://fontsdata.com/zipdown-segoeuiemoji-132714.htm 
    wget https://noto-website.storage.googleapis.com/pkgs/NotoColorEmoji-unhinted.zip
    mv zipdown-segoeuiemoji-132714.htm segoeuiemoji.zip
    unzip segoeuiemoji.zip
    unzip NotoColorEmoji-unhinted.zip
    mkdir /home/pi/.fonts &>/dev/null
    mv seguiemj.ttf "/home/pi/.fonts/Segoe UI.ttf"
    mv NotoColorEmoji.ttf "/home/pi/.fonts/Noto Color Emoji.ttf"
    fc-cache -f -v &>/dev/null
    rm -r ~/tmp
    cd
    ```
1. Run & check

    Clone this repo
    
    ```
    sudo python3 IR-remote.py
    ```

    Open chrome - [gharishkumar.github.io/min-vision-chart](https://gharishkumar.github.io/min-vision-chart)
