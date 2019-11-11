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
        result+=unidade.get(numero)
    elif(numero < 100):
        result+=TradutorDezena(numero)
    elif(numero < 1000):
        result+=TradutorCentena(numero)
    elif(numero < 100000):
        result+=TradutorMilhar(numero)
    else:
        return 'número fora do alcance'
    return result

unidade = {
    1: "um",
    2: "dois",
    3: "três",
    4: "quatro",
    5: "cinco",
    6: "seis",
    7: "sete",
    8: "oito",
    9: "nove",
    10: "dez",
    11: "onze",
    12: "doze",
    13: "treze",
    14: "catorze",
    15: "quinze",
    16: "dezesseis",
    17: "dezessete",
    18: "dezoito",
    19:  "dezenove"
}

dezena = {
    2: 'vinte',
    3: 'trinta',
    4: 'quarenta',
    5: 'cinquenta',
    6: 'sessenta',
    7: 'setenta',
    8: 'oitenta',
    9: 'noventa'
}

centena = {
    1: 'cem',
    2: 'duzentos',
    3: 'trezentos',
    4: 'quatrocentos',
    5: 'quinhentos',
    6: 'seissentos',
    7: 'setecentos',
    8: 'oitocentos',
    9: 'novecentos'
}

def TradutorDezena(num):
    result = ""
    numero = math.ceil(int(num/10))
    if numero == 0:
        result=unidade.get(num)
        return result
    elif num%(numero*10)==0:
        result+=dezena.get(numero)
        return result
    else:
        result+='{} e {}'.format(dezena.get(numero),Tradutor(num%(numero*10)))
    return result

def TradutorCentena(num):
    result = ""
    numero = math.ceil(int(num/100))
    if numero == 0:
        result=TradutorDezena(num)
    elif numero ==1:
        if num!=100:
            result+='cento e {}'.format(Tradutor(num-100))
        else:
            result+='cem'
    elif(num%(numero*100)==0):
        result+=centena.get(numero)
    else:
        result+='{} e {}'.format(centena.get(numero),Tradutor(num%(numero*100)))
    return result

def TradutorMilhar(num):
    result = ""
    numero = math.ceil(int(num/1000))
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