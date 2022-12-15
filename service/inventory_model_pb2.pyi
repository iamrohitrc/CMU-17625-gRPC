from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

ADVENTURE: Genre
AVAILABLE: Status
BIOGRAPHY: Genre
DESCRIPTOR: _descriptor.FileDescriptor
MYSTERY: Genre
SPORTS: Genre
TECHNOLOGY: Genre
TOKEN: Status

class Book(_message.Message):
    __slots__ = ["author", "genre", "isbn", "title", "year"]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    GENRE_FIELD_NUMBER: _ClassVar[int]
    ISBN_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    author: str
    genre: Genre
    isbn: str
    title: str
    year: int
    def __init__(self, isbn: _Optional[str] = ..., title: _Optional[str] = ..., author: _Optional[str] = ..., genre: _Optional[_Union[Genre, str]] = ..., year: _Optional[int] = ...) -> None: ...

class InventoryItem(_message.Message):
    __slots__ = ["Status", "book", "number"]
    BOOK_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    Status: Status
    book: Book
    number: int
    def __init__(self, number: _Optional[int] = ..., book: _Optional[_Union[Book, _Mapping]] = ..., Status: _Optional[_Union[Status, str]] = ...) -> None: ...

class Genre(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
