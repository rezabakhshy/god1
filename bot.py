from pyrogram import Client,filters
from random import randint
from gtts import gTTS
import requests,time,shutil
import os
from googletrans import Translator
from typing import Text
import googlesearch
app = Client("my_accound",api_id=13893053,api_hash="f586d92837b0f6eebcaa3e392397f47c")

@app.on_message((filters.me) & filters.regex("^!srch "))
def gif(client,message):
    text=message.text
    text=text[6:]
    result=googlesearch.search(text,num_results=30)
    tex=""
    for i in range(1,19):
        tex+=result[i]+"\n\n__________________________________\n\n"
    client.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=tex)

@app.on_message(filters.regex("^!trans ") & filters.me)
def ocr(client,message):
    text=message.reply_to_message.text
    text2=message.text
    text2=text2.replace("!trans ","")
    dest=text2.split()[0]
    translator = Translator()
    result = translator.translate(text,dest=dest)
    client.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=result.text)

@app.on_message(filters.regex("^!tts$") &  filters.me)
def tts(client,message):
    chat_id=message.chat.id
    message_id=message.message_id
    text = message.reply_to_message.text
    language="en"
    myobj=gTTS(text=text,lang=language,slow=False)
    myobj.save("test.ogg")
    client.send_audio(chat_id,"test.ogg",reply_to_message_id=message_id)
    os.remove('test.ogg')



@app.on_message((filters.me) & filters.regex("^! "))
def small_write(client, message):
    text=message.text
    chat_id=message.chat.id
    tex=""
    text=text.replace("! ","")
    x=len(text)
    i=0
    while text[i]!='.':
        if text[i]=="\n":
            i=i+1
            tex+="\n" +text[i]
            i=i+1
        if text[i]!=" ":
            tex+=text[i]
            i=i+1
        else:
            tex+=text[i]
            i=i+1
            tex+=text[i]
            i=i+1
        time.sleep(0.2)
        client.edit_message_text(chat_id,message_id=message.message_id,text=tex)

@app.on_message((filters.me) & filters.regex("^!vazhe "))
def vazhe(client,message):
    text=message.text
    chat_id=message.chat.id
    name=text.replace("!vazhe ","")
    Response=requests.post(f"https://api.codebazan.ir/vajehyab/?text={name}")
    tex=Response.json()
    fa=tex["result"]["fa"]
    en=tex["result"]["en"]
    moein=tex["result"]["Fmoein"]
    deh=tex["result"]["Fdehkhoda"]
    mo=tex["result"]["motaradefmotezad"]
    text=f"**فارسی کلمه:** `{fa}`\n**تلفظ کلمه: ** `{en}`\n\n**معنی کلمه در فرهنگ لغت معین: ** `{moein}`\n\n**معنی کلمه در فرهنگ لغت دهخدا: ** `{deh}`\n\n**مترادف و متضاد کلمه: ** `{mo}`"
    client.edit_message_text(chat_id,message_id=message.message_id,text=text)

@app.on_message((filters.me) & filters.regex("^!logo "))
def logo2(client,message):
    text=message.text
    chat_id=message.chat.id
    name=text.replace("!logo ","")
    num=randint(58,109)
    Response=requests.post(f"https://api.codebazan.ir/ephoto/writeText?output=image&effect=create-online-black-and-white-layerlogo-{num}.html&text={name}")
    with open("logo2.jpg","wb") as f:
        f.write(Response.content)   
    client.send_photo(chat_id,"logo2.jpg",reply_to_message_id=message.message_id)
    os.remove("logo2.jpg")

@app.on_message((filters.me) & filters.regex("^!num "))
def numtofa(client,message):
    text=message.text
    chat_id=message.chat.id
    nume=text.replace("!num ","")
    Response=requests.post(f"https://api.codebazan.ir/num/?num={nume}")
    tex=Response.json()
    client.edit_message_text(chat_id,message_id=message.message_id,text=tex["result"]["num"])

@app.on_message((filters.me) & filters.regex("^!pdf "))
def webtopdf(client,message):
    text=message.text
    chat_id=message.chat.id
    name=text.replace("!pdf ","")
    tex=name[0:5]
    if tex=="https":
        name=name[8:]
        url1="https://"+name
    if tex=="http:":
        name=name[7:]
        url1="http://"+name
    Response=requests.post(f"https://api.codebazan.ir/htmltopdf/?type=json&url={url1}")
    tex=Response.json()
    url=tex["result"]["url"]
    pdf=requests.get(url)
    time.sleep(3)
    namefile="test.pdf"
    with open("webtopdf.pdf","wb") as f:
        f.write(pdf.content)
    client.send_document(chat_id,"webtopdf.pdf",reply_to_message_id=message.message_id)
    os.remove("webtopdf.pdf")

@app.on_message((filters.me) & filters.regex("^!proxy$"))
def proxy(client,message):
    messag_id=message.message_id
    Response=requests.post("http://api.codebazan.ir/mtproto/json/") 
    tex=Response.json()
    tex=tex["Result"]
    text=""
    for i in range(0,20):
        server=tex[i]["server"]
        port=tex[i]["port"]
        secret=tex[i]["secret"]
        text+=f"{i+1}- https://t.me/proxy?server={server}&port={port}&secret={secret}\n\n/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/\n"
    client.edit_message_text(chat_id=message.chat.id,message_id=messag_id,text=text)

@app.on_message((filters.me) & filters.regex("^!pass "))
def password_gen(client,message):
    text=message.text
    messag_id=message.message_id
    name=text.replace("!pass ","")
    Response=requests.post(f"http://api.codebazan.ir/password/?length={name}")
    client.edit_message_text(chat_id=message.chat.id,message_id=messag_id,text=Response.text)

@app.on_message((filters.me) & filters.regex("^!. "))
def strrev(client,message):
    text=message.text
    messag_id=message.message_id
    name=text.replace("!. ","")
    Response=requests.post(f"http://api.codebazan.ir/strrev/?text={name}") 
    client.edit_message_text(chat_id=message.chat.id,message_id=messag_id,text=Response.text)

@app.on_message((filters.me) & filters.regex("^!arz$"))
def arz(client,message):
    messag_id=message.message_id
    Response=requests.post("http://api.codebazan.ir/arz/?type=arz")
    tex=Response.json()
    result=""
    for i in range(0,15):
        name=tex[i]["name"]
        price=tex[i]["price"]
        change=tex[i]["change"]
        percent=tex[i]["percent"]
        result+=f"**name:**{name}\n**price:**{price}\n**change:**{change}{percent}\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n"
    client.edit_message_text(chat_id=message.chat.id,message_id=messag_id,text=result)

@app.on_message((filters.me) & filters.regex("^!font "))
def font(client,message):
    text=message.text
    messag_id=message.message_id
    text=text.replace("!font ","")
    Response=requests.post(f"http://api.codebazan.ir/font/?text={text}")
    tex=Response.json()
    result=""
    for i in tex["result"]:
        font=tex["result"][i]
        result+=f"**{i}:**`{font}`\n\n"
    client.edit_message_text(chat_id=message.chat.id,message_id=messag_id,text=result)
     
@app.on_message((filters.me) & filters.regex("^!fontfa "))
def font(client,message):
    text=message.text
    messag_id=message.message_id
    text=text.replace("!fontfa ","")
    Response=requests.post(f"https://api.codebazan.ir/font/?type=fa&text={text}")
    tex=Response.json()
    result=""
    for i in tex["Result"]:
        font=tex["Result"][i]
        result+=f"**{i}:**`{font}`\n"
    client.edit_message_text(chat_id=message.chat.id,message_id=messag_id,text=result)

@app.on_message((filters.me) & filters.regex("^!ttr "))
def ttr(client,message):
    text=message.reply_to_message.text
    tex=message.text
    chat_id=message.chat.id
    language=tex.replace("!ttr ","")
    myobj=gTTS(text=text,lang=language,slow=False)
    myobj.save("testvoice.ogg")
    client.send_audio(chat_id,"testvoice.ogg",reply_to_message_id=message.message_id)
    os.remove('testvoice.ogg')

@app.on_message((filters.me) & filters.regex("^!bio$"))
def biografi(client,message):
    Response=requests.post("https://api.codebazan.ir/bio")
    text=Response.text
    client.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=text)

@app.on_message((filters.me) & filters.regex("^!newyear$"))
def newyear(client,message):
    response=requests.post("https://api.codebazan.ir/new-year")
    tex=response.json()
    text=""
    day=tex["day"]
    text+=f"{day} روز و"
    hour=tex["hour"]
    text+=f"{hour} ساعت و"
    min=tex["min"]
    text+=f"{min} دقیقه و"
    sec=tex["sec"]
    text+=f"{sec} ثانیه دیگر تا نوروز مانده است."
    client.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=text)

@app.on_message((filters.me) & filters.regex("^!saadi$"))
def ghazalsaadi(client,message):
    response=requests.post(f"https://api.codebazan.ir/ghazalsaadi/?type=json&id={randint(0,637)}")
    tex=response.json()
    title=tex["title"]
    cont=tex["contents"]
    text=f"**عنوان: ** `{title}`\n**غزل: **`{cont}`"
    client.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=text)

@app.on_message((filters.me) & filters.regex("!del$"))
def gif(client,message):
    message_id=message.message_id
    chat_id=message.chat.id
    client.delete_messages(chat_id,message_id)
    message_id=message.reply_to_message.message_id
    client.delete_messages(chat_id,message_id)

@app.on_message((filters.me) & filters.regex("^!gif "))
def gif(client,message):
    text=message.text
    chat_id=message.chat.id
    messag_id=message.message_id
    name=text.replace("!gif ","")
    response=requests.post(f"https://api.codebazan.ir/image/?type=gif&text={name}")
    text1=response.json()
    url=text1[f"giflink{randint(1,11)}"]
    gif=requests.get(url)
    with open(f"{name}.gif","wb") as f:
        f.write(gif.content)
    client.send_animation(chat_id,f"{name}.gif",reply_to_message_id=messag_id)
    os.remove(f"{name}.gif")

@app.on_message((filters.me) & filters.regex("^!card$"))
def visacard(client,message):
    response=requests.post(f"https://api.codebazan.ir/visa-card/")
    text=response.json()
    i=randint(0,11)
    name=text["Result"][i]["name"]
    lastname=text["Result"][i]["lastname"]
    adress=text["Result"][i]["Address"]
    city=text["Result"][i]["City"]
    state=text["Result"][i]["State"]
    post=text["Result"][i]["Postalcode"]
    country=text["Result"][i]["Country"]
    birthday=text["Result"][i]["birthday"]
    cardtype=text["Result"][i]["cardtype"]
    number=text["Result"][i]["cardnumber"]
    cvv2=text["Result"][i]["CVV2"]
    expire=text["Result"][i]["Expirationdate"]
    result=f"**name:** `{name}`\n**lastname:** `{lastname}`\n**address:** `{adress}`\n**city:** `{city}`\n**state:** `{state}`\n**postalcode:** `{post}`\n**country:** `{country}`\n**birthday:** `{birthday}`\n**cardtype:** `{cardtype}`\n**cardnumber:** `{number}`\n**cvv2:** `{cvv2}`\n**Expirationdate:** `{expire}`"
    client.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=result)


@app.on_message((filters.me) & filters.regex("^!meli"))
def meli(client,message):
    text=message.text
    code=text.replace("!meli ","")
    Response=requests.post(f"https://api.codebazan.ir/codemelli/?code={code}")
    tex=Response.json()
    client.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=tex["Result"])

@app.on_message((filters.me) & filters.regex("^!air "))
def air(client,message):
    text=message.text
    city=text.replace("!air ","")
    Response=requests.post(f"https://api.codebazan.ir/weather/?city={city}")
    tex=Response.json()
    ostan=tex["result"]["استان"]
    shahr=tex["result"]["شهر"]
    dama=tex["result"]["دما"]
    sorat=tex["result"]["سرعت باد"]
    vaziat=tex["result"]["وضعیت هوا"]
    fdama=tex["فردا"]["دما"]
    fvaziat=tex["فردا"]["وضعیت هوا"]
    text=f"**استان: ** {ostan}\n**شهر: ** {shahr}\n**          امروز **\n**دما: ** {dama}\n**سرعت باد: ** {sorat}\n**وضعیت هوا: ** {vaziat}\n\n      **فردا **\n**دما: ** {fdama}\n**وضعیت هوا: ** {fvaziat}"
    client.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=text)

@app.on_message((filters.me) & filters.regex("!down "))
def gif(client,message):
    text=message.text
    url=text[6:]
    response=requests.get(url)
    size=int(response.headers["content-length"])/1024/1024
    size=str(size)[:5]
    file_name=os.path.basename(url)
    with open(file_name,"wb") as f:
        shutil.copyfileobj(response.content,f)
    message_id=message.message_id
    chat_id=message.chat.id
    client.send_document(chat_id,file_name,caption=f"\n**NAME:** {file_name}\n**SAIZE:** {size} MB")
    os.remove(file_name)


@app.on_message((filters.me) & filters.regex("^!help$"))
def help(client,message):
    help=""
    help+="**command:**\n!down \n**descriptin:**\nget lonk download and upload to telegram\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+="**command:**\n!del \n**descriptin:**\nget rep;y message and delete message\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+="**command:**\n!srch \n**descriptin:**\nget text and show result search\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+="**command:**\n!trans \n**descriptin:**\nget text and source language and defective language so print trtanslate\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+="**command:**\n!tts \n**descriptin:**\nget text and send voice text to language english \n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+="**command:**\n! \n**descriptin:**\nget text and print it slowly\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+="**command:**\n!air\n**descriptin:**\nget city and send climatic condition\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+="**command:**\n!meli\n**descriptin:**\nsend result sending code meli\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+="**command:**\n!card\n**descriptin:**\nsend credit card\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+="**command:**\n!gif\n**descriptin:**\nget string and send gif withe string\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+="**command:**\n!saadi\n**descriptin:**\nsend one lyric from saadi\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+="**command:**\n!newyear\n**descriptin:**\nsend remaining amount until nowruz\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+="**command:**\n!bio\n**descriptin:**\nsend one bio\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+="**command:**\n!vazhe\n**descriptin:**\nget word prsion and send meaning\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+="**command:**\n!num\n**descriptin:**\nget number and send number to persion\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+="**command:**\n!.\n**descriptin:**\nget string and send strrev\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+="**command:**\n!arz\n**descriptin:**\nsend list from name , price and change currency\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+="**command:**\n!font\n**descriptin:**\nget name or any thing and send difrent fonts\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+="**command:**\n!fontfa\n**descriptin:**\nget persion text and send difrent font\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+="**command:**\n!logo\n**descriptin:**\nget text and send logo withe text\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+="**command:**\n!ttr\n**descriptin:**\nget language and text so send voice text withe input language \n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+="**command:**\n!pdf\n**descriptin:**\nget link web and send pdf shot web \n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+="**command:**\n!proxy\n**descriptin:**\nsend 20 MTproxy for telegram\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+="**command:**\n!pass\n**descriptin:**\nget number and genereat password to len number\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    client.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=help)
app.run()  # Automatically start() and idle()
