from antlr4 import CommonTokenStream, InputStream
from antlr4.Recognizer import ConsoleErrorListener

from small.cst.small.SmallGrammarLexer import SmallGrammarLexer
from small.cst.small.SmallGrammarParser import SmallGrammarParser


def parse(stream: InputStream):
    lexer = SmallGrammarLexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = SmallGrammarParser(tokens)

    parser.removeErrorListeners()
    errors: list[str] = []

    class ErrorListener(ConsoleErrorListener):
        def syntaxError(
            self,
            recognizer,
            offendingSymbol,  # noqa: N803
            line,
            column,
            msg,
            e,  # noqa: N803
        ):
            errors.append(f"line {line}:{column} {msg}")

    parser.addErrorListener(ErrorListener())

    cst = parser.program()

    if errors:
        raise ValueError("\n".join(errors))

    return cst
