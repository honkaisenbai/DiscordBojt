import json
import os
import subprocess
try:
    import googletrans
except:
    subprocess.call("py -m pip install googletrans==3.1.0a0")
while True:
    print("Nội dung cần dịch?")
    text = str(input(">> "))
    print("Ngôn ngữ cần dịch?")
    dest = str(input(">> "))
    translator = googletrans.Translator()
    try:
        translated = translator.translate(text=text,dest=dest)
        print("Đã dịch xong!\n=> "+translated.text)
    except ValueError:
        if not os.path.isfile('langcodes.json'):
            with open('langcodes.json','w',encoding='utf-8') as f:
                f.write(f'{{}}')
            langcodes = json.load(open('langcodes.json','r',encoding='utf-8'))
            langcodes = googletrans.LANGCODES
            with open('langcodes.json','w',encoding='utf-8') as f:
                json.dump(langcodes,f,indent=4)
        print("Không rõ ngôn ngữ cần dịch!\nHãy mở file `langcodes.json` để biết rõ các mã ngôn ngữ được hỗ trợ")