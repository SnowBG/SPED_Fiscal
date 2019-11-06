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
    elif linha[1] == '0150':
      tabela_cadastro_participante(linha)
    elif linha[1] == '0175':
      alteracao_cadastro_participante(linha)
    elif linha[1] == '0190':
      identificacao_unidades_medida(linha)
    elif linha[1] == '0200':
      tabela_id_item(linha)
    elif linha[1] == '206':
      codigo_produto_anp(linha)
    elif linha[1] == '0210':
      consumo_especifico_padronizado(linha)
    elif linha[1] == '0220':
      fatores_conversao_unidade(linha)
    elif linha[1] == '0300':
      cadastro_bens_componentes_ativo_imobiliario(linha)
    elif linha[1] == '0305':
      info_utilizacao_do_bem(linha)
    elif linha[1] == '0400':
      tab_natureza_op_prestacao(linha)
    elif linha[1] == '0450':
      tab_info_complementar_doc_fiscal(linha)
    elif linha[1] == '0460':
      tab_obs_lancamento_fiscal(linha)
    elif linha[1] == '0500':
      plano_contas_contabeis(linha)
    elif linha[1] == '0600':
      contro_custos(linha)
    elif linha[1] == '0990':
      encerramento_bloco(linha)
    elif linha[1] == 'A001':
      abertura_bloco_a(linha)
    elif linha[1] == 'A010':
      identificacao_estabelecimento(linha)
    elif linha[1] == 'A100':
      nfs(linha)
    elif linha[1] == 'A110':
      info_complementar_nf(linha)
    elif linha[1] == 'A111':
      processo_referenciado(linha)
    elif linha[1] == 'A120':
      op_importacao(linha)
    elif linha[1] == 'A170':
      itens_doc(linha)


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

def alteracao_item(linha):
  '''
  REGISTRO 0205: ALTERAÇÃO DO ITEM
    REG: Texto fixo contendo "0205"
    DESCR_ANT_ITEM: Descrição anterior do item
    DT_INI: Data inicial de utilização da descrição do item
    DT_FIM: Data final de utilização da descrição do item
    COD_ANT_ITEM:Código anterior do item com relação à última informação apresentada.
  '''
  REG = linha[1]
  DESCR_ANT_ITEM = linha[2]
  DT_INI = linha[3]
  DT_FIM = linha[4]
  COD_ANT_ITEM = linha[5]

  lgg.info('REGISTRO 0205: ALTERAÇÃO DO ITEM.')
  lgg.info(f'REG: {REG}, DESCR_ANT_ITEM: {DESCR_ANT_ITEM}, DT_INI: {DT_INI}, DT_FIM {DT_FIM}, COD_ANT_ITEM: {COD_ANT_ITEM}')

def codigo_produto_anp(linha):
  '''
  REGISTRO 0206: CÓDIGO DE PRODUTO CONFORME TABELA PUBLICADA PELA ANP.
    REG: Texto fixo contendo "0206".
    COD_COMB: Código do produto, conforme tabela publicada pela ANP.
  '''
  REG = linha[1]
  COD_COMB = linha[2]

  lgg.info('REGISTRO 0206: CÓDIGO DE PRODUTO CONFORME TABELA PUBLICADA PELA ANP.')
  lgg.info('REG: {REG}, COD_COMB: {COD_COMB}')

def consumo_especifico_padronizado(linha):
  '''
  REGISTRO 0210: Consumo Específico Padronizado
    REG: Texto fixo contendo "0210"
    COD_ITEM_COMP: Código do item componente/insumo (campo 02 do Registro 0200)
    QTD_COMP: Quantidade do item componente/insumo para se produzir uma unidadedo item composto/resultante
    PERDA: Perda/quebra   normal   percentual   do   insumo/componente  para   seproduzir uma unidade do item composto/resultante
  '''
  REG = linha[1]
  COD_ITEM_COMP = linha[2]
  QTD_COMP = linha[3]
  PERDA = linha[4]
  lgg.info('REGISTRO 0210: Consumo Específico Padronizado')
  lgg.info('REG: {REG}, COD_ITEM_COMP: {COD_ITEM_COMP}, QTD_COMP: {QTD_COMP}')

def fatores_conversao_unidade(linha):
  '''
  REGISTRO 0220: FATORES DE CONVERSÃO DE UNIDADES.
    REG: Texto fixo contendo "0220"
    UNID_CONV:Unidade comercial a ser convertida na unidade de estoque, referida no registro 0200.
    FAT_CONV: Fator de conversão: fator utilizado para converter (multiplicar) a unidade a ser convertida na unidade adotada no inventário.
  '''
  REG = linha[1]
  UNID_CONV = linha[2]
  FAT_CONV = linha[3]

  lgg.info('REGISTRO 0220: FATORES DE CONVERSÃO DE UNIDADES.')
  lgg.info(f'REG: {REG}, UNID_CONV: {UNID_CONV}, FAT_CONV: {FAT_CONV}')

def cadastro_bens_componentes_ativo_imobiliario(linha):
  '''
  REGISTRO 0300: CADASTRO DE BENS OU COMPONENTES DO ATIVO IMOBILIZADO.
    REG: Texto fixo contendo "0300".
    COD_IND_BEM: Código individualizado do bem ou componente adotado no controle patrimonial do estabelecimento informante.
    IDENT_MERC: Identificação do tipo de mercadoria:
      1 = bem;
      2 = componente.
    DESCR_ITEM: Descrição   do   bem   ou   componente   (modelo,   marca   e   outras
    características necessárias a sua individualização).
    COD_PRNC: Código de cadastro do bem principal nos casos em que o bem ou componente ( campo 02) esteja vinculado a um bem principal.
    COD_CTA: Código da conta analítica de contabilização do bem ou componente (campo 06 do Registro 0500).
    NR_PARC: Número total de parcelas a serem apropriadas, segundo a legislação
    de cada unidade federada.

  '''
  REG = linha[1]
  COD_IND_BEM = linha[2]
  IDENT_MERC = linha[3]
  DESCR_ITEM = linha[4]
  COD_PRNC = linha[5]
  COD_CTA = linha[6]
  NR_PARC = linha[7]

  
  lgg.info('REGISTRO 0300: CADASTRO DE BENS OU COMPONENTES DO ATIVO IMOBILIZADO.')
  lgg.info(f'REG: {REG}, COD_IND_BEM: {COD_IND_BEM}, IDENT_MERC: {IDENT_MERC}. DESCR_ITEM: {DESCR_ITEM}, COD_PRNC: {COD_PRNC}, COD_CTA: {COD_CTA} NR_PARC: {NR_PARC}')

def info_utilizacao_do_bem(linha):
  '''
  REGISTRO 0305: INFORMAÇÕES SOBRE A UTILIZAÇÃO DO BEM
    REG: Texto fixo contendo "0305"
    COD_CCUS: Código do centro de custo onde o bem está sendo ou será utilizado (campo 03 do Registro 0600)
    FUNC: Descrição sucinta da função do bem na atividade do estabelecimento
    VIDA_UTIL: Vida útil estimada do bem, em número de meses
  '''
  REG = linha[1]
  COD_CCUS = linha[2]
  FUNC = linha[3]
  VIDA_UTIL = linha[4]
  


  lgg.info('REGISTRO 0305: INFORMAÇÕES SOBRE A UTILIZAÇÃO DO BEM')
  lgg.info(f'REG: {REG}, COD_CCUS: {COD_CCUS}, FUNC: {FUNC}. VIDA_UTIL: {VIDA_UTIL}')

def tab_natureza_op_prestacao(linha):
  '''
  REGISTRO 0400: TABELA DE NATUREZA DA OPERAÇÃO/PRESTAÇÃO
    REG: Texto fixo contendo "0400".
    COD_NAT: Código da natureza da operação/prestação.
    DESCR_NAT: Descrição da natureza da operação/prestação.
  '''
  REG = linha[1]
  COD_NAT = linha[2]
  DESCR_NAT = linha[3]


  lgg.info('REGISTRO 0400: TABELA DE NATUREZA DA OPERAÇÃO/PRESTAÇÃO.')
  lgg.info(f'REG: {REG}, COD_NAT: {COD_NAT}, DESCR_NAT: {DESCR_NAT}')

def tab_info_complementar_doc_fiscal(linha):
  '''
  REGISTRO 0450: TABELA DE INFORMAÇÃO COMPLEMENTAR DO DOCUMENTO FISCAL
    REG: Texto fixo contendo "0400".
    COD_INF: Código da informação complementar do documento fiscal.
    TXT: Texto livre da informação complementar existente no documento fiscal,
inclusive   espécie   de   normas   legais,   poder   normativo,   número,
capitulação, data e demais referências pertinentes com indicações
referentes ao tributo.
  '''
  REG = linha[1]
  COD_INF = linha[2]
  TXT = linha[3]


  lgg.info('REGISTRO 0450: TABELA DE INFORMAÇÃO COMPLEMENTAR DO DOCUMENTO FISCAL.')
  lgg.info(f'REG: {REG}, COD_INF: {COD_INF}, TXT: {TXT}')

def plano_contas_contabeis(linha):
  '''
  REGISTRO 0500: PLANO DE CONTAS CONTÁBEIS
    REG: Texto fixo contendo “0500”.
    DT_ALT: Data da inclusão/alteração.
    NAT_CC: Código da natureza da conta/grupo de contas:
      01 - Contas de ativo;
      02 - Contas de passivo;
      03 - Patrimônio líquido;
      04 - Contas de resultado;
      05 - Contas de compensação;
      09 - Outras.
    IND_CTA: Indicador do tipo de conta:
      S - Sintética (grupo de contas);
      A - Analítica (conta).
    NÍVEL: Nível da conta analítica/grupo de contas.
    COD_CTA: Código da conta analítica/grupo de contas.
    NOME_CTA: Nome da conta analítica/grupo de contas.
  '''
  REG = linha[1]
  DT_ALT = linha[2]
  NAT_CC = linha[3]
  IND_CTA = linha[4]
  NÍVEL = linha[5]
  COD_CTA = linha[6]
  NOME_CTA = linha[7]

  lgg.info('REGISTRO 0500: PLANO DE CONTAS CONTÁBEIS.')
  lgg.info(f'REG: {REG}, DT_ALT: {DT_ALT}, NAT_CC: {NAT_CC}, IND_CTA: {IND_CTA}, NÍVEL: {NÍVEL}, COD_CTA: {COD_CTA}, NOME_CTA: {NOME_CTA}')

def info_utilizacao_do_bem(linha):
  '''
  REGISTRO 0600: CENTRO DE CUSTOS
    REG: Texto fixo contendo "0305"
    DT_ALT: Data da inclusão/alteração.
    COD_CCUS: Código do centro de custos.
    CCUS: Nome do centro de custos
  '''
  REG = linha[1]
  DT_ALT = linha[2]
  COD_CCUS = linha[3]
  CCUS = linha[4]
  


  lgg.info('REGISTRO 0305: INFORMAÇÕES SOBRE A UTILIZAÇÃO DO BEM')
  lgg.info(f'REG: {REG}, DT_ALT: {DT_ALT}, COD_CCUS: {COD_CCUS}. CCUS: {CCUS}')

def encerramento_bloco(linha):
  '''
  REGISTRO 0990: ENCERRAMENTO DO BLOCO 0
  Vars:
    REG Texto fixo contendo “0001”.
    QTD_LIN_0: Quantidade total de linhas do Bloco 0
  '''
  REG = linha[1]
  QTD_LIN_0 = linha[2]

  lgg.info('REGISTRO 0001: ENCERRAMENTO DO BLOCO 0')
  lgg.info(f'REG {REG}, QTD_LIN_0 {QTD_LIN_0}')

def abertura_bloco_a(linha):
  '''
  Registro A001: Abertura do Bloco A
    REG Texto fixo contendo "A001" 
    IND_MOV Indicador de movimento: 
      0 - Bloco com dados informados; 
      1 - Bloco sem dados informados 
  '''
  REG = linha[1]
  IND_MOV = linha[2]
  lgg.info('REGISTRO 0001: ABERTURA DO BLOCO 0')
  lgg.info(f'REG {REG}, IND_MOV {IND_MOV}')

def identificacao_estabelecimento(linha):
  '''
    Registro A010: Identificação do Estabelecimento 
      REG Texto fixo contendo “A010”
      CNPJ Número de inscrição do estabelecimento no CNPJ. 
  '''
  REG = linha[1]
  CNPJ = linha[2]
  lgg.info('REGISTRO 0001: ABERTURA DO BLOCO 0')
  lgg.info(f'REG {REG}, CNPJ {CNPJ}')

def nfs(linha):
  '''
  Registro A100: Documento - Nota Fiscal de Serviço
    REG Texto fixo contendo "A100" 
    IND_OPER Indicador do tipo de operação: 
      0 - Serviço Contratado pelo Estabelecimento; 
      1 - Serviço Prestado pelo Estabelecimento. 
    IND_EMIT Indicador do emitente do documento fiscal: 
      0 - Emissão Própria; 
      1 - Emissão de Terceiros 
    COD_PART Código do participante (campo 02 do Registro 0150): 
      - do emitente do documento, no caso de emissão de terceiros; 
      - do adquirente, no caso de serviços prestados. 
    COD_SIT Código da situação do documento fiscal: 
      00 – Documento regular 
      02 – Documento cancelado 
    SER Série do documento fiscal
    SUB Subsérie do documento fiscal 
    NUM_DOC Número do documento fiscal ou documento internacional equivalente 
    CHV_NFSE Chave/Código de Verificação da nota fiscal de serviço eletrônica 
    DT_DOC Data da emissão do documento fiscal 
    DT_EXE_SERV Data de Execução / Conclusão do Serviço 
    VL_DOC Valor total do documento 
    IND_PGTO Indicador do tipo de pagamento: 
      0- À vista; 
      1- A prazo; 
      9- Sem pagamento. 
    VL_DESC Valor total do desconto
    VL_BC_PIS Valor da base de cálculo do PIS/PASEP
    VL_PIS Valor total do PIS 
    VL_BC_COFINS Valor da base de cálculo da COFINS
    VL_COFINS Valor total da COFINS 
    VL_PIS_RET Valor total do PIS retido na fonte 
    VL_COFINS_RET Valor total da COFINS retido na fonte. 
    VL_ISS Valor do ISS
  '''
  REG = linha[1]
  IND_OPER = linha[2]
  IND_EMIT = linha[3]
  COD_PART = linha[4]
  COD_SIT = linha[5]
  SER = linha[6]
  SUB = linha[7]
  NUM_DOC = linha[8]
  CHV_NFSE = linha[9]
  DT_DOC = linha[10]
  DT_EXE_SERV = linha[11]
  VL_DOC = linha[12]
  IND_PGTO = linha[13]
  VL_DESC = linha[14]
  VL_BC_PIS = linha[15]
  VL_PIS = linha[16]
  VL_BC_COFINS = linha[17]
  VL_COFINS = linha[18]
  VL_PIS_RET = linha[19]
  VL_COFINS_RET = linha[20]
  VL_ISS = linha[21]

  lgg.info('Registro A100: Documento - Nota Fiscal de Serviço.')
  lgg.info(f'REG: {REG}, IND_OPER: {IND_OPER}, IND_EMIT: {IND_EMIT}, COD_PART: {COD_PART}, COD_SIT: {COD_SIT}, SER: {SER}, SUB: {SUB}, NUM_DOC: {NUM_DOC}, CHV_NFSE: {CHV_NFSE}, DT_DOC: {DT_DOC}, DT_EXE_SERV: {DT_EXE_SERV}, VL_DOC: {VL_DOC}, IND_PGTO: {IND_PGTO}, VL_DESC: {VL_DESC}, VL_BC_PIS: {VL_BC_PIS}, VL_PIS: {VL_PIS}, VL_BC_COFINS: {VL_BC_COFINS}, VL_COFINS: {VL_COFINS}, VL_PIS_RET: {VL_PIS_RET}, VL_COFINS_RET: {VL_COFINS_RET}, VL_ISS: {VL_ISS}')

def info_complementar_nf(linha):
  '''
  Registro A110: Complemento do Documento - Informação Complementar da NF 
    REG Texto fixo contendo "A110"
    COD_INF Código da informação complementar do documento fiscal (Campo 02 do Registro 0450) 
    TXT_COMPL Informação Complementar do Documento Fiscal 
  '''

  REG = linha[1]
  COD_INF = linha[2]
  TXT_COMPL = linha[3]
  lgg.info('REGISTRO 0001: ABERTURA DO BLOCO 0')
  lgg.info(f'REG {REG}, COD_INF {COD_INF}, TXT_COMPL {TXT_COMPL}')

def processo_referenciado(linha):
  '''
  Registro A111: Processo Referenciado  
    REG Texto fixo contendo "A110"
    NUM_PROC Identificação do processo ou ato concessório 
    IND_PROC Indicador da origem do processo: 
      1 - Justiça Federal; 
      3 – Secretaria da Receita Federal do Brasil 
      9 - Outros.  
  '''

  REG = linha[1]
  NUM_PROC = linha[2]
  IND_PROC = linha[3]
  lgg.info('REGISTRO 0001: ABERTURA DO BLOCO 0')
  lgg.info(f'REG {REG}, NUM_PROC {NUM_PROC}, IND_PROC {IND_PROC}')

def op_importacao(linha):
  '''
  Registro A120: Informação Complementar - Operações de Importação.
    REG Texto fixo contendo "A120” 
    VL_TOT_SERV Valor total do serviço, prestado por pessoa física ou jurídica domiciliada no exterior. 
    VL_BC_PIS Valor da base de cálculo da Operação – PIS/PASEP – Importação 
    VL_PIS_IMP Valor pago/recolhido de PIS/PASEP – Importação 
    DT_PAG_PIS Data de pagamento do PIS/PASEP – Importação 
    VL_BC_COFINS Valor da base de cálculo da Operação – COFINS – Importação 
    VL_COFINS_IMP Valor pago/recolhido de COFINS – Importação
    DT_PAG_COFINS Data de pagamento do COFINS- Importação
    LOC_EXE_SERV Local da execução do serviço: 
      0 – Executado no País; 
      1 – Executado no Exterior, cujo resultado se verifique no País. 
  '''
  REG = linha[1]
  VL_TOT_SERV = linha[2]
  VL_BC_PIS = linha[3]
  VL_PIS_IMP = linha[4]
  DT_PAG_PIS = linha[5]
  VL_BC_COFINS = linha[6]
  VL_COFINS_IMP = linha[7]
  DT_PAG_COFINS = linha[8]
  LOC_EXE_SERV = linha[9]

  lgg.info('Registro A120: Informação Complementar - Operações de Importação')
  lgg.info(f'REG: {REG},  VL_TOT_SERV: {VL_TOT_SERV}, VL_PIS_IMP: {VL_PIS_IMP}, DT_PAG_PIS: {DT_PAG_PIS}, VL_BC_COFINS: {VL_BC_COFINS}, VL_COFINS_IMP: {VL_COFINS_IMP}, DT_PAG_COFINS: {DT_PAG_COFINS}, LOC_EXE_SERV: {LOC_EXE_SERV}')

def itens_doc(linha):
  '''
  Registro A170: Complemento do Documento - Itens do Documento
    REG Texto fixo contendo "A170"
    NUM_ITEM Número seqüencial do item no documento fiscal 
    COD_ITEM Código do item (campo 02 do Registro 0200) 
    DESCR_COMPL Descrição complementar do item como adotado no documento fiscal 
    VL_ITEM Valor total do item (mercadorias ou serviços) 
    VL_DESC Valor do desconto comercial  / exclusão da base de cálculo do PIS/PASEP e da COFINS 
    NAT_BC_CRED Código da base de cálculo do crédito, conforme a Tabela indicada no item 4.3.7, caso seja informado código representativo de crédito no Campo 09 (CST_PIS) ou no Campo 13 (CST_COFINS). 
    IND_ORIG_CRED Indicador da origem do crédito: 0 – Operação no Mercado Interno 1 – Operação de Importação 
    CST_PIS Código da Situação Tributária referente ao PIS/PASEP – Tabela 4.3.3. 
    VL_BC_PIS Valor da base de cálculo do PIS/PASEP.
    ALIQ_PIS Alíquota do PIS/PASEP (em percentual)
    VL_PIS Valor do PIS/PASEP 
    CST_COFINS Código da Situação Tributária referente ao COFINS – Tabela 4.3.4. 
    VL_BC_COFINS Valor da base de cálculo da COFINS 
    ALIQ_COFINS Alíquota do COFINS (em percentual) 
    VL_COFINS Valor da COFINS 
    COD_CTA Código da conta analítica contábil debitada/creditada 
    COD_CCUS Código do centro de custos 
  '''
  
  REG = linha[1]
  NUM_ITEM = linha[2]
  COD_ITEM = linha[3]
  DESCR_COMPL = linha[4]
  VL_ITEM = linha[5]
  VL_DESC = linha[6]
  NAT_BC_CRED = linha[7]
  IND_ORIG_CRED = linha[8]
  CST_PIS = linha[9]
  VL_BC_PIS = linha[10]
  ALIQ_PIS = linha[11]
  VL_PIS = linha[12]
  CST_COFINS = linha[13]
  VL_BC_COFINS = linha[14]
  ALIQ_COFINS = linha[15]
  VL_COFINS = linha[16]
  COD_CTA = linha[17]
  COD_CCUS = linha[18]

  lgg.info('Registro A170: Complemento do Documento - Itens do Documento.')

  lgg.info(f'REG: {REG}, NUM_ITEM: {NUM_ITEM}, COD_ITEM: {COD_ITEM}, DESCR_COMPL: {DESCR_COMPL}, VL_ITEM: {VL_ITEM}, VL_DESC: {VL_DESC}, NAT_BC_CRED: {NAT_BC_CRED}, IND_ORIG_CRED: {IND_ORIG_CRED}, CST_PIS: {CST_PIS}, VL_BC_PIS: {VL_BC_PIS} ALIQ_PIS: {ALIQ_PIS}, VL_PIS: {VL_PIS}, CST_COFINS: {CST_COFINS}, VL_BC_COFINS: {VL_BC_COFINS}, ALIQ_COFINS: {ALIQ_COFINS}, VL_COFINS: {VL_COFINS}, COD_CTA: {COD_CTA}, COD_CCUS: {COD_CCUS}.')

triagem()