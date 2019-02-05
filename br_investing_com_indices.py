# -*- coding: utf-8 -*-
import re
import requests
import threading

class BrInvestingCom(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        url = "https://br.investing.com/indices/us-30"
        user_agent = {'User-agent': 'Mozilla/5.0'}
        enderecoReferido = requests.get(url=url,headers=user_agent, timeout=123)
        texto = enderecoReferido.texto
        print("0000"*10)
        tag_valor_USD_BRL = r'<p id="TSB__summary_last_2103" class="arial_24 bold inlineblock js-item-last pid-2103-last_nColor">(.*?)</p>'
        tag_VENDAS = r'<span class="js-item-summary studySummaryOval sell arial_12 bold float_lang_base_2" id="TSB__technical_summary_2103">(.*?)</span>'
        tag_IBOVESPA = r'<td class="lastNum pid-17920-last" id="sb_last_17920">(.*?)</td>'
        taf_bovespa_futuros = r'<td class="lastNum pid-941612-last" id="sb_last_941612">(.*?)</td>'
        USD_BRL =re.compile(tag_valor_USD_BRL, re.UNICODE)
        BRL =re.compile(tag_VENDAS, re.UNICODE)
        indice = USD_BRL.search(texto)
        discricao = BRL.search(texto)
        informacao = discricao.group(1)
        valor = indice.group(1)
        dados = "US/BRL : {} : .. . .. {}".format(valor, informacao)
        print(dados)
        ibovespa =re.compile(tag_IBOVESPA , re.UNICODE)
        pesquisa_item_um = ibovespa.search(texto)
        print("Ibovespa : ..... . .. ...", pesquisa_item_um.group(1))
        ibovespa_F = re.compile(taf_bovespa_futuros, re.UNICODE)
        i_futuro =  ibovespa_F.search(texto)
        print("Ibovespa Futuro : ... . .. ", i_futuro.group(1))
        print("0000" * 10)
        data = r'<span class="bold pid-169-time">(.*?)</span>'
        volume = r'<span class="inlineblock pid-169-volume">(.*?)</span>'
        abertura = r'<span class="arial_26 inlineblock pid-169-last" id="last_last" dir="ltr">(.*?)</span>'
        porcen = r'<span class="arial_20 greenFont  pid-169-pcp parentheses" dir="ltr">(.*?)</span>'
        itens = {'Hora': data, 'Volume': volume, 'Abertura': abertura, 'Up': porcen}
        for titulo , visualizar in dict.items(itens):
            conteudo = re.compile(visualizar, re.UNICODE)
            filtro = conteudo.search(texto)
            dados = filtro.group(1)
            print(titulo, "...........", dados)
        print("0000" * 10)


if __name__ == '__main__':
    BrInvestingCom()
