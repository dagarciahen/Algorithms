class Mapping:
    def get(self, key):
        raise NotImplementedError

    def put(self, key, value):
        raise NotImplementedError
    def __len__(self):
        raise NotImplementedError

    def _entryiter_(self):
        raise NotImplementedErrr
    def __iter__(self):
        return (e.key for e in self._entryiter())
    def values(self):
        return (e.value for e in self._entryiter())

    def items(self):
        return ((e.key, e.value) for e in self._entryiter())

