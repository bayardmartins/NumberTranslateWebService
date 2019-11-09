# NumberTranslateWebService
Web Server que recebe um inteiro e responde com o texto escrito por extenso.

Instruções para uso
  Execute o arquivo NumberTranslateWebService.py (NumberTranslateWebService.py python na linha de comando)
  Através de sua ferramenta favorita de teste de API envie um GET para localhost:8080/UMNUMERO
  Esta aplicação aceita entradas de -99999 até 99999. Caso seja enviado um GET válido o servidor responderá
  status 200 e um json com chave "extenso" e valor o número enviado por extenso. Caso o número enviado não
  seja um inteiro, ou o valor absoluto do número seja maior do que 99999 a resposta será 404.
  Por exemplo:
  GET: localhost/1234 a resposta será 200 {"extenso": "mil e duzentos e trinta e quatro"}
  GET: localhost/abc a resposta será 404 abc
