class Index:
    """Class, which provides indexing the sequence of values."""

    def __init__(self, labels, name=""):
        """(Contructor). Creates an object for indexing sequence of values using given keys. If labels list is empty, and if labels contains duplicated keys, ValueErrors are raised."""
        
        if len(set(labels)) != len(labels):
            raise ValueError(f"Labels list must contain every single label (key) only once.")

        if not labels:
            raise ValueError(f"Labels list must contain at least 1 label.")

        self.labels = labels
        self.name = name

    def __len__(self):
        return len(self.labels)
    
    def __iter__(self):
        """Supports iterations. Must return generator."""
        yield from self.labels

    def get_loc(self, key):
        """Translates key from labels to corresponding index. 
        If the key does not exist, ValueError is raised. If it does, the key index is returned."""

        if key not in self.labels:
            raise KeyError(f"Given key: {key} is not in labels.")
        return self.labels.index(key)
