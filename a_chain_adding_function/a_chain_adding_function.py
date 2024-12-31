def add(n):
    def inner (y=None):
        if y is None:
            return n
        return add(n+y)
    inner.__call__ = lambda: n
    return inner

print(add(1)(2))
