# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: peer/chaincode.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common import policies_pb2 as common_dot_policies__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='peer/chaincode.proto',
  package='protos',
  syntax='proto3',
  serialized_pb=_b('\n\x14peer/chaincode.proto\x12\x06protos\x1a\x15\x63ommon/policies.proto\":\n\x0b\x43haincodeID\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\"\xa1\x01\n\x0e\x43haincodeInput\x12\x0c\n\x04\x61rgs\x18\x01 \x03(\x0c\x12<\n\x0b\x64\x65\x63orations\x18\x02 \x03(\x0b\x32\'.protos.ChaincodeInput.DecorationsEntry\x12\x0f\n\x07is_init\x18\x03 \x01(\x08\x1a\x32\n\x10\x44\x65\x63orationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"\xdc\x01\n\rChaincodeSpec\x12(\n\x04type\x18\x01 \x01(\x0e\x32\x1a.protos.ChaincodeSpec.Type\x12)\n\x0c\x63haincode_id\x18\x02 \x01(\x0b\x32\x13.protos.ChaincodeID\x12%\n\x05input\x18\x03 \x01(\x0b\x32\x16.protos.ChaincodeInput\x12\x0f\n\x07timeout\x18\x04 \x01(\x05\">\n\x04Type\x12\r\n\tUNDEFINED\x10\x00\x12\n\n\x06GOLANG\x10\x01\x12\x08\n\x04NODE\x10\x02\x12\x07\n\x03\x43\x41R\x10\x03\x12\x08\n\x04JAVA\x10\x04\"\x84\x01\n\x17\x43haincodeDeploymentSpec\x12-\n\x0e\x63haincode_spec\x18\x01 \x01(\x0b\x32\x15.protos.ChaincodeSpec\x12\x14\n\x0c\x63ode_package\x18\x03 \x01(\x0cJ\x04\x08\x02\x10\x03J\x04\x08\x04\x10\x05R\x0e\x65\x66\x66\x65\x63tive_dateR\x08\x65xec_env\"a\n\x17\x43haincodeInvocationSpec\x12-\n\x0e\x63haincode_spec\x18\x01 \x01(\x0b\x32\x15.protos.ChaincodeSpecJ\x04\x08\x02\x10\x03R\x11id_generation_alg\"(\n\x0eLifecycleEvent\x12\x16\n\x0e\x63haincode_name\x18\x01 \x01(\t\"-\n\x07\x43\x44SData\x12\x0c\n\x04hash\x18\x01 \x01(\x0c\x12\x14\n\x0cmetadatahash\x18\x02 \x01(\x0c\"\xd4\x01\n\rChaincodeData\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x0c\n\x04\x65scc\x18\x03 \x01(\t\x12\x0c\n\x04vscc\x18\x04 \x01(\t\x12/\n\x06policy\x18\x05 \x01(\x0b\x32\x1f.common.SignaturePolicyEnvelope\x12\x0c\n\x04\x64\x61ta\x18\x06 \x01(\x0c\x12\n\n\x02id\x18\x07 \x01(\x0c\x12=\n\x14instantiation_policy\x18\x08 \x01(\x0b\x32\x1f.common.SignaturePolicyEnvelopeBR\n\"org.hyperledger.fabric.protos.peerZ,github.com/hyperledger/fabric-protos-go/peerb\x06proto3')
  ,
  dependencies=[common_dot_policies__pb2.DESCRIPTOR,])



_CHAINCODESPEC_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='protos.ChaincodeSpec.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GOLANG', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NODE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAR', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JAVA', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=438,
  serialized_end=500,
)
_sym_db.RegisterEnumDescriptor(_CHAINCODESPEC_TYPE)


_CHAINCODEID = _descriptor.Descriptor(
  name='ChaincodeID',
  full_name='protos.ChaincodeID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='protos.ChaincodeID.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='protos.ChaincodeID.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='protos.ChaincodeID.version', index=2,
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
  ],
  serialized_start=55,
  serialized_end=113,
)


_CHAINCODEINPUT_DECORATIONSENTRY = _descriptor.Descriptor(
  name='DecorationsEntry',
  full_name='protos.ChaincodeInput.DecorationsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='protos.ChaincodeInput.DecorationsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='protos.ChaincodeInput.DecorationsEntry.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=227,
  serialized_end=277,
)

_CHAINCODEINPUT = _descriptor.Descriptor(
  name='ChaincodeInput',
  full_name='protos.ChaincodeInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='args', full_name='protos.ChaincodeInput.args', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='decorations', full_name='protos.ChaincodeInput.decorations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_init', full_name='protos.ChaincodeInput.is_init', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CHAINCODEINPUT_DECORATIONSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=116,
  serialized_end=277,
)


_CHAINCODESPEC = _descriptor.Descriptor(
  name='ChaincodeSpec',
  full_name='protos.ChaincodeSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='protos.ChaincodeSpec.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chaincode_id', full_name='protos.ChaincodeSpec.chaincode_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='input', full_name='protos.ChaincodeSpec.input', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='protos.ChaincodeSpec.timeout', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CHAINCODESPEC_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=280,
  serialized_end=500,
)


_CHAINCODEDEPLOYMENTSPEC = _descriptor.Descriptor(
  name='ChaincodeDeploymentSpec',
  full_name='protos.ChaincodeDeploymentSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chaincode_spec', full_name='protos.ChaincodeDeploymentSpec.chaincode_spec', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code_package', full_name='protos.ChaincodeDeploymentSpec.code_package', index=1,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=503,
  serialized_end=635,
)


_CHAINCODEINVOCATIONSPEC = _descriptor.Descriptor(
  name='ChaincodeInvocationSpec',
  full_name='protos.ChaincodeInvocationSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chaincode_spec', full_name='protos.ChaincodeInvocationSpec.chaincode_spec', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=637,
  serialized_end=734,
)


_LIFECYCLEEVENT = _descriptor.Descriptor(
  name='LifecycleEvent',
  full_name='protos.LifecycleEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chaincode_name', full_name='protos.LifecycleEvent.chaincode_name', index=0,
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
  serialized_start=736,
  serialized_end=776,
)


_CDSDATA = _descriptor.Descriptor(
  name='CDSData',
  full_name='protos.CDSData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='protos.CDSData.hash', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadatahash', full_name='protos.CDSData.metadatahash', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=778,
  serialized_end=823,
)


_CHAINCODEDATA = _descriptor.Descriptor(
  name='ChaincodeData',
  full_name='protos.ChaincodeData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='protos.ChaincodeData.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='protos.ChaincodeData.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='escc', full_name='protos.ChaincodeData.escc', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vscc', full_name='protos.ChaincodeData.vscc', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='policy', full_name='protos.ChaincodeData.policy', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='protos.ChaincodeData.data', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='protos.ChaincodeData.id', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instantiation_policy', full_name='protos.ChaincodeData.instantiation_policy', index=7,
      number=8, type=11, cpp_type=10, label=1,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=826,
  serialized_end=1038,
)

_CHAINCODEINPUT_DECORATIONSENTRY.containing_type = _CHAINCODEINPUT
_CHAINCODEINPUT.fields_by_name['decorations'].message_type = _CHAINCODEINPUT_DECORATIONSENTRY
_CHAINCODESPEC.fields_by_name['type'].enum_type = _CHAINCODESPEC_TYPE
_CHAINCODESPEC.fields_by_name['chaincode_id'].message_type = _CHAINCODEID
_CHAINCODESPEC.fields_by_name['input'].message_type = _CHAINCODEINPUT
_CHAINCODESPEC_TYPE.containing_type = _CHAINCODESPEC
_CHAINCODEDEPLOYMENTSPEC.fields_by_name['chaincode_spec'].message_type = _CHAINCODESPEC
_CHAINCODEINVOCATIONSPEC.fields_by_name['chaincode_spec'].message_type = _CHAINCODESPEC
_CHAINCODEDATA.fields_by_name['policy'].message_type = common_dot_policies__pb2._SIGNATUREPOLICYENVELOPE
_CHAINCODEDATA.fields_by_name['instantiation_policy'].message_type = common_dot_policies__pb2._SIGNATUREPOLICYENVELOPE
DESCRIPTOR.message_types_by_name['ChaincodeID'] = _CHAINCODEID
DESCRIPTOR.message_types_by_name['ChaincodeInput'] = _CHAINCODEINPUT
DESCRIPTOR.message_types_by_name['ChaincodeSpec'] = _CHAINCODESPEC
DESCRIPTOR.message_types_by_name['ChaincodeDeploymentSpec'] = _CHAINCODEDEPLOYMENTSPEC
DESCRIPTOR.message_types_by_name['ChaincodeInvocationSpec'] = _CHAINCODEINVOCATIONSPEC
DESCRIPTOR.message_types_by_name['LifecycleEvent'] = _LIFECYCLEEVENT
DESCRIPTOR.message_types_by_name['CDSData'] = _CDSDATA
DESCRIPTOR.message_types_by_name['ChaincodeData'] = _CHAINCODEDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ChaincodeID = _reflection.GeneratedProtocolMessageType('ChaincodeID', (_message.Message,), dict(
  DESCRIPTOR = _CHAINCODEID,
  __module__ = 'peer.chaincode_pb2'
  # @@protoc_insertion_point(class_scope:protos.ChaincodeID)
  ))
_sym_db.RegisterMessage(ChaincodeID)

ChaincodeInput = _reflection.GeneratedProtocolMessageType('ChaincodeInput', (_message.Message,), dict(

  DecorationsEntry = _reflection.GeneratedProtocolMessageType('DecorationsEntry', (_message.Message,), dict(
    DESCRIPTOR = _CHAINCODEINPUT_DECORATIONSENTRY,
    __module__ = 'peer.chaincode_pb2'
    # @@protoc_insertion_point(class_scope:protos.ChaincodeInput.DecorationsEntry)
    ))
  ,
  DESCRIPTOR = _CHAINCODEINPUT,
  __module__ = 'peer.chaincode_pb2'
  # @@protoc_insertion_point(class_scope:protos.ChaincodeInput)
  ))
_sym_db.RegisterMessage(ChaincodeInput)
_sym_db.RegisterMessage(ChaincodeInput.DecorationsEntry)

ChaincodeSpec = _reflection.GeneratedProtocolMessageType('ChaincodeSpec', (_message.Message,), dict(
  DESCRIPTOR = _CHAINCODESPEC,
  __module__ = 'peer.chaincode_pb2'
  # @@protoc_insertion_point(class_scope:protos.ChaincodeSpec)
  ))
_sym_db.RegisterMessage(ChaincodeSpec)

ChaincodeDeploymentSpec = _reflection.GeneratedProtocolMessageType('ChaincodeDeploymentSpec', (_message.Message,), dict(
  DESCRIPTOR = _CHAINCODEDEPLOYMENTSPEC,
  __module__ = 'peer.chaincode_pb2'
  # @@protoc_insertion_point(class_scope:protos.ChaincodeDeploymentSpec)
  ))
_sym_db.RegisterMessage(ChaincodeDeploymentSpec)

ChaincodeInvocationSpec = _reflection.GeneratedProtocolMessageType('ChaincodeInvocationSpec', (_message.Message,), dict(
  DESCRIPTOR = _CHAINCODEINVOCATIONSPEC,
  __module__ = 'peer.chaincode_pb2'
  # @@protoc_insertion_point(class_scope:protos.ChaincodeInvocationSpec)
  ))
_sym_db.RegisterMessage(ChaincodeInvocationSpec)

LifecycleEvent = _reflection.GeneratedProtocolMessageType('LifecycleEvent', (_message.Message,), dict(
  DESCRIPTOR = _LIFECYCLEEVENT,
  __module__ = 'peer.chaincode_pb2'
  # @@protoc_insertion_point(class_scope:protos.LifecycleEvent)
  ))
_sym_db.RegisterMessage(LifecycleEvent)

CDSData = _reflection.GeneratedProtocolMessageType('CDSData', (_message.Message,), dict(
  DESCRIPTOR = _CDSDATA,
  __module__ = 'peer.chaincode_pb2'
  # @@protoc_insertion_point(class_scope:protos.CDSData)
  ))
_sym_db.RegisterMessage(CDSData)

ChaincodeData = _reflection.GeneratedProtocolMessageType('ChaincodeData', (_message.Message,), dict(
  DESCRIPTOR = _CHAINCODEDATA,
  __module__ = 'peer.chaincode_pb2'
  # @@protoc_insertion_point(class_scope:protos.ChaincodeData)
  ))
_sym_db.RegisterMessage(ChaincodeData)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\"org.hyperledger.fabric.protos.peerZ,github.com/hyperledger/fabric-protos-go/peer'))
_CHAINCODEINPUT_DECORATIONSENTRY.has_options = True
_CHAINCODEINPUT_DECORATIONSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
