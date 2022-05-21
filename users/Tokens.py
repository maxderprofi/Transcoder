
Tokens = {
    '+'     	    : 'TT_PLUS',
    '-'    	        : 'TT_MINUS',
    '*'      	    : 'TT_MUL',
    '/'      	    : 'TT_DIV',
    '='			    : 'TT_EQ',
    '%'             : 'TT_MODULO',
    '|'             : 'TT_B_OR',
    '&'             : 'TT_B_AND',
    '!'             : 'TT_NOT',
    '<'             : 'TT_LT',
    '>'             : 'TT_GT',
    '('          	: 'TT_LPAREN',
    ')'   	        : 'TT_RPAREN',
    '{'             : 'TT_LSQUARE',
    '}'             : 'TT_RSQUARE',
    '['             : 'TT_RWPAREN',
    ']'             : 'TT_LWPAREN',
    ';'             : 'TT_SEMIKOLON',
    ','		        : 'TT_COMMA',
    '.'             : 'TT_DOT',

    # Double Tokens
    '**'            : 'TT_POW',
    '=>'            : 'TT_PFEIL',
    '||'            : 'TT_OR',
    '&&'            : 'TT_AND',
    '=='            : 'TT_EE',
    '!='            : 'TT_NE',
    '<='            : 'TT_LTE',
    '>='            : 'TT_GTE',
    '+='            : 'TT_PLUS_EQUAL',
    '-='            : 'TT_MINUS_EQUAL',
    '*='            : 'TT_MUL_EQUAL',
    '/='            : 'TT_DIV_EQUAL',
    '%='            : 'TT_MOD_EQUAL',
    '>>'            : 'TT_B_RR',
    '<<'            : 'TT_B_RL'
}

KEYWORDS = [
  'FALSE',
  'TRUE',
  'NONE',
  'NOT',
  'OR',
  'AND',
  'ELSE',
  'IF',
  'ELIF',
  'RETURN',
  'YIELD',
  'BREAK',
  'PASS',
  'CONTINUE',
  'IMPORT',
  'CLASS',
  'DEF',
  'FROM',
  'AS',
  'DEL',
  'IS',
  'LAMBDA',
  'RAISE',
  'TRY',
  'EXCEPT',
  'FINAL',
  'GLOBAL',
  'FOR',
  'WHILE',
  'IN',
  'WITH'
]

TT_INT		    	= 'INT'
TT_FLOAT    	    = 'FLOAT'
TT_STRING		    = 'STRING'
TT_IDENTIFIER   	= 'IDENTIFIER'
TT_KEYWORD		    = 'KEYWORD'
TT_COMMENT          = 'COMMENT'
TT_NEWLINE		    = 'NEWLINE'
TT_EOF				= 'EOF'

doubleTokens = {}
for key, val in Tokens.items():
    if len(key) == 2:
        doubleTokens[key] = val
    elif len(key) >= 3:
        raise CustomError("Value can´t be longer than two Chars (Tokens)")



for Token in doubleTokens:
    Tokens.pop(Token)

first  = [val[0] for val in doubleTokens.keys()]
second = [val[1] for val in doubleTokens.keys()]
