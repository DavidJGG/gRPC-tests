# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rexample.proto\"0\n\x12multiplicarRequest\x12\x0c\n\x04num1\x18\x01 \x01(\x03\x12\x0c\n\x04num2\x18\x02 \x01(\x03\"%\n\x10multiplicarReply\x12\x11\n\tresultado\x18\x01 \x01(\x03\"\x1b\n\x0bmegaRequest\x12\x0c\n\x04size\x18\x01 \x01(\x05\"\x1e\n\tmegaReply\x12\x11\n\tsecuencia\x18\x01 \x01(\t2\x99\x01\n\x0bmultiplicar\x12\x35\n\x0bmultiplicar\x12\x13.multiplicarRequest\x1a\x11.multiplicarReply\x12\x31\n\x07\x64ividir\x12\x13.multiplicarRequest\x1a\x11.multiplicarReply\x12 \n\x04mega\x12\x0c.megaRequest\x1a\n.megaReplyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'example_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_MULTIPLICARREQUEST']._serialized_start=17
  _globals['_MULTIPLICARREQUEST']._serialized_end=65
  _globals['_MULTIPLICARREPLY']._serialized_start=67
  _globals['_MULTIPLICARREPLY']._serialized_end=104
  _globals['_MEGAREQUEST']._serialized_start=106
  _globals['_MEGAREQUEST']._serialized_end=133
  _globals['_MEGAREPLY']._serialized_start=135
  _globals['_MEGAREPLY']._serialized_end=165
  _globals['_MULTIPLICAR']._serialized_start=168
  _globals['_MULTIPLICAR']._serialized_end=321
# @@protoc_insertion_point(module_scope)