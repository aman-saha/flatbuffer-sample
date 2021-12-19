# automatically generated by the FlatBuffers compiler, do not modify

# namespace: SampleClient

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Client(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Client()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsClient(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Client
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Client
    def ClientType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # Client
    def Client(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            from flatbuffers.table import Table
            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

def ClientStart(builder): builder.StartObject(2)
def Start(builder):
    return ClientStart(builder)
def ClientAddClientType(builder, clientType): builder.PrependUint8Slot(0, clientType, 0)
def AddClientType(builder, clientType):
    return ClientAddClientType(builder, clientType)
def ClientAddClient(builder, client): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(client), 0)
def AddClient(builder, client):
    return ClientAddClient(builder, client)
def ClientEnd(builder): return builder.EndObject()
def End(builder):
    return ClientEnd(builder)