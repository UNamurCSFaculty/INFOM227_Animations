from small.cst import parse
from small.ast.builder import build
from antlr4 import InputStream, FileStream


def read_stream(stream: InputStream):
    return build(parse(stream), program=str(stream))


def read_string(string: str):
    return read_stream(InputStream(string))


def read_file(filepath: str):
    return read_stream(FileStream(filepath))
