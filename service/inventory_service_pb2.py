# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inventory_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import inventory_model_pb2 as inventory__model__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17inventory_service.proto\x12\x0finventorySystem\x1a\x15inventory_model.proto\"@\n\x12\x43reateBookResponse\x12\x12\n\nstatusCode\x18\x01 \x01(\x05\x12\x16\n\x0ereponseMessage\x18\x02 \x01(\t\"\x1e\n\x0eGetBookRequest\x12\x0c\n\x04isbn\x18\x01 \x01(\t\"b\n\x0fGetBookResponse\x12\x12\n\nstatusCode\x18\x01 \x01(\x05\x12\x16\n\x0ereponseMessage\x18\x02 \x01(\t\x12#\n\x04\x62ook\x18\x03 \x01(\x0b\x32\x15.inventorySystem.Book2\xaa\x01\n\x10InventoryService\x12H\n\nCreateBook\x12\x15.inventorySystem.Book\x1a#.inventorySystem.CreateBookResponse\x12L\n\x07GetBook\x12\x1f.inventorySystem.GetBookRequest\x1a .inventorySystem.GetBookResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'inventory_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CREATEBOOKRESPONSE._serialized_start=67
  _CREATEBOOKRESPONSE._serialized_end=131
  _GETBOOKREQUEST._serialized_start=133
  _GETBOOKREQUEST._serialized_end=163
  _GETBOOKRESPONSE._serialized_start=165
  _GETBOOKRESPONSE._serialized_end=263
  _INVENTORYSERVICE._serialized_start=266
  _INVENTORYSERVICE._serialized_end=436
# @@protoc_insertion_point(module_scope)