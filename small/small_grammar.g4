grammar small_grammar;

/*
 * Lexer Rules
 */

// Keywords

IF: 'if';

ELSE: 'else';

WHILE: 'while';

FUNCTION: 'function';

RETURN: 'return';

// Separators / Punctuators

LBRACE: '{';

RBRACE: '}';

LPAR: '(';

RPAR: ')';

COMMA: ',';

SEMICOLON: ';';

// Operators

ASSIGN: '=';

AND: 'and';

OR: 'or';

ADD: '+';

SUBSTRACT: '-';

MULTIPLY: '*';

DIVIDE: '/';

GREATER: '>';

GREATER_EQUAL: '>=';

LESS: '<';

LESS_EQUAL: '<=';

EQUAL: '==';

DIFFERENT: '!=';

// Literals

TRUE: 'True';

FALSE: 'False';

fragment DIGIT: [0-9];

NUM: DIGIT+;

// Identifiers

fragment LETTER: [a-zA-Z];

IDENTIFIER: LETTER (LETTER | DIGIT)*;

// Comments -> ignored

COMMENT: ('/*' (.*?) '*/' | '//' .*? '\r'? ('\n' | EOF)) -> skip;

// Whitespaces -> ignored

NEWLINE: '\r'? '\n' -> skip;

WS: [ \t]+ -> skip;

/*
 * Parser Rules
 */

// Operators

math_op: ADD | SUBSTRACT | MULTIPLY | DIVIDE;

logic_op:
	LESS
	| GREATER
	| EQUAL
	| DIFFERENT
	| GREATER_EQUAL
	| LESS_EQUAL;

nop: EQUAL | DIFFERENT | AND | OR;

// Expressions

expr: arith_expr | bool_expr;

arith_expr: noprnd | bin_math_op;

bool_expr: boprnd | rel_op | bin_logic_op;

bin_math_op: left = noprnd math_op right = noprnd;

bin_logic_op: left = noprnd logic_op right = noprnd;

rel_op: left = boprnd nop right = boprnd;

noprnd: IDENTIFIER | NUM;

boprnd: IDENTIFIER | TRUE | FALSE;

expr_list: expr (COMMA expr)*;

func_call: IDENTIFIER LPAR expr_list? RPAR;

// Statements

stmt: assign_stmt | if_stmt | while_stmt | return_stmt;

assign_stmt: IDENTIFIER EQUAL (expr | func_call) SEMICOLON;

if_stmt:
	IF LPAR bool_expr RPAR if_body = sequence ELSE else_body = sequence;

while_stmt: WHILE LPAR bool_expr RPAR while_body = sequence;

return_stmt: RETURN expr SEMICOLON;

stmt_list: stmt*;

sequence: stmt | LBRACE stmt_list RBRACE;

// Programs

program: function*;

function: FUNCTION IDENTIFIER LPAR param_list? RPAR stmt_list;

param_list: param (COMMA param)*;

param: IDENTIFIER;