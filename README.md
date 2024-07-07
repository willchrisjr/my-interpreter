
# Tokenizer

This project is a tokenizer (or lexical analyzer) written in Python. It reads a source code file, breaks it down into a series of tokens, and prints these tokens. This is a fundamental step in the process of interpreting or compiling a programming language.

## Table of Contents

- [Overview](#overview)
- [Token Types](#token-types)
- [Classes](#classes)
  - [TokenType](#tokentype)
  - [Token](#token)
  - [Scanner](#scanner)
- [Usage](#usage)
- [Error Handling](#error-handling)
- [Example](#example)

## Overview

The tokenizer reads the source code character by character, identifies meaningful sequences (tokens), and categorizes them. Tokens can represent keywords, operators, identifiers, literals, and other syntactic elements.

## Token Types

The `TokenType` enumeration defines the different types of tokens that the tokenizer can recognize. These include:

- Single-character tokens: `LEFT_PAREN`, `RIGHT_PAREN`, `LEFT_BRACE`, `RIGHT_BRACE`, `COMMA`, `DOT`, `MINUS`, `PLUS`, `SEMICOLON`, `STAR`, `SLASH`, `EQUAL`, `BANG`, `LESS`, `GREATER`
- One or two character tokens: `EQUAL_EQUAL`, `BANG_EQUAL`, `LESS_EQUAL`, `GREATER_EQUAL`
- Literals: `STRING`, `NUMBER`, `IDENTIFIER`
- Keywords: `AND`, `CLASS`, `ELSE`, `FALSE`, `FOR`, `FUN`, `IF`, `NIL`, `OR`, `PRINT`, `RETURN`, `SUPER`, `THIS`, `TRUE`, `VAR`, `WHILE`
- End-of-file token: `EOF`

## Classes

### TokenType

The `TokenType` class is an enumeration that defines all possible types of tokens. It uses the `auto()` function to automatically assign values to the enumeration members.

### Token

The `Token` class represents a token. It has the following attributes:

- `type`: The type of the token (an instance of `TokenType`).
- `lexeme`: The actual text of the token.
- `literal`: The literal value of the token (if any).
- `line`: The line number where the token appears.

The `__str__` method provides a string representation of the token for easy printing.

### Scanner

The `Scanner` class is responsible for scanning the source code and generating tokens. It has the following attributes:

- `source`: The source code to scan.
- `tokens`: A list to hold the generated tokens.
- `start`: The start position of the current token.
- `current`: The current position in the source code.
- `line`: The current line number.
- `had_error`: A flag to indicate if an error occurred.
- `keywords`: A dictionary of reserved words.

#### Methods

- `scan_tokens()`: Scans all tokens in the source code and returns the list of tokens.
- `scan_token()`: Scans a single token.
- `string()`: Handles string literals.
- `number()`: Handles number literals.
- `identifier()`: Handles identifiers and reserved words.
- `is_alpha(c)`: Checks if a character is a letter or underscore.
- `is_alphanumeric(c)`: Checks if a character is alphanumeric or underscore.
- `is_at_end()`: Checks if the end of the source code is reached.
- `advance()`: Advances to the next character.
- `match(expected)`: Matches the next character with an expected character.
- `peek()`: Peeks at the current character without consuming it.
- `peek_next()`: Peeks at the next character without consuming it.
- `add_token(type, literal=None)`: Adds a token to the list of tokens.
- `error(line, message)`: Reports an error.

## Usage

To use the tokenizer, run the script with the `tokenize` command followed by the filename of the source code to be tokenized:

```sh
python your_program.py tokenize <filename>
```

For example:

```sh
python your_program.py tokenize example.txt
```

## Error Handling

The `Scanner` class includes basic error handling. If an unexpected character is encountered, an error message is printed to `stderr`, and the `had_error` flag is set to `True`. If an unterminated string is encountered, an error message is printed, and the scanning process continues.

## Example

Consider the following source code in a file named `example.txt`:

```txt
var x = 10;
print(x);
```

Running the tokenizer on this file:

```sh
python your_program.py tokenize example.txt
```

Will produce the following output:

```txt
VAR var null
IDENTIFIER x null
EQUAL = null
NUMBER 10 10.0
SEMICOLON ; null
PRINT print null
LEFT_PAREN ( null
IDENTIFIER x null
RIGHT_PAREN ) null
SEMICOLON ; null
EOF  null
```

This output shows the sequence of tokens identified by the tokenizer, including their types, lexemes, and literal values (if any).

## Conclusion

This tokenizer is a fundamental component of a compiler or interpreter. It breaks down source code into tokens, which can then be used for parsing and further processing.


# Detailed explanation of features and functionality



### Braces

Extended the scanner to recognize braces in addition to parentheses. Here are the key functions:

1. Updated the `TokenType` enum to include `LEFT_BRACE` and `RIGHT_BRACE`.
2. Modified the `scan_token` method in the `Scanner` class to recognize '{' and '}' characters and create the appropriate tokens.

The scanner  handles:
- Left parenthesis: '('
- Right parenthesis: ')'
- Left brace: '{'
- Right brace: '}'
- Whitespace: ignored
- Any other character: reported as an unexpected character

### Token Output

The output format remains the same, with the new brace tokens following the established pattern:

```
<token_type> <lexeme> <literal>
```

For example:
```
LEFT_BRACE { null
RIGHT_BRACE } null
```



### Additional Single-Character Tokens

Extended the scanner to recognize several new single-character tokens. Here are the key functions:

1. Updated the `TokenType` enum to include new token types: `COMMA`, `DOT`, `MINUS`, `PLUS`, `SEMICOLON`, and `STAR`.
2. Modified the `scan_token` method in the `Scanner` class to recognize these new characters and create the appropriate tokens.

The scanner can handle the following single-character tokens:
- Comma: ','
- Dot: '.'
- Minus: '-'
- Plus: '+'
- Semicolon: ';'
- Star: '*'

These are in addition to the previously supported parentheses and braces.

### Token Output

The output format remains the same, with the new tokens following the established pattern

<token_type> <lexeme> <literal>


For example:
COMMA , null
DOT . null
PLUS + null


This significantly expands the range of Lox syntax our scanner can recognize, bringing us closer to a complete lexical analysis of the language.


### Lexical Error Handling

Handle and report lexical errors. Here are the key functions:

1. The `Scanner` class keeps track of the current line number.
2. Added an `error` method to the `Scanner` class that reports errors to stderr with the required `[line N]` prefix.
3. The `scan_token` method now reports unexpected characters as errors.
4. Added a `had_error` flag to the `Scanner` class to track if any errors occurred during scanning.
5. The `main` function sets the exit code to 65 if any lexical errors were encountered.

These changes allow the scanner to continue processing the input even after encountering an error, reporting all lexical errors it finds. Valid tokens are still output to stdout, while error messages are sent to stderr.

### Error Output

Lexical errors are reported in the following format:
[line N] Error: Unexpected character: X


Where `N` is the line number and `X` is the unexpected character.

This improves the scanner's robustness and error reporting capabilities, bringing it closer to a production-ready lexical analyzer.


### Assignment and Equality Operators

Extended the scanner to recognize assignment (=) and equality (==) operators, as well as the bang (!) and bang-equal (!=) operators. Here are the key functions:

1. Added new token types to the `TokenType` enum: `EQUAL`, `EQUAL_EQUAL`, `BANG`, and `BANG_EQUAL`.
2. Updated the `scan_token` method to handle these new operators:
   - For '=', it checks if the next character is also '=' to distinguish between assignment (=) and equality (==).
   - For '!', it checks if the next character is '=' to distinguish between bang (!) and not-equal (!=).
3. Implemented a new `match` method in the `Scanner` class to look ahead one character without consuming it, used for two-character operators.

These changes allow our scanner to correctly tokenize expressions containing assignment and equality operators, such as:
x = 5
if (x == 10) { ... }
if (x != 20) { ... }


The scanner can now distinguish between single-character (= and !) and two-character (== and !=) operators, improving its ability to handle more complex Lox syntax.


### Relational Operators

Extended the scanner to recognize relational operators (<, >, <=, >=). Here are the key functions:

1. Added new token types to the `TokenType` enum: `LESS`, `LESS_EQUAL`, `GREATER`, and `GREATER_EQUAL`.
2. Updated the `scan_token` method to handle these new operators:
   - For '<', it checks if the next character is '=' to distinguish between less-than (<) and less-than-or-equal (<=).
   - For '>', it checks if the next character is '=' to distinguish between greater-than (>) and greater-than-or-equal (>=).

These changes allow our scanner to correctly tokenize expressions containing relational operators, such as:
if (x < 10) { ... }
if (y >= 20) { ... }


The scanner can now distinguish between single-character (< and >) and two-character (<= and >=) relational operators, further improving its ability to handle complex Lox syntax.

This completes the set of basic comparison operators in our scanner, allowing it to recognize all standard relational and equality operators used in most programming languages.


### Division Operator and Comments

Extended the scanner to recognize the division operator (/) and handle comments (//). Here are the key functions:

1. Added a new token type to the `TokenType` enum: `SLASH`.
2. Updated the `scan_token` method to handle the slash character:
   - If a single slash is encountered, it's treated as the division operator.
   - If two slashes are encountered, it's treated as the start of a comment.
3. Implemented comment handling:
   - When a comment is detected, the scanner consumes all characters until the end of the line or the end of the file.
   - Comments are completely ignored and do not produce any tokens.
4. Added a new `peek` method to look at the current character without consuming it, used for handling comments.

These allow scanner to correctly tokenize expressions containing the division operator and to ignore comments, such as:
x = 10 / 2;  // This is a comment


The scanner will now:
- Recognize '/' as a SLASH token when used as a division operator.
- Ignore everything after '//' until the end of the line, treating it as a comment.

This improves scanner's ability to handle more complex Lox syntax and adds support for code comments, which are crucial for code readability and documentation.It also allows the scanner to handle the division operator and comments as specified. 


### String Literals

Extended the scanner to recognize and handle string literals. Here are the key functions:

1. Added a new token type to the `TokenType` enum: `STRING`.
2. Implemented a new `string` method in the `Scanner` class to handle string literals:
   - It consumes characters until it finds a closing double quote or reaches the end of the file.
   - It supports multi-line strings by incrementing the line counter when encountering newlines.
   - If it reaches the end of the file without finding a closing quote, it reports an "Unterminated string" error.
3. Updated the `scan_token` method to call the `string` method when it encounters a double quote.
4. Modified the `add_token` method to accept an optional `literal` parameter, used for storing the string value.

These changes allow scanner to correctly tokenize string literals and handle unterminated strings, such as:
"This is a valid string"
"This is an unterminated string


The scanner will now:
- Recognize string literals enclosed in double quotes and create STRING tokens for them.
- Store the string value (without the surrounding quotes) as the token's literal value.
- Report an error for unterminated strings, including the line number where the string started.

This significantly improves our scanner's capabilities, allowing it to handle an important data type in the Lox language. It also demonstrates how the scanner can handle multi-line tokens and report more complex lexical errors and allows the scanner to handle string literals as specified, including error reporting for unterminated strings, while still recognizing and outputting all previously supported tokens.



### Number Literals

Extended the scanner to recognize and handle number literals. Here are the key functions:

1. Added a new token type to the `TokenType` enum: `NUMBER`.
2. Implemented a new `number` method in the `Scanner` class to handle number literals:
   - It consumes digits for the integer part of the number.
   - It looks for a decimal point followed by digits for the fractional part.
   - It converts the entire lexeme to a float value.
3. Updated the `scan_token` method to call the `number` method when it encounters a digit.
4. Added a new `peek_next` method to look two characters ahead, used for detecting decimal points in numbers.

These changes allow our scanner to correctly tokenize number literals, including both integers and floating-point numbers. For example:

123
3.14159


The scanner will now:
- Recognize integer and floating-point number literals.
- Create NUMBER tokens for these literals.
- Store the numeric value as a float in the token's literal value.

This further expands the scanner's capabilities, allowing it to handle another important data type in the Lox language. It can recognize and tokenize all basic literal types (strings and numbers) as well as all operators and punctuation used in Lox.

### Identifiers

Extended scanner to recognize and handle identifiers. Here are the key functions:

1. Added a new token type to the `TokenType` enum: `IDENTIFIER`.
2. Implemented a new `identifier` method in the `Scanner` class to handle identifiers:
   - It consumes characters that are alphanumeric or underscores.
3. Added two new helper methods:
   - `is_alpha`: checks if a character is alphabetic or an underscore.
   - `is_alphanumeric`: checks if a character is alphanumeric or an underscore.
4. Updated the `scan_token` method to call the `identifier` method when it encounters an alphabetic character or underscore.

These changes allow our scanner to correctly tokenize identifiers. For example:
foo bar _hello


The scanner will now:
- Recognize identifiers that start with a letter or underscore and can contain letters, digits, or underscores.
- Create IDENTIFIER tokens for these lexemes.
- Correctly handle identifiers in the context of other tokens.

This completes the basic lexical analysis capabilities of the scanner. It can now recognize and tokenize all fundamental elements of the Lox language, including:
- Literals (strings and numbers)
- Operators and punctuation
- Identifiers

The scanner is now capable of breaking down Lox source code into a sequence of tokens that can be used by subsequent stages of the interpreter, such as parsing.

### Reserved Words

Extended the scanner to recognize and handle reserved words in the Lox language. Here are the key functions:

1. Added new token types to the `TokenType` enum for each reserved word: `AND`, `CLASS`, `ELSE`, `FALSE`, `FOR`, `FUN`, `IF`, `NIL`, `OR`, `PRINT`, `RETURN`, `SUPER`, `THIS`, `TRUE`, `VAR`, and `WHILE`.
2. Created a `keywords` dictionary in the `Scanner` class that maps reserved word strings to their corresponding `TokenType`.
3. Updated the `identifier` method to check if the scanned identifier is a reserved word:
   - If the identifier matches a reserved word, it creates a token of the corresponding reserved word type.
   - If not, it creates an `IDENTIFIER` token as before.

These changes allow our scanner to correctly tokenize reserved words. For example:
if (true) {
print "Hello, World!";
}


The scanner will:
- Recognize reserved words and create the appropriate token types for them (e.g., `IF`, `TRUE`, `PRINT`).
- Still correctly handle identifiers that are not reserved words.
- Distinguish between reserved words and identifiers in the context of other tokens.


The scanner is now fully capable of breaking down Lox source code into a complete and accurate sequence of tokens that can be used by subsequent stages of the interpreter, such as parsing.
