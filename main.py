import logging as lgg

	
lgg.basicConfig(filename='sped.log',format='%(levelname)s:%(message)s', level=lgg.INFO)

def ler_arquivo():
  with open('2018-01.txt','rb') as f:
    arquivo = f.readlines()
  linhas = []
  [linhas.append(x.decode('ISO-8859-1').split('|')) for x in arquivo]
  return linhas

def triagem():
  linhas = ler_arquivo()
  for linha in linhas:
    if linha[1] == '0000':
      abertura_arquivo(linha)
    elif linha[1] == '0001':
      abertura_bloco(linha)
    elif linha[1] == '0005':
      dados_complementares(linha)
    elif linha[1] == '0015':
      dados_contribuinte_substituto(linha)
    elif linha[1] == '0100':
      dados_contabilista(linha)
    elif linha[1] =='0150':
      tabela_cadastro_participante(linha)
    elif linha[1] == '0175':
      alteracao_cadastro_participante(linha)
    elif linha[1] == '0190':
      identificacao_unidades_medida(linha)
    elif linha[1] =='0200':
      tabela_id_item(linha)

def abertura_arquivo(linha):
  '''
  REGISTRO 0000: ABERTURA DO ARQUIVO DIGITAL E IDENTIFICAÇÃO DA ENTIDADE
  Vars:
    REG: Texto fixo contendo “0000”.
    COD_VER: Código da versão do leiaute conforme a tabela indicada no Ato Cotepe.
    COD_FIN: Código da finalidade do arquivo:
      0 - Remessa do arquivo original;
      1 - Remessa do arquivo substituto.
    DT_INI: Data inicial das informações contidas no arquivo.
    DT_FIN: Data final das informações contidas no arquivo.
    NOME: Nome empresarial da entidade.
    CNPJ: Número de inscrição da entidade no CNPJ.
    CPF: Número de inscrição da entidade no CPF.
    UF: Sigla da unidade da federação da entidade.
    IE: Inscrição Estadual da entidade.
    COD_MUN: Código do município do domicílio fiscal da entidade, conforme a tabela IBGE.
    IM: Inscrição Municipal da entidade.
    SUFRAMA: Inscrição da entidade na Suframa
    IND_PERFIL: Perfil de apresentação do arquivo fiscal;
      A - Perfil A;
      B - Perfil B.;
      C - Perfil C.

    IND_ATIV: Indicador de tipo de atividade:
      0 - Industrial ou equiparado a industrial;
      1 - Outros
  '''
  REG = linha[1] 
  COD_VER = linha[2] 
  COD_FIN = linha[3]
  DT_INI = linha[4] 
  DT_FIN = linha[5] 
  NOME = linha[6] 
  CNPJ = linha[7] 
  CPF = linha[8]
  UF = linha[9]
  IE = linha[10]
  COD_MUN = linha[11]
  IM = linha[12]
  SUFRAMA = linha[13]
  IND_PERFIL = linha[14]
  IND_ATIV = linha[15]

  lgg.info('REGISTRO 0000: ABERTURA DO ARQUIVO DIGITAL E IDENTIFICAÇÃO DA ENTIDADE.')
  lgg.info(f'REG: {REG},COD_VER: {COD_VER}, COD_FIN: {COD_FIN}, DT_INI: {DT_INI}, DT_FIN: {DT_FIN},NOME: {NOME}, CNPJ: {CNPJ}, {CPF}, {UF}, {IE}, {COD_MUN}, {IM}, {SUFRAMA}, {IND_PERFIL}, {IND_ATIV}')

def abertura_bloco(linha):
  '''
  REGISTRO 0001: ABERTURA DO BLOCO 0
  Vars:
    REG Texto fixo contendo “0001”.
    IND_MOV Indicador de movimento:
          0- Bloco com dados informados;
          1- Bloco sem dados informados.
  '''
  REG = linha[1]
  IND_MOV = linha[2]

  lgg.info('REGISTRO 0001: ABERTURA DO BLOCO 0')
  lgg.info(f'REG {REG}, IND_MOV {IND_MOV}')

def dados_complementares(linha):
  '''
  REGISTRO 0005: DADOS COMPLEMENTARES DA ENTIDADE
      REG: Texto fixo contendo “0005”
      FANTASIA: Nome de fantasia associado ao nome empresarial.
      CEP: Código de Endereçamento Postal.
      END: Logradouro e endereço do imóvel.
      NUM: Número do imóvel.
      COMPL: Dados complementares do endereço.
      BAIRRO: Bairro em que o imóvel está situado.
      FONE: Número do telefone.
      FAX: Número do fax.
      EMAIL: Endereço do correio eletrônico
  '''
  REG = linha[1]
  FANTASIA = linha[2]
  CEP = linha[3]
  END = linha[4]
  NUM = linha[5]
  COMPL = linha[6]
  BAIRRO = linha[7]
  FONE = linha[8]
  FAX = linha[9]
  EMAIL = linha[10]

  lgg.info('REGISTRO 0005: DADOS COMPLEMENTARES DA ENTIDADE.')
  lgg.info(f'REG: {REG},FANTASIA: {FANTASIA},CEP: {CEP},END: {END}, NUM: {NUM}, COMPL: {COMPL},BAIRRO {BAIRRO},FONE {FONE},FAX {FAX}, EMAIL: {EMAIL}')

def dados_contribuinte_substituto(linha):
  '''
  REGISTRO 0015: DADOS DO CONTRIBUINTE SUBSTITUTO OU RESPONSÁVEL PELO ICMS DESTINO.
    REG: Texto fixo contendo "0015"
    UF_ST: Sigla da unidade da federação do contribuinte substituído ou unidade de federação do consumidor final não contribuinte - ICMS Destino EC 87/15”
    IE_ST: Inscrição Estadual do contribuinte substituto na unidade da federação do contribuinte substituído ou unidade de federação do consumidor final não contribuinte - ICMS Destino EC 87/15.
  '''
  REG = linha[1]
  UF_ST = linha[2]
  IE_ST = linha[3]

  lgg.info('REGISTRO 0015: DADOS DO CONTRIBUINTE SUBSTITUTO OU RESPONSÁVEL PELO ICMS DESTINO.')
  lgg.info(f'REG: {REG},UF_ST: {UF_ST},IE_ST: {IE_ST}')

def dados_contabilista(linha):
  '''
  REGISTRO 0100: DADOS DO CONTABILISTA

    REG:Texto fixo contendo “0100”.
    NOME:Nome do contabilista.
    CPF:Número de inscrição do contabilista no CPF.
    CRC:Número   de   inscrição   do   contabilista   no   Conselho   Regional   de
    Contabilidade
    CNPJ:Número de inscrição do escritório de contabilidade no CNPJ, se houver.
    CEP:Código de Endereçamento Postal.
    END:Logradouro e endereço do imóvel.
    NUM:Número do imóvel
    COMPL:Dados complementares do endereço.
    BAIRRO:Bairro em que o imóvel está situado.
    FONE:Número do telefone.
    FAX:Número do fax.
    EMAIL:Endereço do correio eletrônico.
    COD_MUN:Código do município, conforme tabela IBGE.

  '''
  REG = linha[1]
  NOME = linha[2]
  CPF = linha[3]
  CRC = linha[4]
  CNPJ = linha[5]
  CEP = linha[6]
  END = linha[7]
  NUM = linha[8]
  COMPL = linha[9]
  BAIRRO = linha[10]
  FONE = linha[11]
  FAX = linha[12]
  EMAIL = linha[13]

  lgg.info('REGISTRO 0100: DADOS DO CONTABILISTA')
  lgg.info(f'REG: {REG}, NOME: {NOME}, CPF: {CPF}, CRC: {CRC}, CNPJ: {CNPJ}, CEP: {CEP}, END: {END}, NUM: {NUM}, COMPL: {COMPL}, BAIRRO: {BAIRRO}, FONE: {FONE}, {FAX}, {EMAIL}')

def tabela_cadastro_participante(linha):
  '''
  REGISTRO 0150: TABELA DE CADASTRO DO PARTICIPANTE
    REG: Texto fixo contendo “0150”.
    COD_PART: Código de identificação do participante no arquivo.
    NOME: Nome pessoal ou empresarial do participante.
    COD_PAIS: Código do país do participante}, {conforme a tabela indicada no item 3.2.1
    CNPJ: CNPJ do participante.
    CPF: CPF do participante.
    IE: Inscrição Estadual do participante.
    COD_MUN: Código do município}, {conforme a tabela IBGE
    SUFRAMA: Número de inscrição do participante na Suframa.
    END: Logradouro e endereço do imóvel
    NUM: Número do imóvel
    COMPL:Dados complementares do endereço
    BAIRRO: Bairro em que o imóvel está situado
  '''
  REG = linha[1]
  COD_PART = linha[2]
  NOME = linha[3]
  COD_PAIS = linha[4]
  CNPJ = linha[5]
  CPF = linha[6]
  IE = linha[7]
  COD_MUN = linha[8]
  SUFRAMA = linha[9]
  END = linha[10]
  NUM = linha[12]
  COMPL = linha[13]
  BAIRRO = linha[14]

  lgg.info("REGISTRO 0150: TABELA DE CADASTRO DO PARTICIPANTE.")
  lgg.info(F'REG: {REG}, COD_PART: {COD_PART},NOME: {NOME},COD_PAIS {COD_PAIS}, CNPJ: {CNPJ},CPF: {CPF}, IE: {IE},COD_MUN: {COD_MUN},SUFRAMA: {SUFRAMA}, END: {END},NUM {NUM},COMPL: {COMPL}, BAIRRO: {BAIRRO}')

def alteracao_cadastro_participante(linha):
  '''
  REGISTRO 0175: Alteração da Tabela de Cadastro de Participante
    REG: Texto fixo contendo “0175”
    DT_ALT: Data de alteração do cadastro
    NR_CAMPO:Número do campo alterado (campos 03 a 13, exceto 07)
    CONT_ANT: Conteúdo anterior do campo

    '''

  REG = linha[1]
  DT_ALT = linha[2]
  NR_CAMPO = linha[3]
  CONT_ANT = linha[4]
  lgg.info('REGISTRO 0175: Alteração da Tabela de Cadastro de Participante.')
  lgg.info(f' REG: {REG},DT_ALT {DT_ALT},NR_CAMPO: {NR_CAMPO},CONT_ANT: {CONT_ANT}')

def identificacao_unidades_medida(linha):
  '''
  REGISTRO 0190: IDENTIFICAÇÃO DAS UNIDADES DE MEDIDA
    REG: Texto fixo contendo “0190”
    UNID: Código da unidade de medida
    DESCR: Descrição da unidade de medida
    
    '''

  REG = linha[1]
  UNID = linha[2]
  DESCR = linha[3]

  lgg.info('REGISTRO 0190: IDENTIFICAÇÃO DAS UNIDADES DE MEDIDA')
  lgg.info(f'REG: {REG}, UNID: {UNID},DESCR: {DESCR}')


def tabela_id_item(linha):
  '''
  REGISTRO 0200: TABELA DE IDENTIFICAÇÃO DO ITEM (PRODUTO E SERVIÇOS)
    REG: Texto fixo contendo "0200"
    COD_ITEM: Código do item.
    DESCR_ITEM: Descrição do item.
    COD_BARRA: Representação alfanumérico do código de barra do produto, se houver
    COD_ANT_ITEM: Código anterior do item com relação à última informação apresentada.
    UNID_INV: Unidade de medida utilizada na quantificação de estoques.
    TIPO_ITEM: Tipo do item - Atividades Industriais, Comerciais e Serviços:
        00 - Mercadoria para Revenda;
        01 - Matéria-Prima;
        02 - Embalagem;
        03 - Produto em Processo;
        04 - Produto Acabado;
        05 - Subproduto;
        06 - Produto Intermediário;
        07 - Material de Uso e Consumo;
        08 - Ativo Imobilizado;
        09 - Serviços;
        10 - Outros insumos;
        99 - Outras
    COD_NCM: Código da Nomenclatura Comum do Mercosul
    EX_IPI: Código EX, conforme a TIPI
    COD_GEN: Código do gênero do item, conforme a Tabela 4.2.1
    COD_LST: Código do serviço conforme lista do Anexo I da Lei Complementar Federal nº 116/03.
    ALIQ_ICMS: Alíquota de ICMS aplicável ao item nas operações internas
    CEST: Código Especificador da Substituição Tributária

  '''
  REG = linha[1]
  COD_ITEM = linha[2]
  DESCR_ITEM = linha[3]
  COD_BARRA = linha[4]
  COD_ANT_ITEM = linha[5]
  UNID_INV = linha[6]
  TIPO_ITEM = linha[7]
  COD_NCM = linha[8]
  EX_IPI = linha[9]
  COD_GEN = linha[10]
  COD_LST = linha[11]
  ALIQ_ICMS = linha[12]
  CEST = linha[13]

  lgg.info('REGISTRO 0200: TABELA DE IDENTIFICAÇÃO DO ITEM (PRODUTO E SERVIÇOS).')
  lgg.info(f'REG: {REG}, COD_ITEM: {COD_ITEM}, DESCR_ITEM: {DESCR_ITEM}, COD_BARRA: {COD_BARRA}, COD_ANT_ITEM: {COD_ANT_ITEM}, UNID_INV: {UNID_INV}, TIPO_ITEM: {TIPO_ITEM}, COD_NCM: {COD_NCM}, EX_IPI: {EX_IPI}, COD_GEN: {COD_GEN}, COD_LST: {COD_LST}, ALIQ_ICMS: {ALIQ_ICMS}, CEST: {CEST}')



triagem()