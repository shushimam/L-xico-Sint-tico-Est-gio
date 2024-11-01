import ply.lex as lex

reserved = {
    'aggregate_Block': 'AGGREGATE_BLOCK',         #Agrega dados para análise por bloco 
    'aggregate_Trial': 'AGGREGATE_TRIAL',         #Agrega dados para análise por trial
    'analyze_Data': 'ANALYZE_DATA',               #Realiza análise de dados coletados
    'block': 'BLOCK',                             #Define um bloco de procedimentos no experimento
    'catch': 'CATCH',                             #Captura um erro identificado no bloco 'Try'
    'connect_Device': 'CONNECT_DEVICE',           #Conecta a um dispositivo externo (por exemplo, sensores)
    'display_Feedback': 'DISPLAY_FEEDBACK',       #Fornece feedback específico com base na resposta do participante aos objetos apresentados anteriormente no fluxo do experimento
    'display_Image': 'DISPLAY_IMAGE',             #Exibe imagem na tela ou dispositivo de saída
    'display_Movie': 'DISPLAY_MOVIE',             #Apresenta um arquivo de vídeo (.avi/.mp4/.wmv)
    'display_Sound': 'DISPLAY_SOUND',             #Reproduz som ou áudio através de um dispositivo de saída (.wav/.mp3/.wma)
    'display_Text': 'DISPLAY_TEXT',               #Exibe texto na tela ou dispositivo de saída
    'else': 'ELSE',                               #Estrutura condicional 'senão'
    'experiment': 'EXPERIMENT',                   #Sequência experimental completa, composta de diversas etapas a serem definidas
    'experiment_Desing': 'EXPERIMENT_DESING',     #Define o design do experimento, incluindo between-subjects e within-subjects
    'filter': 'FILTER',                           #Filtra dados com base em critérios específicos
    'flag': 'FLAG',                               #Indica um local específico na linha do tempo (Procedimento). O programa pode ‘pular’ para frente ou para trás em um rótulo, para repetir ou pular uma parte do Procedimento
    'for': 'FOR',                                 #Estrutura de loop 'para'
    'if': 'IF',                                   #Estrutura condicional 'se' 
    'let': 'LET',                                 #Declaração de variáveis com escopo limitado
    'list': 'LIST',                               #Contém linhas de itens com propriedades específicas (atributos). As listas geralmente chamam Procedimentos
    'print_Analysis': 'PRINT_ANALYSIS',           #Apresenta a análise de dados
    'procedure': 'PROCEDURE',                     #Determina a ordem dos eventos em um experimento
    'randomize_Order': 'RANDOMIZE_ORDER',         #Randomiza a ordem de elementos (por exemplo, estímulos)
    'read_Sensor': 'READ_SENSOR',                 #Lê de um sensor ou dispositivo externo
    'response_Recorder': 'RESPONSE_RECORDER',     #Registra a resposta do participante via mouse, teclado, voz, joystick ou outra entrada
    'score_Response': 'SCORE_RESPONSE',           #Avalia e pontua a resposta do participante
    'send_Data': 'SEND_DATA',                     #Envia dados para um sistema ou dispositivo externo
    'sort': 'SORT',                               #Ordena dados com base em critérios específicos
    'sound_Recorder': 'SOUND_RECORDER',           #Grava sons e Habilitar e gravar microfone do computador
    'throw': 'THROW',                             #Lança uma exceção ou erro
    'trial': 'TRIAL',                             #Define um ensaio individual dentro de um bloco, Define o estímulo, Define a resposta correta, Define a resposta errada, Define o tempo limite
    'try': 'TRY',                                 #Inicia um bloco de tratamento de erro   
    'wait': 'WAIT',                               #Espera por um tempo especificado sem alterar a saída visual
    'while': 'WHILE',                             #Estrutura de loop 'enquanto'
}

tokens = [
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'RCOLC',
    'LCOLC',
    'RBRACE',
    'LBRACE',
    'PRINCIPAL',
    'OR',
    'AND',
    'LOWEREQ',
    'MOREEQ',
    'EQUAL',
    'DIFFERENT',
    'LOWERAS',
    'MOREAS',
    'SUMEQUALS',
    'MINUSEQUALS',
    'TIMESEQUALS',
    'DIVIDEEQUALS',
    'MOD',
    'ATTRIBUTION',
    'COMMA',
    'SEMICOL',
    'COLON',
    'VAR',
    'STRING',
    'TEXT',
    'BOOLEANT',
    'BOOLEANF',
    'INTEGER',
    'BOOLTYPE',
] + list(reserved.values())

t_ignore = ' \t'

t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_RCOLC = r'\]'
t_LCOLC = r'\['
t_RBRACE = r'\}'
t_LBRACE = r'\{'
t_PRINCIPAL = r'\$'
t_OR = r'\|\|'
t_AND = r'&&'
t_LOWEREQ = r'<='
t_LOWERAS = r'<'
t_MOREEQ = r'>='
t_MOREAS = r'>'
t_EQUAL = r'=='
t_SUMEQUALS = r'\+='
t_MINUSEQUALS = r'-='
t_TIMESEQUALS = r'\*='
t_DIVIDEEQUALS = r'/='
t_MOD = r'%='
t_ATTRIBUTION = r'='
t_DIFFERENT = r'!='
t_COMMA = r','
t_SEMICOL = r';'
t_COLON = r':'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newLine(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_TEXT(t):
    r"'[^']*'"
    return t

def t_INTEGER(t):
    r'integer|INTEGER|Integer'
    t.type = 'INTEGER'
    return t

def t_BOOLEANT(t):
    r'TRUE|true|True'
    t.type = 'BOOLEANT'
    return t

def t_BOOLEANF(t):
    r'FALSE|False|false'
    t.type = 'BOOLEANF'
    return t

def t_BOOLTYPE(t):
    r'Boolean|boolean'
    t.type = 'BOOLTYPE'
    return t

def t_STRING(t):
    r'string|String|STRING'
    t.type = 'STRING'
    return t

def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'VAR')
    return t


def t_error(t):
    print(f"Caracter errado '{t.value[0]}' na linha {t.lineno}")
    t.lexer.skip(1)

lex.lex()
