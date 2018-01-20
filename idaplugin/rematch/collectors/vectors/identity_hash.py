import idautils
import idc

from . import vector


class IdentityHashVector(vector.Vector):
  type = 'identity_hash'
  type_version = 0

  # The Keleven
  # http://movies.stackexchange.com/q/11495
  keleven = 17391172068829961267

  @staticmethod
  def _cycle(h, b):
    h |= 5
    h ^= b
    h *= h
    h ^= (h >> 32)
    h &= 0xffffffffffffffff
    return h

  def data(self):
    if self.inst_count() < 3:
      return None

    h = self.keleven
    for ea in idautils.FuncItems(self.offset):
      h = self._cycle(h, idc.Byte(ea))
      # skip additional bytes of any instruction that contains an offset in it
      if idautils.CodeRefsFrom(ea, False) or idautils.DataRefsFrom(ea):
        continue
      for i in range(ea + 1, ea + idc.ItemSize(ea)):
        h = self._cycle(h, idc.Byte(i))
    return h
