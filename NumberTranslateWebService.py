from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import math

class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            numeroUrl = int(self.path[1:])
            if numeroUrl == 0:
                numeroTraduzido = "zero"
            else:
                numeroTraduzido = Tradutor(numeroUrl)
            jsonTraduzido = { "extenso" : numeroTraduzido }
            x = json.dumps(jsonTraduzido,ensure_ascii=False)
            self.send_response(200,x)
        except:
            self.send_response(404,self.path[1:])
        self.end_headers()
    
def Tradutor(numero):
    result = ""
    if(numero < 0):
        result+='menos '+ Tradutor(abs(numero)) 
    elif(numero < 20):
        result+=TradutorUnidade(numero)
    elif(numero < 100):
        result+=TradutorDezena(numero)
    elif(numero < 1000):
        result+=TradutorCentena(numero)
    elif(numero < 100000):
        result+=TradutorMilhar(numero)
    else:
        return 'número fora do alcance'
    return result

def TradutorUnidade(numero):
    result = ''
    if numero == 1: 
        result+="um"
    elif numero == 2: 
        result+="dois"
    elif numero == 3:
        result+="três"
    elif numero == 4:
        result+="quatro"
    elif numero == 5:
        result+="cinco"
    elif numero == 6:
        result+="seis"
    elif numero == 7:
        result+="sete"
    elif numero == 8:
        result+="oito"
    elif numero == 9:
        result+="nove"
    elif numero == 10: 
        result+="dez"
    elif numero == 11:
        result+="onze"
    elif numero == 12:
        result+="doze"
    elif numero == 13:
        result+="treze"
    elif numero == 14:
        result+="catorze"
    elif numero == 15:
        result+="quinze"
    elif numero == 16:
        result+="dezesseis"
    elif numero == 17:
        result+="dezessete"
    elif numero == 18:
        result+="dezoito"
    elif numero == 19: 
        result+="dezenove"
    return result

def TradutorDezena(num):
    result = ""
    x = math.ceil(int(num/10))
    numero = math.ceil(x)
    if numero == 0:
        result=TradutorUnidade(num)
        return result
    elif numero == 2: 
        if num!=20:
            result+='vinte e {}'.format(Tradutor(num-20))
        else:
            result+='vinte'
    elif numero == 3:
        if num!=30:
            result+='trinta e {}'.format(Tradutor(num-30))
        else:
            result+='trinta'
    elif numero == 4:
        if num!=40:
            result+='quarenta e {}'.format(Tradutor(num-40))
        else:
            result+='quarenta'
    elif numero == 5:
        if num!=50:
            result+='cinquenta e {}'.format(Tradutor(num-50))
        else:
            result+='cinquenta'
    elif numero == 6:
        if num!=60:
            result+='sessenta e {}'.format(Tradutor(num-60))
        else:
            result+='sessenta'
    elif numero == 7:
        if num!=70:
            result+='setenta e {}'.format(Tradutor(num-70))
        else:
            result+='setenta'
    elif numero == 8:
        if num!=80:
            result+='oitenta e {}'.format(Tradutor(num-80))
        else:
            result+='oitenta'
    elif numero == 9:
        if num!=90:
            result+='noventa e {}'.format(Tradutor(num-90))
        else:
            result+='noventa'
    return result

def TradutorCentena(num):
    result = ""
    x = math.ceil(int(num/100))
    numero = math.ceil(x)
    if numero == 0:
        result=TradutorDezena(num)
    elif numero ==1:
        if num!=100:
            result+='cento e {}'.format(Tradutor(num-100))
        else:
            result+='cem'
    elif numero == 2: 
        if num!=200:
            result+='duzentos e {}'.format(Tradutor(num-200))
        else:
            result+='duzentos'
    elif numero == 3:
        if num!=300:
            result+='trezentos e {}'.format(Tradutor(num-300))
        else:
            result+='trezentos'
    elif numero == 4:
        if num!=400:
            result+='quatrocentos e {}'.format(Tradutor(num-400))
        else:
            result+='quatrocentos'
    elif numero == 5:
        if num!=500:
            result+='quinhentos e {}'.format(Tradutor(num-500))
        else:
            result+='quinhentos'
    elif numero == 6:
        if num!=600:
            result+='seissentos e {}'.format(Tradutor(num-600))
        else:
            result+='seissentos'
    elif numero == 7:
        if num!=700:
            result+='setecentos e {}'.format(Tradutor(num-700))
        else:
            result+='setecentos'
    elif numero == 8:
        if num!=800:
            result+='oitocentos e {}'.format(Tradutor(num-800))
        else:
            result+='oitocentos'
    elif numero == 9:
        if num!=900:
            result+='novecentos e {}'.format(Tradutor(num-900))
        else:
            result+='novecentos'
    return result

def TradutorMilhar(num):
    result = ""
    x = math.ceil(int(num/1000))
    numero = math.ceil(x)
    if numero == 0:
        result=TradutorCentena(num)
    else:
        if (num-numero*1000)>0:
            if numero!=1:
                result+='{} mil e {}'.format(Tradutor(numero),Tradutor(num-numero*1000))
            else:
                result+= 'mil e {}'.format(Tradutor(num-numero*1000))
        else:
            if numero!=1:
                result+='{} mil'.format(Tradutor(numero))
            else:
                result+='mil'
    return result

httpd = HTTPServer(('localhost', 8080), Serv)
httpd.serve_forever()