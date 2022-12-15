import inventory_model_pb2 as _inventory_model_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateBookResponse(_message.Message):
    __slots__ = ["reponseMessage", "statusCode"]
    REPONSEMESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUSCODE_FIELD_NUMBER: _ClassVar[int]
    reponseMessage: str
    statusCode: int
    def __init__(self, statusCode: _Optional[int] = ..., reponseMessage: _Optional[str] = ...) -> None: ...

class GetBookRequest(_message.Message):
    __slots__ = ["isbn"]
    ISBN_FIELD_NUMBER: _ClassVar[int]
    isbn: str
    def __init__(self, isbn: _Optional[str] = ...) -> None: ...

class GetBookResponse(_message.Message):
    __slots__ = ["book", "reponseMessage", "statusCode"]
    BOOK_FIELD_NUMBER: _ClassVar[int]
    REPONSEMESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUSCODE_FIELD_NUMBER: _ClassVar[int]
    book: _inventory_model_pb2.Book
    reponseMessage: str
    statusCode: int
    def __init__(self, statusCode: _Optional[int] = ..., reponseMessage: _Optional[str] = ..., book: _Optional[_Union[_inventory_model_pb2.Book, _Mapping]] = ...) -> None: ...
