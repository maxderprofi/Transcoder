#######################################
# DOKUMENTATION
#######################################
'''
You can change "Tokens" and "Keywoards".
But the key in Tokens only kann be two Chars long!!!

USAGE:
import Lexer
lexer = Lexer(File)             # "File" is the code/ Text/ File (string) you want to transform into a Token Array
tokens = lexer.makeTokens()     # "tokens" is an array with all Tokens


'''

#######################################
# IMPORTS
#######################################

import os
import math
from users.Tokens import *


#######################################
# CONSTANTS
#######################################

DIGITS = '0123456789'
LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
LETTERS_DIGITS = LETTERS + DIGITS



#######################################
# TOKENS
#######################################




# CREATE HELP ARRAYS


class Token:
  def __init__(self, type_, value=None):
    self.type = type_
    self.value = value

  def matches(self, type_, value):
    return self.type == type_ and self.value == value

  def __repr__(self):
    if self.value: return f'{self.type}:{self.value}'
    return f'{self.type}'

#######################################
# LEXER
#######################################

class Lexer:
    def __init__(self, text):
        self.tokens = []
        self.index = 0
        self.text = text
        self.current_char = None
        self.advance()

    def advance(self):
         self.current_char = self.text[self.index] if self.index < len(self.text) else None
         self.index += 1

    def makeTokens(self):
        while self.current_char != None:
            if self.current_char in ' \t':          # Skip Whitespace
              self.advance()
            elif self.current_char == '#':          # Skip comment
              self.advance()
              while self.current_char != '\n':
                self.advance()
                self.advance()
            elif self.current_char in ';\n':        # New Line
                tokens.append(Token(TT_NEWLINE))
                self.advance()
            elif self.current_char in DIGITS:       # Numbers
                self.tokens.append(self.make_number())
            elif self.current_char in LETTERS:      # Identifier
                self.tokens.append(self.make_identifier())
            elif self.current_char == '"':
                self.tokens.append(self.make_string())
            elif self.current_char in first:        # Double chars
                  mom_index = first.index(self.current_char)
                  self.advance()
                  if self.current_char == second[mom_index]:
                      self.tokens.append(Token(doubleTokens[first[mom_index]+second[mom_index]]))
                      self.advance()
                  else:
                      self.tokens.append(Token(Tokens[first[mom_index]]))
            elif self.current_char in Tokens.keys():         # Single chars
                  print("Hallo")
                  self.tokens.append(Token(Tokens[self.current_char]))
                  self.advance()
            else:
                raise CustomError("Unknown Token: " + self.current_char)
        return self.tokens


#######################################
# MAKE FUNCTIONS
#######################################

    def make_number(self):
        num_str = ''
        dot_count = 0
        while self.current_char != None and self.current_char in DIGITS + '.':
          if self.current_char == '.':
            if dot_count == 1: break
            dot_count += 1
          num_str += self.current_char
          self.advance()
        if dot_count == 0:
            return Token(TT_INT, int(num_str))
        return Token(TT_FLOAT, float(num_str))

    def make_string(self):
        string = ''
        escape_character = False
        self.advance()
        escape_characters = {
          'n': '\n',
          't': '\t'
        }

        while self.current_char != None and (self.current_char != '"' or escape_character):
          if escape_character:
            string += escape_characters.get(self.current_char, self.current_char)
          else:
            if self.current_char == '\\':
              escape_character = True
            else:
              string += self.current_char
          self.advance()
          escape_character = False
        self.advance()
        return Token(TT_STRING, string, pos_start)

    def make_identifier(self):
        id_str = ''
        while self.current_char != None and self.current_char in LETTERS_DIGITS + '_':
          id_str += self.current_char
          self.advance()
        tok_type = TT_KEYWORD if id_str in KEYWORDS else TT_IDENTIFIER
        return Token(tok_type, id_str)
