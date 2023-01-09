"""Renomear os certificados com o nome do participante contido no texto do certificado em PDF.
    Entrada: Arquivo PDF do certificado
    Processamento: abrir_arquivo_certificado_pdf(nome_do_arquivo_pdf)
                    converter_conteudo_para_texto()
                    localizar_nome_do_participante()
                    renomear_arquivo_pdf_com_nome_do_participante()
    Saída: Certificado renomeado
"""


import PyPDF2
import os
from unidecode import unidecode
from typing import Final

PASTA_COM_ARQUIVOS_PDF: Final = "/home/ricardo/Documentos/Trabalho em casa/CERTIFICADOS/"


def abrir_arquivo_certificado_pdf(nome_arquivo_pdf):
    try:
        arquivo_certificado_pdf = open(nome_arquivo_pdf, 'rb')
        return arquivo_certificado_pdf
    except:
        return None


def converter_conteudo_para_texto(arquivo_certificado_pdf):
    try:
        descritor_do_pdf = PyPDF2.PdfReader(arquivo_certificado_pdf)
        conteudo_texto_do_pdf = descritor_do_pdf.pages[0].extract_text()
        return conteudo_texto_do_pdf
    except:
        return None


def localizar_nome_do_participante(conteudo_texto_do_pdf):
    try:
        linha_com_nome_participante = 3
        nome_localizado = conteudo_texto_do_pdf.splitlines()[linha_com_nome_participante]
        nome_sem_acentuacao = unidecode(nome_localizado)  
        return nome_sem_acentuacao
    except:
        return None


def renomear_arquivo_pdf_com_nome_do_participante(arquivo_certificado_pdf, novo_nome_pdf):
    try:
        os.rename(arquivo_certificado_pdf, novo_nome_pdf)
        return True
    except:
        return None


if __name__ == "__main__":
    quantidade_arquivo_renomeado: int = 0
    print("Renomeando arquivos PDF ...")
    
    for nome_arquivo_pdf in os.listdir(PASTA_COM_ARQUIVOS_PDF):
        try:
            nome_arquivo_pdf_com_caminho = PASTA_COM_ARQUIVOS_PDF+nome_arquivo_pdf
            arquivo_certificado_pdf = abrir_arquivo_certificado_pdf(nome_arquivo_pdf_com_caminho)
            conteudo_texto_do_pdf = converter_conteudo_para_texto(arquivo_certificado_pdf)
            nome_no_certificado = localizar_nome_do_participante(conteudo_texto_do_pdf)
            novo_nome_pdf = f"{PASTA_COM_ARQUIVOS_PDF}CERTIFICADO DOCKER - {nome_no_certificado}.pdf"
            renomear_arquivo_pdf_com_nome_do_participante(nome_arquivo_pdf_com_caminho, novo_nome_pdf)
            quantidade_arquivo_renomeado += 1
            print(f"{quantidade_arquivo_renomeado}, ", end="")

        except:
            print("Erro")
    print("")
    print(f"{quantidade_arquivo_renomeado} arquivo(s) renomeado(s).")
