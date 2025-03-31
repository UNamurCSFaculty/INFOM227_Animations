from antlr4 import FileStream, InputStream

from small.ast.builder import build
from small.cst import parse


def read_stream(stream: InputStream):
    return build(parse(stream), program=str(stream))


def read_string(string: str):
    return read_stream(InputStream(string))


def read_file(filepath: str):
    return read_stream(FileStream(filepath))
