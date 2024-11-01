import ply.yacc as yacc
from Lexico import tokens

precedence = (
    ('left', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE'),
    ('left', 'LPAREN', 'RPAREN'),
    ('left', 'STRING', 'BOOLEANF', 'BOOLEANT', 'INTEGER'),
)

# ESTRUTURA PRINCIPAL DO CODIGO UM SIMBULO DE INICIO E FIM
#ENTRADA:  $ 
#SAIDA: $
#PRE-CONDICAOO: NONE 
#POS-CONDICAO: NONE
def p_start(p):
    '''start : principal script principal'''
    p[0] = ('start', p[1], p[2], p[3])

# ESTRUTURA DO SIMBULO DE PRINCIPAL
#ENTRADA: $ 
#SAIDA: $
#PRE-CONDICAOO: NONE 
#POS-CONDICAO: NONE
def p_principal(p):
    'principal : PRINCIPAL'
    p[0] = p[1]

# ESTRUTURA DE CORPO DO CODIGO RECURSIVO
#ENTRADA: NONE 
#SAIDA: NONE
#PRE-CONDICAOO: NONE 
#POS-CONDICAO: NONE
def p_script(p):
    '''script : call script
              | call'''
    if len(p) == 3:
        p[0] = ('script', p[1], p[2])
    else:
        p[0] = ('script', p[1])

# ESTRUTURA DE CHAMADA DE TODAS AS FUNCOES DO PROGRAMA
#ENTRADA: QUALQUER FUNCAO DO CODIGO
#SAIDA: NONE
#PRE-CONDICAOO: NONE
#POS-CONDICAO: NONE
def p_call(p):
    '''call : declaration 
            | attribution
            | expression_condicional
            | math_op
            | connect
            | while
            | for
            | flag
            | flag_declaration
            | aggregateblock
            | trial
            | aggregatetrial
            | tryc
            | diplayImage
            | displayMovie
            | displaySound
            | displayText
            | experiment_desing
            | list
            | procedure
            | randomize
            | readSensor
            | responceRecorder
            | responseScore
            | analyzeData
            | block
            | displayFeedback
            | experiment
            | filter
            | let
            | printAnalysis
            | sendData
            | sort
            | soundRecorder
            | throw
            | wait
            | call_empty'''
    p[0] = p[1]

# CHAMADA VAZIA, POSSIBILITA O FIM DO CALL COM UMA ENTRADA NULA
#ENTRADA: NULL
#SAIDA: NULL
#PRE-CONDICAOO: NONE  
#POS-CONDICAO: NONE
def p_call_empty(p):
    'call_empty :'
    p[0] = None

#DECLARACAO DE VARIAVEIS
#ENTRADA: UM TIPO (INT, STRING, BOOL), UMA NOME VALIDO DE VARIAVEL COM OU SEM ATRIBUICAO DOS SEUS REPESCTIVOS VALORES 
#SAIDA: NONE 
#PRE-CONDICAOO: ESTAR DENTRO DA ESTRUTURA PRINCIPAL  
#POS-CONDICAO: NONE
def p_declaration(p):
    '''declaration : types attribution 
                   | string VAR ATTRIBUTION LPAREN TEXT RPAREN
                   | booltype VAR ATTRIBUTION BOOLEANT
                   | booltype VAR ATTRIBUTION BOOLEANF
                   | types VAR 
                   | string VAR 
                   | booltype VAR'''
    if len(p) == 5:
        p[0] = ('declaration', p[1], p[2], p[3], p[4])
    else:
        p[0] = ('declaration', p[1], p[2])

# EXPRESSAO CONDICIONAL IF COM OU SEM ELSE
#ENTRADA: ENTRA COM UM 'IF', DENTRO DE PARENTESES A LOFICA CONDICIONAL, DENTRO DE CHAVES O CORPO DA EXECUCAO, ELSE APOS AS CHAVES
#SAIDA: NONE 
#PRE-CONDICAOO: ESTAR DENTRO DA ESTRUTURA PRINCIPAL  
#POS-CONDICAO: NONE
def p_expression_condicional(p):
    '''expression_condicional : if_expression LPAREN idnum logic_exp idnum RPAREN LBRACE script RBRACE
                              | if_expression LPAREN idnum logic_exp idnum RPAREN LBRACE script RBRACE ELSE LBRACE script RBRACE'''
    if len(p) == 10:
        p[0] = ('if', p[3], p[4], p[5], p[8])
    else:
        p[0] = ('if_else', p[3], p[4], p[5], p[8], p[12])

# ESTRUTURA WHILE DE REPETICAO
#ENTRADA: UMA EXPRECAO LOGICA
#SAIDA: NONE
#PRE-CONDICAO: ESTAR DENTRO DA ESTRUTURA PRINCIPAL 
#POS-CONDICAO: NONE
def p_while(p):
    '''while : WHILE LPAREN idnum logic_exp idnum RPAREN LBRACE script RBRACE'''
    p[0] = ('while', p[3], p[4], p[5], p[8])

# ESTRUTURA 'FOR' DE REPETICAO
#ENTRADA: SEPARADOS POR ';' PERMITE A ENTRADA DE UMA DECLARACAO EXPRECAO LOGICA E OPERACAO MATEMATICA EX:i++ 
#SAIDA: NONE
#PRE-CONDICAO: ESTAR DENTRO DA ESTRUTURA PRINCIPAL 
#POS-CONDICAO: NONE
def p_for(p):
    '''for : FOR LPAREN declaration SEMICOL idnum logic_exp idnum SEMICOL attribution RPAREN LBRACE script RBRACE'''
    p[0] = ('for', p[3], p[5], p[6], p[7], p[9], p[12])

# ESTRUTURA PARA O LEXICO 'IF'
#ENTRADA: LEXICO IF
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_if_expression(p):
    'if_expression : IF'
    p[0] = p[1]

# UNIAO AS EXPRESSOES LOGICAS MATEMATICAS
#ENTRADA: QUALQUE EXPRESSAO LOGICA MATEMATICA
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_logic_exp(p):
    '''logic_exp : EQUAL
                 | OR
                 | AND
                 | LOWEREQ
                 | LOWERAS
                 | DIFFERENT
                 | MOREAS
                 | MOREEQ'''
    p[0] = p[1]

# EXPRESSAO DE DECLARACAO FLAG
#ENTRADA: LEXICO 'flag', VARIAVEL  
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_flag(p):
    'flag : FLAG VAR'
    p[0] = ('flag', p[2])

# PONTO DE RETORNO/AVANCO DO FLAG
#ENTRADA: VAR DECLARADA NA DECLARACAO SEGUIDA DE ':'
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_flag_declaration(p):
    'flag_declaration : VAR COLON'
    p[0] = ('flag_declaration', p[1])

# ESTRUTURA PARA O LEXICO 'integer'
#ENTRADA: LEXICO integer
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_types(p):
    '''types : INTEGER'''
    p[0] = p[1]

# ESTRUTURA PARA O LEXICO 'boolean'
#ENTRADA: LEXICO boolean
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_booltype(p):
    '''booltype : BOOLTYPE'''
    p[0] = p[1]

# ESTRUTURA PARA A FUNCAO DE CONECT DEVICE
#ENTRADA: O NOME DO DISPOSITIVO
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_connect_device(p):
    '''connect : CONNECT_DEVICE LPAREN TEXT RPAREN'''
    p[0] = ('connect', p[2])

# ESTRUTURA PARA O LEXICO 'string'
#ENTRADA: LEXICO string
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_stringtype(p):
    '''string : STRING'''
    p[0] = p[1]

# ESTRUTURA AUXILIAR DE DACLARACAO DE VARIAVEL
#ENTRADA: UMA VARIAVEL VALIDA
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_ident(p):
    'ident : VAR'
    p[0] = p[1]

# ESTRUTURA DE UNIAO DE VARIAVEIS E NUMEROS
#ENTRADA: UMA VARIAVEL OU UM NUMERO
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_idnum(p):
    '''idnum : ident
             | NUMBER'''
    p[0] = p[1]

#ESTRUTURA PARA ATRIBUIÇÃO 
# ENTRADA : UMA VARIAVEL '=' UMA EXPRESSÃO MATEMÁTICA, UM ID OU NUMERO, UM TEXTO, UMA EXPREÇÃO LOGICA
# SAIDA : NONE
#PRE-CODIÇÃO : NONE
#POS-CONDIÇÃO : NONE
def p_attribution(p):
    '''attribution : VAR ATTRIBUTION math_op
                   | VAR ATTRIBUTION idnum
                   | VAR ATTRIBUTION TEXT
                   | VAR ATTRIBUTION idnum logic_exp idnum '''
    if len(p) == 4:
        p[0] = ('attribution', p[1], p[2], p[3])
    elif len(p) == 6:
        p[0] = ('attribution', p[1], p[2], (p[3], p[4], p[5]))

# ESTRUTURA DE UNIAO DAS EXPRESSOES MATEMATICAS
#ENTRADA: UMA EXPRESSAO MATEMATICA
#SAIDA: NONE
#PRE-CONDICAO: ESTAR NA ESTRUTURA PRINCIPAL
#POS-CONDICAO: NONE
def p_math_op(p):
    '''math_op : math_op PLUS math_op
               | math_op MINUS math_op
               | math_op TIMES math_op
               | math_op DIVIDE math_op
               | idnum'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ('math_op', p[2], p[1], p[3])

# ESTRUTURA PARA A EXPRESSAO MATEMATICA DE SOMA E ATRIBUICAO
#ENTRADA: UMA VARIAVEL OU NUMERO, '+=', VARIAVEL OU NUMERO 
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_expression_sumequals(p):
    'expression_sumequals : idnum SUMEQUALS idnum'
    p[0] = ('sumequals', p[1], p[3])

# ESTRUTURA PARA A EXPRESSAO MATEMATICA DE SUBTRACAO E ATRIBUICAO
#ENTRADA: UMA VARIAVEL OU NUMERO, '-=', VARIAVEL OU NUMERO 
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_expression_minusquals(p):
    'expression_minusequals : idnum MINUSEQUALS idnum'
    p[0] = ('minusequals', p[1], p[3])

# ESTRUTURA PARA A EXPRESSAO MATEMATICA DE MULTIPLICACAO E ATRIBUICAO
#ENTRADA: UMA VARIAVEL OU NUMERO, '*=', VARIAVEL OU NUMERO 
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_expression_timesequals(p):
    'expression_timesequals : idnum TIMESEQUALS idnum'
    p[0] = ('timesequals', p[1], p[3])

# ESTRUTURA PARA A EXPRESSAO MATEMATICA DE DIVISAO E ATRIBUICAO
#ENTRADA: UMA VARIAVEL OU NUMERO, '=/', VARIAVEL OU NUMERO 
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_expression_divideequals(p):
    'expression_divideequals : idnum DIVIDEEQUALS idnum'
    p[0] = ('divideequals', p[1], p[3])

# ESTRUTURA PARA A EXPRESSAO MATEMATICA DE MODULO
#ENTRADA: UMA VARIAVEL OU NUMERO, '%', VARIAVEL OU NUMERO 
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_expression_mod(p):
    'expression_mod : idnum MOD idnum'
    p[0] = ('mod', p[1], p[3])

# ESTRUTURA PARA O LEXICO 'AGGREGATEBLOCK'
#ENTRADA:  DUAS VARIAVEIS DO TIPO BLOCK
#SAIDA: NONE
#PRE-CONDICAO:  TER DUAS VARIAVES DECLARADAS 
#POS-CONDICAO: NONE
def p_aggregateblock(p):
    '''aggregateblock : AGGREGATE_BLOCK LPAREN VAR COLON VAR RPAREN'''
    p[0] = ('aggregate_block', p[3], p[5])

# ESTRUTURA PARA O LEXICO 'TRIAL'
#ENTRADA: UMA VARIAVEL ,UM INTEIRO ,  UMA RECURSIVIDADE DE STRINGS ; RECURSIVIDADE DE STRINGS , INTEIRO  
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_trial(p):
    '''trial : TRIAL LPAREN TEXT SEMICOL TEXT SEMICOL TEXT SEMICOL idnum RPAREN'''
    p[0] = ('trial',p[9])


# ESTRUTURA PARA O LEXICO 'AGGREGATETRIAL'
#ENTRADA: DUAS VARIAVES DO TIPO TRIAL
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_aggregatetrial(p):
    '''aggregatetrial : AGGREGATE_TRIAL LPAREN VAR COLON VAR RPAREN'''
    p[0] = ('aggregat_trial', p[3], p[5])

# ESTRUTURA PARA O LEXICO 'TRY'
#ENTRADA: todo UM SCRIPT PARA O TRY  
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_tryc(p):
    '''tryc : TRY LBRACE script RBRACE catch '''
    p[0] = ('try', p[3], p[5])

# ESTRUTURA PARA O  'CATCH' 
#ENTRADA: O LEXICO CATCH
#SAIDA: NONE
#PRE-CONDICAO:  ESTAR LOGO APÓS O '}' DO TRY
#POS-CONDICAO: NONE
def p_catch(p):
    '''catch : CATCH LPAREN VAR RPAREN LBRACE script RBRACE'''
    p[0] = ('catch', p[3], p[6])


# ESTRUTURA PARA O LEXICO 'DISPLAYIMAGE'
#ENTRADA: UM DISPOSITIVO DE SAIDA DE IMAGEM
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_displayImage(p):
    '''diplayImage : DISPLAY_IMAGE LPAREN TEXT RPAREN'''
    p[0] = ('display_Image', p[3])

# ESTRUTURA PARA O LEXICO 'DISPLAYMOVIE'
#ENTRADA: O NOME DA UM ARQUIVO DE VIDEO SEGUIDO DE .AVI||.MP4||.WVM
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE 
def p_displayMovie(p):
    '''displayMovie : DISPLAY_MOVIE LPAREN TEXT RPAREN'''
    p[0] = ('display_Movie', p[3])

# ESTRUTURA PARA O LEXICO 'DISPLAYSOUND'
#ENTRADA: NOME DE UM ARQUIO DE AUDIO SEGUIDO DE .WAV||.MP3||.WMA
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_displaySound(p):
    '''displaySound : DISPLAY_SOUND LPAREN TEXT RPAREN'''
    p[0] = ('display_Sound', p[3])

# ESTRUTURA PARA O LEXICO 'DISPLAYTEXT'
#ENTRADA: O TEXTO QUE SERA INSERIDO 
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_displayText(p):
    '''displayText : DISPLAY_TEXT LPAREN TEXT RPAREN'''
    p[0] = ('display_Text', p[3])

#Sequência experimental completa, composta de diversas etapas a serem definidas
#ENTRADA: UMA RECURSIVIDDE DE STRINGS DEFININDO AS ESTAPAS
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_experiment(p):
    'experiment : EXPERIMENT LPAREN group_list RPAREN'
    p[0] = ('experiment', p[3])
    
    
#Define o design do experimento, incluindo between-subjects e within-subjects
#ENTRADA: TIPO DO DESIGN , 
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_experiment_desing(p):
    '''experiment_desing : EXPERIMENT_DESING LPAREN design_details RPAREN '''
    p[0] = ('experiment_desing', p[3])

#FUNCAO AUXILIAR PARA DEFINICAO DEOS GRUPOS E DAS CONDICOES 
#ENTRADA: DEFINI IMA RECURSAO DE GRUPOS SEGUIDO DE UMA RECURSAO DE CONDICAOES 
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_design_details(p):
    '''design_details : TEXT COLON groups conditions'''
    p[0] = (p[3], p[4])

#AUXILIAR PARA A RECURSAO DE GRUPOS
#ENTRADA: NONE
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_groups(p):
    '''groups : group_list SEMICOL'''
    p[0] = p[1]

#RECURSAO DE GRUPOS 
#ENTRADA: OS NOMES DOS GRUPOS SEPARADOS POR VIRGOLA
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_group_list(p):
    '''group_list : VAR COMMA group_list
                  | VAR'''
    if len(p) == 4:
        p[0] = [p[1]] + p[3]
    else:
        p[0] = [p[1]]

#FUNÇAO AUXILIAR DE RECURSAO DE CONDIÇOES
#ENTRADA: NONE
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_conditions(p):
    '''conditions : VAR LCOLC condition_list RCOLC '''
    p[0] = (p[1], p[3])

#FUNCAO DE RECURSAO DE CONDICOES 
#ENTRADA: ENTRE ASPAS SIMPLES AS CONDICOES 
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_condition_list(p):
    '''condition_list : TEXT COMMA condition_list
                      | TEXT'''
    if len(p) == 4:
        p[0] = [p[1]] + p[3]
    else:
        p[0] = [p[1]]

#Contém linhas de itens com propriedades específicas (atributos). As listas geralmente chamam Procedimentos
#ENTRADA: UM NOME VALIDO DE VARIAVEL E ENTRE CHAVES UM NEMERO ( UM ARRAY)
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_list(p):
    '''list : LIST VAR LCOLC NUMBER RCOLC'''
    p[0] = ('list', p[4])

#Determina a ordem dos eventos em um experimento
#ENTRADA: UMA RECURSAO DE VARIAVEIS
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_procedure(p):
    '''procedure : PROCEDURE LPAREN group_list RPAREN'''
    p[0] = ('procedure', p[3])

#tranforma em aleatoria a ordem de elementos (por exemplo, estímulos)
#ENTRADA: 
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_randomize(p):
    '''randomize : RANDOMIZE_ORDER LPAREN group_list RPAREN'''
    p[0] = ('randomize', p[3])

#Lê de um sensor ou dispositivo externo
#ENTRADA: O NOME DE UM SENSOR ENTRE ASPAS DUPLAS 
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE'
def p_readSensor(p):
    '''readSensor : READ_SENSOR LPAREN TEXT RPAREN'''
    p[0] = ('read_Sensor', p[3])

#Registra a resposta do participante via mouse, teclado, voz, joystick ou outra entrada
#ENTRADA: RECEBE UMA VARIAVEL PARA ARMAZENAR AS RESPOSTAS DO PARTICIPANTE
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_responceRecorder(p):
    '''responceRecorder : RESPONSE_RECORDER LPAREN VAR RPAREN'''
    p[0] = ('responce_Recorder', p[3])

#Avalia e pontua a resposta do participante
#ENTRADA: RECEBE A VARIAVEL QUE GARDA A RESPOSTA DO PARTICIPANTE E DEFINE UMA STRING COMO AVALIACAO 
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_responseScore(p):
    '''responseScore : SCORE_RESPONSE LPAREN VAR COMMA TEXT RPAREN'''
    p[0] = ('responseScore', p[3], p[5])

# ESTRUTURA PARA O LEXICO 'ANALYZEDATA'
#ENTRADA: UMA VARIAVEL   
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_analyzeData(p):
    '''analyzeData : ANALYZE_DATA LPAREN VAR RPAREN'''
    p[0] = ('analyze_Data', p[3])

# ESTRUTURA PARA O LEXICO 'BLOCK'
#ENTRADA: UMA OU MAIS VARIAVEIS   
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_block(p):
    '''block : BLOCK group_list'''
    p[0] = ('block', p[2])

# ESTRUTURA PARA O LEXICO 'DISPLAYFEEDBACK'
#ENTRADA: UMA VARIAVEL QUE CONTEM UM EXPERIMENTO
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_displayFeedback(p):
    '''displayFeedback : DISPLAY_FEEDBACK LPAREN TEXT RPAREN'''
    p[0] = ('display_Feedback', p[3])



#Filtra dados com base em critérios específicos
#ENTRADA: CRITERIOS ESPECIFICOS ESCRITOS ENTRE ASPAS SIMPLES E SEPARADOS POR VIRGOLA
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_filter(p):
    '''filter : FILTER LPAREN TEXT RPAREN'''
    p[0] = ('filter', p[3])

# ESTRUTURA PARA O LEXICO 'LET'
#Declaração de variáveis com escopo limitado
#ENTRADA: UMA VARIAVEL, UM NUMERO||VARIAVEL||STRING PARA DEFINICAO DE ESCOPO
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_let(p):
    '''let : LET VAR LPAREN TEXT RPAREN
           | LET VAR LPAREN idnum RPAREN'''
    p[0] = ('let', p[2], p[4])

#Apresenta a análise de dados
#ENTRADA: UMA OU MAIS VARIAVEIS DE PROCEDIMENTOS
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_printAnalysis(p):
    '''printAnalysis : PRINT_ANALYSIS LPAREN group_list RPAREN'''
    p[0] = ('print_Analysis', p[3])

#Envia dados para um sistema ou dispositivo externo
#ENTRADA: UMA RECURSAO DE VARIAVEIS A SER ENVIANDAS PARA O DISPOSITIVO DECLARADO COM UMA STRING ENTRE ASPAS DUPLAS
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_sendData(p):
    '''sendData : SEND_DATA LPAREN group_list COLON TEXT RPAREN'''
    p[0] = ('send_Data', p[4], p[6])

#Ordena dados com base em critérios específicos
#ENTRADA: ORDENA UM CONJUTO DE VARIAVEIS
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_sort(p):
    '''sort : SORT LPAREN group_list RPAREN'''
    p[0] = ('sort', p[3])

#Grava sons e Habilitar e gravar microfone do computador
#ENTRADA: UMA VARIAVEL PARA GUARDAR A GRAVAÇAO, NOME DO DISPOSITIVO QUE IRA GRAVAR
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_soundRecorder(p):
    '''soundRecorder : SOUND_RECORDER LPAREN VAR COMMA TEXT RPAREN'''
    p[0] = ('sound_Recorder', p[3], p[5])

#Lança uma exceção ou erro
#ENTRADA: NONE
#SAIDA: RETORNA UMA MENSAGEM NA TELA COM A FUNCAO DISPLAYTEXT
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE'
def p_throw(p):
    '''throw : THROW LPAREN displayText RPAREN'''
    p[0] = ('throw', p[3])



#Espera por um tempo especificado sem alterar a saída visual
#ENTRADA: RECEBE UM NUMERO PARA ESPERA OU NÃO PARA UM TEMPO ESPECIFICO PRÉ PROGRAMADO
#SAIDA: NONE
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE'
def p_wait(p):
    '''wait : WAIT LPAREN NUMBER RPAREN
            | WAIT LPAREN RPAREN
    '''
    if len(p) == 5:
        p[0] = ('wait', p[3])
    else:
        p[0] = ('wait', None)

#FUNCAP DE ERRO CASO ENCONTRE UM ERRO SINTATICO 
#ENTRADA: NONE
#SAIDA: MENSAGEM DE ERRO
#PRE-CONDICAO:  NONE
#POS-CONDICAO: NONE
def p_error(p):
    print(f'Syntax error at {p !r}')

# CRIA O PARSER YACC
parser = yacc.yacc()
