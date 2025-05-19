class Protocol:
    def __init__(self, version: int):
        if version < 1 or version > 767:
            print("version {version} not supported")
            exit()
        else:
            self.version = version
