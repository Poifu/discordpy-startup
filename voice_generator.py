import subprocess
import re

# remove_custom_emoji
# 絵文字IDは読み上げない
def remove_custom_emoji(text):
    pattern = r'<:[a-zA-Z0-9_]+:[0-9]+>'    # カスタム絵文字のパターン
    return re.sub(pattern,'',text)   # 置換処理

# urlAbb
# URLなら省略
def urlAbb(text):
    pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
    return re.sub(pattern,'URLは省略！',text)   # 置換処理

# creat_WAV
# message.contentをテキストファイルに書き込み
def creat_WAV(inputText):
        #message.contentをテキストファイルに書き込み
    input_file = 'input.txt'

    with open(input_file,'w',encoding='shift_jis') as file:
        file.write(inputText)

    command = '/open_jtalk/bin/open_jtalk -x {x} -m {m} -r {r} -ow {ow} {input_file}'

    #辞書のPath
    x = '/open_jtalk/bin/dic'

    #ボイスファイルのPath
    m = '/open_jtalk/bin/mei/mei_normal.htsvoice'

    #発声のスピード
    r = '1.0'

    #出力ファイル名　and　Path
    ow = 'output.wav'

    args= {'x':x, 'm':m, 'r':r, 'ow':ow, 'input_file':input_file}

    cmd= command.format(**args)
    print(cmd)

    subprocess.run(cmd)
    return True

if __name__ == '__main__':
    creat_WAV('テスト')
