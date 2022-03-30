class Singleton:

    _instance = None

    @classmethod
    def get(cls):
        if cls._instance is None:
            cls._instance = cls()

        return cls._instance
