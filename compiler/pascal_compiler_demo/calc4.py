'''
about the syntax demo code
'''

from enum import Enum
import numpy as np

class Type(Enum):

    INTEGER = 'INTEGER'
    PLUS = 'PLUS'
    MINUS = 'MINUS'
    EOF = 'EOF'
    MUL = 'MUL'
    DIV = 'DIV'

op_list = [[Type.PLUS,'+'],[Type.MINUS,'-'],[Type.MUL,'*'],[Type.DIV,'/']]
class Token(object):
    def __init__(self,type,value):
        #token type:INTEGER,PLUS or EOF
        self.type = type
        #roken value:0,1,2,3,4,5,6,7,8,9,'+' or None
        self.value = value
    def __str__(self):
        return 'Token({type},{value})'.format(
            type = self.type,
            value = self.value
        )
    
    def __repr__(self):
        return self.__str__()


class Lexer(object):
    def __init__(self,text):
        #remove the whitespace of the text
        self.text =  text.replace(' ','')
        self.pos = 0
        #self.current_token = None
        self.current_char = self.text[self.pos]



    def error(self):
        raise Exception('invalid character')
    
    def advance(self):
        '''advance the 'pos' pointer and set the current_char variable'''
        self.pos += 1
        if self.pos > len(self.text)-1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]
    
    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        '''return a multi integer from the input'''
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        
        return int(result)

    def get_next_token(self):
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(Type.INTEGER,self.integer())
            
            for index in range(len(op_list)):
                if self.current_char == op_list[index][1]:
                    self.advance()
                    return Token(op_list[index][0],op_list[index][1])
            
            self.error()
        
        return Token(Type.EOF,None)

    
class Interpreter(object):
    def __init__(self,lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()
    
    def error(self):
        raise Exception('invalid syntax')


    def eat(self,token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        token = self.current_token
        self.eat(Type.INTEGER)
        return token.value

    def expr(self):
        result = self.factor()

        while self.current_token.type in (np.array(op_list)[:,0]):
            token = self.current_token
            self.eat(token.type)
            result = eval(str(result)+ token.value+str(self.factor()))

        return result
        
    
def main():
    while True:
        try:
            text = input('calc>')
        except EOFError:
            break
            
        if not text:
            continue

        lexer = Lexer(text)
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        print(result)

if __name__ == '__main__':
    main()
    

    
