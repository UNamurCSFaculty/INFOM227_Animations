grammar SmallGrammar;

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

// Programs

program: function*;

function: FUNCTION IDENTIFIER LPAR paramList? RPAR stmtList;

paramList: param (COMMA param)*;

param: IDENTIFIER;

// Statements

stmt: assignStmt | ifStmt | whileStmt | returnStmt;

assignStmt: IDENTIFIER EQUAL (expr | funcCall) SEMICOLON;

ifStmt:
	IF LPAR boolExpr RPAR ifBody = sequence ELSE elseBody = sequence;

whileStmt: WHILE LPAR boolExpr RPAR sequence;

returnStmt: RETURN expr SEMICOLON;

stmtList: stmt*;

sequence: stmt | LBRACE stmtList RBRACE;

// Expressions

exprList: expr (COMMA expr)*;

funcCall: IDENTIFIER LPAR exprList? RPAR;

expr: arithExpr | boolExpr;

arithExpr: noprnd | binMathOp;

boolExpr: boprnd | relOp | binLogicOp;

binMathOp: left = noprnd mathOp right = noprnd;

binLogicOp: left = noprnd logicOp right = noprnd;

relOp: left = boprnd nop right = boprnd;

noprnd: IDENTIFIER | NUM;

boprnd: IDENTIFIER | TRUE | FALSE;

// Operators

mathOp: ADD | SUBSTRACT | MULTIPLY | DIVIDE;

logicOp:
	LESS
	| GREATER
	| EQUAL
	| DIFFERENT
	| GREATER_EQUAL
	| LESS_EQUAL;

nop: EQUAL | DIFFERENT | AND | OR;