class frozendict(dict):
    """Un diccionario inmutable."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def __hash__(self):
        return hash(tuple(sorted(self.items())))
    
    def __setitem__(self, key, value):
        raise TypeError("frozendict es inmutable")
    
    def __delitem__(self, key):
        raise TypeError("frozendict es inmutable")
