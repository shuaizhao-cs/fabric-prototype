# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/configuration.proto

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
  name='common/configuration.proto',
  package='common',
  syntax='proto3',
  serialized_pb=_b('\n\x1a\x63ommon/configuration.proto\x12\x06\x63ommon\" \n\x10HashingAlgorithm\x12\x0c\n\x04name\x18\x01 \x01(\t\"*\n\x19\x42lockDataHashingStructure\x12\r\n\x05width\x18\x01 \x01(\r\"%\n\x10OrdererAddresses\x12\x11\n\taddresses\x18\x01 \x03(\t\"\x1a\n\nConsortium\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x95\x01\n\x0c\x43\x61pabilities\x12<\n\x0c\x63\x61pabilities\x18\x01 \x03(\x0b\x32&.common.Capabilities.CapabilitiesEntry\x1aG\n\x11\x43\x61pabilitiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.common.Capability:\x02\x38\x01\"\x0c\n\nCapabilityBV\n$org.hyperledger.fabric.protos.commonZ.github.com/hyperledger/fabric-protos-go/commonb\x06proto3')
)




_HASHINGALGORITHM = _descriptor.Descriptor(
  name='HashingAlgorithm',
  full_name='common.HashingAlgorithm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='common.HashingAlgorithm.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  ],
  serialized_start=38,
  serialized_end=70,
)


_BLOCKDATAHASHINGSTRUCTURE = _descriptor.Descriptor(
  name='BlockDataHashingStructure',
  full_name='common.BlockDataHashingStructure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='common.BlockDataHashingStructure.width', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=72,
  serialized_end=114,
)


_ORDERERADDRESSES = _descriptor.Descriptor(
  name='OrdererAddresses',
  full_name='common.OrdererAddresses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='addresses', full_name='common.OrdererAddresses.addresses', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=116,
  serialized_end=153,
)


_CONSORTIUM = _descriptor.Descriptor(
  name='Consortium',
  full_name='common.Consortium',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='common.Consortium.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  ],
  serialized_start=155,
  serialized_end=181,
)


_CAPABILITIES_CAPABILITIESENTRY = _descriptor.Descriptor(
  name='CapabilitiesEntry',
  full_name='common.Capabilities.CapabilitiesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='common.Capabilities.CapabilitiesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='common.Capabilities.CapabilitiesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=262,
  serialized_end=333,
)

_CAPABILITIES = _descriptor.Descriptor(
  name='Capabilities',
  full_name='common.Capabilities',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='capabilities', full_name='common.Capabilities.capabilities', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CAPABILITIES_CAPABILITIESENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=184,
  serialized_end=333,
)


_CAPABILITY = _descriptor.Descriptor(
  name='Capability',
  full_name='common.Capability',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=335,
  serialized_end=347,
)

_CAPABILITIES_CAPABILITIESENTRY.fields_by_name['value'].message_type = _CAPABILITY
_CAPABILITIES_CAPABILITIESENTRY.containing_type = _CAPABILITIES
_CAPABILITIES.fields_by_name['capabilities'].message_type = _CAPABILITIES_CAPABILITIESENTRY
DESCRIPTOR.message_types_by_name['HashingAlgorithm'] = _HASHINGALGORITHM
DESCRIPTOR.message_types_by_name['BlockDataHashingStructure'] = _BLOCKDATAHASHINGSTRUCTURE
DESCRIPTOR.message_types_by_name['OrdererAddresses'] = _ORDERERADDRESSES
DESCRIPTOR.message_types_by_name['Consortium'] = _CONSORTIUM
DESCRIPTOR.message_types_by_name['Capabilities'] = _CAPABILITIES
DESCRIPTOR.message_types_by_name['Capability'] = _CAPABILITY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HashingAlgorithm = _reflection.GeneratedProtocolMessageType('HashingAlgorithm', (_message.Message,), dict(
  DESCRIPTOR = _HASHINGALGORITHM,
  __module__ = 'common.configuration_pb2'
  # @@protoc_insertion_point(class_scope:common.HashingAlgorithm)
  ))
_sym_db.RegisterMessage(HashingAlgorithm)

BlockDataHashingStructure = _reflection.GeneratedProtocolMessageType('BlockDataHashingStructure', (_message.Message,), dict(
  DESCRIPTOR = _BLOCKDATAHASHINGSTRUCTURE,
  __module__ = 'common.configuration_pb2'
  # @@protoc_insertion_point(class_scope:common.BlockDataHashingStructure)
  ))
_sym_db.RegisterMessage(BlockDataHashingStructure)

OrdererAddresses = _reflection.GeneratedProtocolMessageType('OrdererAddresses', (_message.Message,), dict(
  DESCRIPTOR = _ORDERERADDRESSES,
  __module__ = 'common.configuration_pb2'
  # @@protoc_insertion_point(class_scope:common.OrdererAddresses)
  ))
_sym_db.RegisterMessage(OrdererAddresses)

Consortium = _reflection.GeneratedProtocolMessageType('Consortium', (_message.Message,), dict(
  DESCRIPTOR = _CONSORTIUM,
  __module__ = 'common.configuration_pb2'
  # @@protoc_insertion_point(class_scope:common.Consortium)
  ))
_sym_db.RegisterMessage(Consortium)

Capabilities = _reflection.GeneratedProtocolMessageType('Capabilities', (_message.Message,), dict(

  CapabilitiesEntry = _reflection.GeneratedProtocolMessageType('CapabilitiesEntry', (_message.Message,), dict(
    DESCRIPTOR = _CAPABILITIES_CAPABILITIESENTRY,
    __module__ = 'common.configuration_pb2'
    # @@protoc_insertion_point(class_scope:common.Capabilities.CapabilitiesEntry)
    ))
  ,
  DESCRIPTOR = _CAPABILITIES,
  __module__ = 'common.configuration_pb2'
  # @@protoc_insertion_point(class_scope:common.Capabilities)
  ))
_sym_db.RegisterMessage(Capabilities)
_sym_db.RegisterMessage(Capabilities.CapabilitiesEntry)

Capability = _reflection.GeneratedProtocolMessageType('Capability', (_message.Message,), dict(
  DESCRIPTOR = _CAPABILITY,
  __module__ = 'common.configuration_pb2'
  # @@protoc_insertion_point(class_scope:common.Capability)
  ))
_sym_db.RegisterMessage(Capability)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n$org.hyperledger.fabric.protos.commonZ.github.com/hyperledger/fabric-protos-go/common'))
_CAPABILITIES_CAPABILITIESENTRY.has_options = True
_CAPABILITIES_CAPABILITIESENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
