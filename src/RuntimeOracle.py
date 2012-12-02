class RuntimeOracle:
    """Handles the run-time assertion checking of Uroborus-instrumented code.

    Specifically, RuntimeOracle keeps track of passes and failures of each
    'run', which are defined by subsequent calls to <code>assertTrue</code>,
    and in writes the results to a file. 
    """

    pass_count = 0
    fail_count = 0
    run = 0
    current_run = True

    def __init__(self, datafile):
        """Create a new RuntimeOracle that writes its data to <code>datafile</code>."""
        self.FILE = open(datafile, 'w')

    def getRunNum(self):
        return self.run

    # assertTrue now NEVER increments run.
    # The uroborus module will call run_complete to delineate runs, which will happen
    # after each test method is called.
    def assertTrue(self, expr):
        boolResult = bool(expr) # In case we got some other nonsense
        self.current_run = self.current_run and boolResult

    def assertEquals(self, arg1, arg2):
        return self.assertTrue(arg1 == arg2)

    def run_complete(self):
        if self.current_run:
            self.pass_count += 1
            self.FILE.write(str(self.run) + '\t' + str(1) + '\n')
        else:
            self.fail_count += 1
            self.FILE.write(str(self.run) + '\t' + str(0) + '\n')
        self.run = self.run + 1
        this_run = self.current_run
        self.current_run = True
        return this_run

    def except_fail(self):
        self.current_run = False
        self.run_complete()

    def passes(self):
        return self.pass_count

    def fails(self):
        return self.fail_count
