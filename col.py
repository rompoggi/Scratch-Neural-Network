class col:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def __innit__(self):
        return
    
    def fail_(self, msg):
        return self.FAIL + msg + self.ENDC

    def fail(self,msg):
        print(self.fail_(msg))

    def warn_(self,msg):
        return self.WARNING + msg + self.ENDC
    
    def warn(self,msg):
        print(self.warn_(msg))

    def ok_(self,msg):
        return self.OKGREEN + msg + self.ENDC

    def ok(self,msg: str):
        print(self.ok_(msg))

    def okblue_(self,msg: str):
        return self.OKBLUE + msg + self.ENDC

    def okblue(self,msg):
        print(self.okblue_(msg))

    def okcyan_(self,msg: str):
        return self.OKCYAN + msg + self.ENDC

    def okcyan(self,msg):
        print(self.okcyan_(msg))

    def okgreen_(self,msg: str):
        return self.OKGREEN + msg + col.ENDC

    def okgreen(self,msg):
        print(self.okgreen_(msg))

    def header_(self,msg: str):
        return self.HEADER + msg + col.ENDC

    def header(self,msg: str):
        print(self.header_(msg))

    def bold_(self,msg: str):
        return self.BOLD + msg + col.ENDC
    
    def bold(self,msg: str):
        print(self.bold_(msg))

    def underline_(self,msg: str):
        return self.UNDERLINE + msg + col.ENDC

    def underline(self,msg: str):
        print(self.underline_(msg))

    def show(self):
        self.fail("This is a fail message ")
        self.warn("This is a warn message")
        self.ok("This is an ok message")
        self.okblue("This is an okblue message")
        self.okcyan("This is an okcyan message")
        self.okgreen("This is an okgreen message")
        self.header("This is a header message")
        self.bold("This is a bold message")
        self.underline("This is a underline message")

# col = col()

# col.show()