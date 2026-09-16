import io
from docx import Document


def criar_documento(dados):
    
    substituicoes = {
    "{NOMECLIENTE}": dados.nome,
    "{NACIONALIDADECLIENTE}": dados.nacionalidade,
    # Se 'estado civil' e 'profissão' também vierem de variáveis, mude aqui:
    "{ESTADOCIVILCLIENTE}": dados.estado_civil,
    "{PROFISSAOCLIENTE}": dados.profissao,
    "{CINCLIENTE}": dados.nr_rg,  # ou dados.nr_ci
    "{CPFCLIENTE}": dados.nr_cpf,
    "{RUACLIENTE}": dados.rua,
    "{ENDERECONUMEROCLIENTE}": dados.numero,
    "{BAIRROCLIENTE}": dados.bairro,
    "{CIDADECLIENTE}": dados.cidade,
    "{ESTADOCLIENTE}": dados.estado,
    "{CEPCLIENTE}": dados.cep,
    }
    doc = Document("contratoHonorarios.docx")
    
    for paragrafo in doc.paragraphs:
        for termo_antigo, termo_novo in substituicoes.items():
            if termo_antigo in paragrafo.text:
                paragrafo.text = paragrafo.text.replace(termo_antigo, termo_novo)
    
    arquivo_em_memoria = io.BytesIO()
    doc.save(arquivo_em_memoria)
    arquivo_em_memoria.seek(0)
    return arquivo_em_memoria.getvalue()