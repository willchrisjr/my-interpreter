import sys
from enum import Enum, auto

# Define an enumeration for different types of tokens
class TokenType(Enum):
    # Single-character tokens
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    LEFT_BRACE = auto()
    RIGHT_BRACE = auto()
    COMMA = auto()
    DOT = auto()
    MINUS = auto()
    PLUS = auto()
    SEMICOLON = auto()
    STAR = auto()
    SLASH = auto()
    EQUAL = auto()
    EQUAL_EQUAL = auto()
    BANG = auto()
    BANG_EQUAL = auto()
    LESS = auto()
    LESS_EQUAL = auto()
    GREATER = auto()
    GREATER_EQUAL = auto()
    STRING = auto()
    NUMBER = auto()
    IDENTIFIER = auto()
    
    # Reserved words
    AND = auto()
    CLASS = auto()
    ELSE = auto()
    FALSE = auto()
    FOR = auto()
    FUN = auto()
    IF = auto()
    NIL = auto()
    OR = auto()
    PRINT = auto()
    RETURN = auto()
    SUPER = auto()
    THIS = auto()
    TRUE = auto()
    VAR = auto()
    WHILE = auto()
    
    # End-of-file token
    EOF = auto()

# Define a class to represent a token
class Token:
    def __init__(self, type, lexeme, literal, line):
        self.type = type  # The type of token
        self.lexeme = lexeme  # The actual text of the token
        self.literal = literal  # The literal value (if any)
        self.line = line  # The line number where the token appears

    def __str__(self):
        return f"{self.type.name} {self.lexeme} {self.literal if self.literal is not None else 'null'}"

# Define a class to scan the source code and generate tokens
class Scanner:
    def __init__(self, source):
        self.source = source  # The source code to scan
        self.tokens = []  # List to hold the generated tokens
        self.start = 0  # Start position of the current token
        self.current = 0  # Current position in the source code
        self.line = 1  # Current line number
        self.had_error = False  # Flag to indicate if an error occurred
        self.keywords = {  # Dictionary of reserved words
            "and": TokenType.AND,
            "class": TokenType.CLASS,
            "else": TokenType.ELSE,
            "false": TokenType.FALSE,
            "for": TokenType.FOR,
            "fun": TokenType.FUN,
            "if": TokenType.IF,
            "nil": TokenType.NIL,
            "or": TokenType.OR,
            "print": TokenType.PRINT,
            "return": TokenType.RETURN,
            "super": TokenType.SUPER,
            "this": TokenType.THIS,
            "true": TokenType.TRUE,
            "var": TokenType.VAR,
            "while": TokenType.WHILE
        }

    # Method to scan all tokens in the source code
    def scan_tokens(self):
        while not self.is_at_end():
            self.start = self.current  # Update the start position
            self.scan_token()  # Scan the next token

        self.tokens.append(Token(TokenType.EOF, "", None, self.line))  # Add EOF token at the end
        return self.tokens

    # Method to scan a single token
    def scan_token(self):
        c = self.advance()  # Get the next character
        if c == '(':
            self.add_token(TokenType.LEFT_PAREN)
        elif c == ')':
            self.add_token(TokenType.RIGHT_PAREN)
        elif c == '{':
            self.add_token(TokenType.LEFT_BRACE)
        elif c == '}':
            self.add_token(TokenType.RIGHT_BRACE)
        elif c == ',':
            self.add_token(TokenType.COMMA)
        elif c == '.':
            self.add_token(TokenType.DOT)
        elif c == '-':
            self.add_token(TokenType.MINUS)
        elif c == '+':
            self.add_token(TokenType.PLUS)
        elif c == ';':
            self.add_token(TokenType.SEMICOLON)
        elif c == '*':
            self.add_token(TokenType.STAR)
        elif c == '=':
            self.add_token(TokenType.EQUAL_EQUAL if self.match('=') else TokenType.EQUAL)
        elif c == '!':
            self.add_token(TokenType.BANG_EQUAL if self.match('=') else TokenType.BANG)
        elif c == '<':
            self.add_token(TokenType.LESS_EQUAL if self.match('=') else TokenType.LESS)
        elif c == '>':
            self.add_token(TokenType.GREATER_EQUAL if self.match('=') else TokenType.GREATER)
        elif c == '/':
            if self.match('/'):  # Handle comments
                while self.peek() != '\n' and not self.is_at_end():
                    self.advance()
            else:
                self.add_token(TokenType.SLASH)
        elif c == '"':
            self.string()  # Handle string literals
        elif c.isdigit():
            self.number()  # Handle number literals
        elif self.is_alpha(c):
            self.identifier()  # Handle identifiers and reserved words
        elif c == '\n':
            self.line += 1  # Handle new lines
        elif c.isspace():
            pass  # Ignore whitespace
        else:
            self.error(self.line, f"Unexpected character: {c}")

    # Method to handle string literals
    def string(self):
        while self.peek() != '"' and not self.is_at_end():
            if self.peek() == '\n':
                self.line += 1
            self.advance()

        if self.is_at_end():
            self.error(self.line, "Unterminated string.")
            return

        self.advance()  # Consume the closing quote
        value = self.source[self.start + 1 : self.current - 1]  # Extract the string value
        self.add_token(TokenType.STRING, value)

    # Method to handle number literals
    def number(self):
        while self.peek().isdigit():
            self.advance()

        if self.peek() == '.' and self.peek_next().isdigit():
            self.advance()  # Consume the decimal point

            while self.peek().isdigit():
                self.advance()

        value = float(self.source[self.start:self.current])  # Convert the number to a float
        self.add_token(TokenType.NUMBER, value)

    # Method to handle identifiers and reserved words
    def identifier(self):
        while self.is_alphanumeric(self.peek()):
            self.advance()

        text = self.source[self.start:self.current]
        type = self.keywords.get(text, TokenType.IDENTIFIER)  # Check if the identifier is a reserved word
        self.add_token(type)

    # Helper method to check if a character is a letter or underscore
    def is_alpha(self, c):
        return c.isalpha() or c == '_'

    # Helper method to check if a character is alphanumeric or underscore
    def is_alphanumeric(self, c):
        return c.isalnum() or c == '_'

    # Helper method to check if the end of the source code is reached
    def is_at_end(self):
        return self.current >= len(self.source)

    # Helper method to advance to the next character
    def advance(self):
        self.current += 1
        return self.source[self.current - 1]

    # Helper method to match the next character with an expected character
    def match(self, expected):
        if self.is_at_end():
            return False
        if self.source[self.current] != expected:
            return False
        self.current += 1
        return True

    # Helper method to peek at the current character without consuming it
    def peek(self):
        if self.is_at_end():
            return '\0'
        return self.source[self.current]

    # Helper method to peek at the next character without consuming it
    def peek_next(self):
        if self.current + 1 >= len(self.source):
            return '\0'
        return self.source[self.current + 1]

    # Helper method to add a token to the list of tokens
    def add_token(self, type, literal=None):
        text = self.source[self.start:self.current]
        self.tokens.append(Token(type, text, literal, self.line))

    # Helper method to report an error
    def error(self, line, message):
        print(f"[line {line}] Error: {message}", file=sys.stderr)
        self.had_error = True

# Main function to run the scanner
def main():
    print("Logs from your program will appear here!", file=sys.stderr)

    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    if command != "tokenize":
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)

    with open(filename) as file:
        file_contents = file.read()

    scanner = Scanner(file_contents)
    tokens = scanner.scan_tokens()

    for token in tokens:
        print(token)

    if scanner.had_error:
        exit(65)

if __name__ == "__main__":
    main()