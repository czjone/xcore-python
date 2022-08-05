from googletrans import Translator
translator = Translator()
print(translator.translate('这就是一条测试信息,还管是对还是不对', dest='ja').text)