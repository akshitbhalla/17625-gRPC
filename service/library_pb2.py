# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: library.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rlibrary.proto\x12\tinventory\x1a\x19google/protobuf/any.proto\"m\n\x06Status\x12\x11\n\x04\x63ode\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x14\n\x07message\x18\x02 \x01(\tH\x01\x88\x01\x01\x12%\n\x07\x64\x65tails\x18\x03 \x03(\x0b\x32\x14.google.protobuf.AnyB\x07\n\x05_codeB\n\n\x08_message\"\xac\x01\n\x04\x42ook\x12\x11\n\x04isbn\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05title\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x13\n\x06\x61uthor\x18\x03 \x01(\tH\x02\x88\x01\x01\x12$\n\x05genre\x18\x04 \x01(\x0e\x32\x10.inventory.GenreH\x03\x88\x01\x01\x12\x11\n\x04year\x18\x05 \x01(\x05H\x04\x88\x01\x01\x42\x07\n\x05_isbnB\x08\n\x06_titleB\t\n\x07_authorB\x08\n\x06_genreB\x07\n\x05_year\"\x94\x01\n\rInventoryItem\x12\x13\n\x06number\x18\x01 \x01(\x05H\x01\x88\x01\x01\x12\x1f\n\x04\x62ook\x18\x02 \x01(\x0b\x32\x0f.inventory.BookH\x00\x12/\n\x06status\x18\x03 \x01(\x0e\x32\x1a.inventory.InventoryStatusH\x02\x88\x01\x01\x42\x06\n\x04typeB\t\n\x07_numberB\t\n\x07_status*K\n\x05Genre\x12\x0b\n\x07\x46\x41NTASY\x10\x00\x12\x0b\n\x07MYSTERY\x10\x01\x12\r\n\tADVENTURE\x10\x02\x12\x0b\n\x07ROMANCE\x10\x03\x12\x0c\n\x08THRILLER\x10\x04*+\n\x0fInventoryStatus\x12\r\n\tAVAILABLE\x10\x00\x12\t\n\x05TAKEN\x10\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'library_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GENRE._serialized_start=492
  _GENRE._serialized_end=567
  _INVENTORYSTATUS._serialized_start=569
  _INVENTORYSTATUS._serialized_end=612
  _STATUS._serialized_start=55
  _STATUS._serialized_end=164
  _BOOK._serialized_start=167
  _BOOK._serialized_end=339
  _INVENTORYITEM._serialized_start=342
  _INVENTORYITEM._serialized_end=490
# @@protoc_insertion_point(module_scope)
