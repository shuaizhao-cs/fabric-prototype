# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: peer/lifecycle/db.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='peer/lifecycle/db.proto',
  package='lifecycle',
  syntax='proto3',
  serialized_pb=_b('\n\x17peer/lifecycle/db.proto\x12\tlifecycle\"1\n\rStateMetadata\x12\x10\n\x08\x64\x61tatype\x18\x01 \x01(\t\x12\x0e\n\x06\x66ields\x18\x02 \x03(\t\"G\n\tStateData\x12\x0f\n\x05Int64\x18\x01 \x01(\x03H\x00\x12\x0f\n\x05\x42ytes\x18\x02 \x01(\x0cH\x00\x12\x10\n\x06String\x18\x03 \x01(\tH\x00\x42\x06\n\x04TypeBf\n,org.hyperledger.fabric.protos.peer.lifecycleZ6github.com/hyperledger/fabric-protos-go/peer/lifecycleb\x06proto3')
)




_STATEMETADATA = _descriptor.Descriptor(
  name='StateMetadata',
  full_name='lifecycle.StateMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='datatype', full_name='lifecycle.StateMetadata.datatype', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fields', full_name='lifecycle.StateMetadata.fields', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=87,
)


_STATEDATA = _descriptor.Descriptor(
  name='StateData',
  full_name='lifecycle.StateData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Int64', full_name='lifecycle.StateData.Int64', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Bytes', full_name='lifecycle.StateData.Bytes', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='String', full_name='lifecycle.StateData.String', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='Type', full_name='lifecycle.StateData.Type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=89,
  serialized_end=160,
)

_STATEDATA.oneofs_by_name['Type'].fields.append(
  _STATEDATA.fields_by_name['Int64'])
_STATEDATA.fields_by_name['Int64'].containing_oneof = _STATEDATA.oneofs_by_name['Type']
_STATEDATA.oneofs_by_name['Type'].fields.append(
  _STATEDATA.fields_by_name['Bytes'])
_STATEDATA.fields_by_name['Bytes'].containing_oneof = _STATEDATA.oneofs_by_name['Type']
_STATEDATA.oneofs_by_name['Type'].fields.append(
  _STATEDATA.fields_by_name['String'])
_STATEDATA.fields_by_name['String'].containing_oneof = _STATEDATA.oneofs_by_name['Type']
DESCRIPTOR.message_types_by_name['StateMetadata'] = _STATEMETADATA
DESCRIPTOR.message_types_by_name['StateData'] = _STATEDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StateMetadata = _reflection.GeneratedProtocolMessageType('StateMetadata', (_message.Message,), dict(
  DESCRIPTOR = _STATEMETADATA,
  __module__ = 'peer.lifecycle.db_pb2'
  # @@protoc_insertion_point(class_scope:lifecycle.StateMetadata)
  ))
_sym_db.RegisterMessage(StateMetadata)

StateData = _reflection.GeneratedProtocolMessageType('StateData', (_message.Message,), dict(
  DESCRIPTOR = _STATEDATA,
  __module__ = 'peer.lifecycle.db_pb2'
  # @@protoc_insertion_point(class_scope:lifecycle.StateData)
  ))
_sym_db.RegisterMessage(StateData)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n,org.hyperledger.fabric.protos.peer.lifecycleZ6github.com/hyperledger/fabric-protos-go/peer/lifecycle'))
# @@protoc_insertion_point(module_scope)
