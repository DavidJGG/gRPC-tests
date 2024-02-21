from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class multiplicarRequest(_message.Message):
    __slots__ = ("num1", "num2")
    NUM1_FIELD_NUMBER: _ClassVar[int]
    NUM2_FIELD_NUMBER: _ClassVar[int]
    num1: int
    num2: int
    def __init__(self, num1: _Optional[int] = ..., num2: _Optional[int] = ...) -> None: ...

class multiplicarReply(_message.Message):
    __slots__ = ("resultado",)
    RESULTADO_FIELD_NUMBER: _ClassVar[int]
    resultado: int
    def __init__(self, resultado: _Optional[int] = ...) -> None: ...

class megaRequest(_message.Message):
    __slots__ = ("size",)
    SIZE_FIELD_NUMBER: _ClassVar[int]
    size: int
    def __init__(self, size: _Optional[int] = ...) -> None: ...

class megaReply(_message.Message):
    __slots__ = ("secuencia",)
    SECUENCIA_FIELD_NUMBER: _ClassVar[int]
    secuencia: str
    def __init__(self, secuencia: _Optional[str] = ...) -> None: ...
