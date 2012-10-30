class RuntimeOracle:
    """Handles the run-time assertion checking of Uroborus-instrumented code.

    Specifically, RuntimeOracle keeps track of passes and failures of each
    'run', which are defined by subsequent calls to <code>assertTrue</code>,
    and in writes the results to a file. 
    """

    run = 0
    continuation = False
    current_run = True

    def __init__(self, datafile):
        """Create a new RuntimeOracle that writes its data to <code>datafile</code>."""
        self.FILE = open(datafile, 'w')

    def getRunNum(self):
        return self.run

    def assertTrue(self, expr, nextRun=True):

        boolResult = bool(expr) # In case we got some other nonsense

        # In case assert has already been called for this run, we 'and' the results
        if self.continuation:
            self.current_run = self.current_run and boolResult
        else:
            self.current_run = boolResult

        if nextRun:
            self.FILE.write(str(self.run) + '\t' + str(1 if self.current_run else 0) + '\n')
            self.run = self.run + 1
            self.continuation = False
        else:
            self.continuation = True
