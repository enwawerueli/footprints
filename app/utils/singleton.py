class Singleton:
    """Manages instanciation of decorated class to limit to only a
    single instance"""

    def __init__(self, klass):
        self._Class = klass
        self._instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = self._Class(*args, **kwargs)
        return self._instance
