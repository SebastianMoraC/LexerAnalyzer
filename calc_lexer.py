import ply.lex as lex
import sys

# list of tokens
tokens = (
   # Reserverd words
    
    'ADDITION',
    'SUBSTRACTION',
    'PRODUCT',
    'DIVIDE',
    'PAREN',
    'ENDPAREN',
    'EXP',
    'JUMP',
    'NUM'
)
t_JUMP = r'\n'
t_ADDITION = r'\+'
t_SUBSTRACTION = r'\-'
t_PRODUCT = r'\*'
t_DIVIDE = r'\/'
t_PAREN = r'\('
t_ENDPAREN  = r'\)'
t_EXP = r'\^'


def t_NUM(t):
    r'\d+(\.\d+)?(\^\d+)?'
    t.value = float(t.value)
    return t
    
def t_error(t):
    print ("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)

def test(data, lexer):
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print (tok)

lexer = lex.lex()

if __name__ == '__main__':
	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
	    fin = 'arithmetic.txt'

    
	f = open(fin, 'r')
	data = f.read()
	print (data)
	lexer.input(data) 
	test(data, lexer)
	input()


