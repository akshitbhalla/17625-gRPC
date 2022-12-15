from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

ADVENTURE: Genre
AVAILABLE: InventoryStatus
DESCRIPTOR: _descriptor.FileDescriptor
FANTASY: Genre
MYSTERY: Genre
ROMANCE: Genre
TAKEN: InventoryStatus
THRILLER: Genre

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
    __slots__ = ["book", "number", "status"]
    BOOK_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    book: Book
    number: int
    status: InventoryStatus
    def __init__(self, number: _Optional[int] = ..., book: _Optional[_Union[Book, _Mapping]] = ..., status: _Optional[_Union[InventoryStatus, str]] = ...) -> None: ...

class Status(_message.Message):
    __slots__ = ["code", "details", "message"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: int
    details: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    message: str
    def __init__(self, code: _Optional[int] = ..., message: _Optional[str] = ..., details: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...) -> None: ...

class Genre(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class InventoryStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
