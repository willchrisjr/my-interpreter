# My Interpreter

This project is an implementation of an interpreter for the Lox programming language, based on the book "Crafting Interpreters" by Robert Nystrom.

## Current Status

We have implemented a basic scanner (lexer) that can tokenize a subset of the Lox language. Currently, it supports:

- Parentheses
- Braces
- Basic error reporting for unexpected characters
- EOF (End of File) token

## Code Structure

The main components of our code are:

1. `TokenType` enum: Defines the types of tokens our scanner can recognize.
2. `Token` class: Represents individual tokens with type, lexeme, and literal value.
3. `Scanner` class: Handles the tokenization process.
4. `main` function: Orchestrates the program flow, reads input, and outputs results.

## Recent Changes

### Added Support for Braces

We've extended our scanner to recognize braces in addition to parentheses. Here's what we changed:

1. Updated the `TokenType` enum to include `LEFT_BRACE` and `RIGHT_BRACE`.
2. Modified the `scan_token` method in the `Scanner` class to recognize '{' and '}' characters and create the appropriate tokens.

The scanner now handles:
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

## Recent Changes

### Added Support for Additional Single-Character Tokens

We've extended our scanner to recognize several new single-character tokens. Here's what we changed:

1. Updated the `TokenType` enum to include new token types: `COMMA`, `DOT`, `MINUS`, `PLUS`, `SEMICOLON`, and `STAR`.
2. Modified the `scan_token` method in the `Scanner` class to recognize these new characters and create the appropriate tokens.

The scanner now handles the following single-character tokens:
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


This update significantly expands the range of Lox syntax our scanner can recognize, bringing us closer to a complete lexical analysis of the language.
This README entry focuses on the latest changes we've made, explaining the new single-character tokens we've added support for and how they fit into the existing scanner structure.

## Recent Changes

### Added Support for Lexical Error Handling

We've updated our scanner to handle and report lexical errors. Here are the key changes:

1. The `Scanner` class now keeps track of the current line number.
2. We've added an `error` method to the `Scanner` class that reports errors to stderr with the required `[line N]` prefix.
3. The `scan_token` method now reports unexpected characters as errors.
4. We've added a `had_error` flag to the `Scanner` class to track if any errors occurred during scanning.
5. The `main` function now sets the exit code to 65 if any lexical errors were encountered.

These changes allow our scanner to continue processing the input even after encountering an error, reporting all lexical errors it finds. Valid tokens are still output to stdout, while error messages are sent to stderr.

### Error Output

Lexical errors are now reported in the following format:
[line N] Error: Unexpected character: X


Where `N` is the line number and `X` is the unexpected character.

This update improves our scanner's robustness and error reporting capabilities, bringing it closer to a production-ready lexical analyzer.
This update allows the scanner to handle and report lexical errors as specified, while still recognizing and outputting valid tokens.

## Recent Changes

### Added Support for Assignment and Equality Operators

We've extended our scanner to recognize assignment (=) and equality (==) operators, as well as the bang (!) and bang-equal (!=) operators. Here are the key changes:

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
This update allows the scanner to handle assignment and equality operators as specified, while still recognizing and outputting all previously supported tokens.

## Recent Changes

### Added Support for Relational Operators

We've extended our scanner to recognize relational operators (<, >, <=, >=). Here are the key changes:

1. Added new token types to the `TokenType` enum: `LESS`, `LESS_EQUAL`, `GREATER`, and `GREATER_EQUAL`.
2. Updated the `scan_token` method to handle these new operators:
   - For '<', it checks if the next character is '=' to distinguish between less-than (<) and less-than-or-equal (<=).
   - For '>', it checks if the next character is '=' to distinguish between greater-than (>) and greater-than-or-equal (>=).

These changes allow our scanner to correctly tokenize expressions containing relational operators, such as:
if (x < 10) { ... }
if (y >= 20) { ... }


The scanner can now distinguish between single-character (< and >) and two-character (<= and >=) relational operators, further improving its ability to handle complex Lox syntax.

This update completes the set of basic comparison operators in our scanner, allowing it to recognize all standard relational and equality operators used in most programming languages.
This update allows the scanner to handle relational operators as specified, while still recognizing and outputting all previously supported tokens

## Recent Changes

### Added Support for Division Operator and Comments

We've extended our scanner to recognize the division operator (/) and handle comments (//). Here are the key changes:

1. Added a new token type to the `TokenType` enum: `SLASH`.
2. Updated the `scan_token` method to handle the slash character:
   - If a single slash is encountered, it's treated as the division operator.
   - If two slashes are encountered, it's treated as the start of a comment.
3. Implemented comment handling:
   - When a comment is detected, the scanner consumes all characters until the end of the line or the end of the file.
   - Comments are completely ignored and do not produce any tokens.
4. Added a new `peek` method to look at the current character without consuming it, used for handling comments.

These changes allow our scanner to correctly tokenize expressions containing the division operator and to ignore comments, such as:
x = 10 / 2;  // This is a comment


The scanner will now:
- Recognize '/' as a SLASH token when used as a division operator.
- Ignore everything after '//' until the end of the line, treating it as a comment.

This update improves our scanner's ability to handle more complex Lox syntax and adds support for code comments, which are crucial for code readability and documentation.
This update allows the scanner to handle the division operator and comments as specified, while still recognizing and outputting all previously supported tokens.

## Recent Changes

### Added Support for String Literals

We've extended our scanner to recognize and handle string literals. Here are the key changes:

1. Added a new token type to the `TokenType` enum: `STRING`.
2. Implemented a new `string` method in the `Scanner` class to handle string literals:
   - It consumes characters until it finds a closing double quote or reaches the end of the file.
   - It supports multi-line strings by incrementing the line counter when encountering newlines.
   - If it reaches the end of the file without finding a closing quote, it reports an "Unterminated string" error.
3. Updated the `scan_token` method to call the `string` method when it encounters a double quote.
4. Modified the `add_token` method to accept an optional `literal` parameter, used for storing the string value.

These changes allow our scanner to correctly tokenize string literals and handle unterminated strings, such as:
"This is a valid string"
"This is an unterminated string


The scanner will now:
- Recognize string literals enclosed in double quotes and create STRING tokens for them.
- Store the string value (without the surrounding quotes) as the token's literal value.
- Report an error for unterminated strings, including the line number where the string started.

This update significantly improves our scanner's capabilities, allowing it to handle an important data type in the Lox language. It also demonstrates how the scanner can handle multi-line tokens and report more complex lexical errors.
This update allows the scanner to handle string literals as specified, including error reporting for unterminated strings, while still recognizing and outputting all previously supported tokens.

## Recent Changes

### Added Support for Number Literals

We've extended our scanner to recognize and handle number literals. Here are the key changes:

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

This update further expands our scanner's capabilities, allowing it to handle another important data type in the Lox language. The scanner can now recognize and tokenize all basic literal types (strings and numbers) as well as all operators and punctuation used in Lox.
This update allows the scanner to handle number literals as specified, while still recognizing and outputting all previously supported tokens. The scanner now supports a wide range of Lox syntax elements, including literals, operators, and punctuation.

### Added Support for Identifiers

We've extended our scanner to recognize and handle identifiers. Here are the key changes:

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

This update completes the basic lexical analysis capabilities of our scanner. It can now recognize and tokenize all fundamental elements of the Lox language, including:
- Literals (strings and numbers)
- Operators and punctuation
- Identifiers

The scanner is now capable of breaking down Lox source code into a sequence of tokens that can be used by subsequent stages of the interpreter, such as parsing.
This update allows the scanner to handle identifiers as specified, while still recognizing and outputting all previously supported tokens. The scanner now supports all basic lexical elements of the Lox language.

### Added Support for Reserved Words

We've extended our scanner to recognize and handle reserved words in the Lox language. Here are the key changes:

1. Added new token types to the `TokenType` enum for each reserved word: `AND`, `CLASS`, `ELSE`, `FALSE`, `FOR`, `FUN`, `IF`, `NIL`, `OR`, `PRINT`, `RETURN`, `SUPER`, `THIS`, `TRUE`, `VAR`, and `WHILE`.
2. Created a `keywords` dictionary in the `Scanner` class that maps reserved word strings to their corresponding `TokenType`.
3. Updated the `identifier` method to check if the scanned identifier is a reserved word:
   - If the identifier matches a reserved word, it creates a token of the corresponding reserved word type.
   - If not, it creates an `IDENTIFIER` token as before.

These changes allow our scanner to correctly tokenize reserved words. For example:
if (true) {
print "Hello, World!";
}


The scanner will now:
- Recognize reserved words and create the appropriate token types for them (e.g., `IF`, `TRUE`, `PRINT`).
- Still correctly handle identifiers that are not reserved words.
- Distinguish between reserved words and identifiers in the context of other tokens.

This update completes the lexical analysis capabilities of our scanner for the Lox language. It can now recognize and tokenize all elements of Lox, including:
- Literals (strings and numbers)
- Operators and punctuation
- Identifiers
- Reserved words

The scanner is now fully capable of breaking down Lox source code into a complete and accurate sequence of tokens that can be used by subsequent stages of the interpreter, such as parsing.
This update allows the scanner to handle reserved words as specified, while still recognizing and outputting all previously supported tokens. The scanner now supports all lexical elements of the Lox language, including reserved words.