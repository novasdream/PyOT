# This is a shadow of the main branch, 9.51
import base
from struct import pack

provide = []

def verify(): return True


class Packet(base.BasePacket):
    maxOutfits = 33
    maxMounts = 31

    # Magic Effect
    def magicEffect(self, pos, type):
        self.raw(pack("<BHHBB", 0x83, pos.x, pos.y, pos.z, type))
        
class Protocol(base.BaseProtocol):
    Packet = Packet
