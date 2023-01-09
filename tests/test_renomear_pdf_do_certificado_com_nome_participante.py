"""Renomear os certificados com o nome do participante contido no texto do certificado em PDF.
    Entrada: Arquivo PDF do certificado
    Processamento: abrir_arquivo_certificado_pdf(nome_do_arquivo_pdf)
                    converter_conteudo_para_texto()
                    localizar_nome_do_participante()
                    renomear_arquivo_pdf_com_nome_do_participante()
    Saída: Certificado renomeado
"""


from renomear_pdf_do_certificado_com_nome_participante import __version__, main as app


def test_version():
    assert __version__ == '0.1.0'

def test_abrir_arquivo_certificado_pdf():
    assert app.abrir_arquivo_certificado_pdf(app.PASTA_COM_ARQUIVOS_PDF+"RODRIGO FERNANDO.pdf") != None

def test_abrir_arquivo_certificado_pdf_invalido():
    assert app.abrir_arquivo_certificado_pdf("") == None

def test_converter_conteudo_para_texto():
    assert app.converter_conteudo_para_texto(app.abrir_arquivo_certificado_pdf(app.PASTA_COM_ARQUIVOS_PDF+"RODRIGO FERNANDO.pdf")) != None

def test_converter_conteudo_para_texto_em_branco():
    assert app.converter_conteudo_para_texto(app.abrir_arquivo_certificado_pdf(app.PASTA_COM_ARQUIVOS_PDF+"RODRIGO FERNANDO.pdddddd")) != ""

def test_localizar_nome_do_participante():
    assert app.localizar_nome_do_participante(app.converter_conteudo_para_texto(app.abrir_arquivo_certificado_pdf(app.PASTA_COM_ARQUIVOS_PDF+"RODRIGO FERNANDO.pdf"))) == "RODRIGO FERNANDO PINHEIRO OLIVEIRA"

def test_localizar_nome_do_participante_invalido():
    assert app.localizar_nome_do_participante(app.converter_conteudo_para_texto(app.abrir_arquivo_certificado_pdf("./certificados/CERTIFICADO - JOSE ONTEIRO.pdfffffff"))) == None
 
def test_renomear_arquivo_pdf_com_nome_do_participante():
    assert app.renomear_arquivo_pdf_com_nome_do_participante(app.PASTA_COM_ARQUIVOS_PDF+"RODRIGO FERNANDO.pdf", app.PASTA_COM_ARQUIVOS_PDF+"RODRIGO FERNANDOx.pdf") != None