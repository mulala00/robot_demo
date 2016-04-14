from robot.libraries.Remote import *


class MyRemote(Remote):
    def __init__(self, uri='http://127.0.0.1:8270', timeout=None):
        Remote.__init__(self, uri, timeout)

    def run_keyword(self, name, args, kwargs):
        coercer = ArgumentCoercer()
        args = coercer.coerce(args)
        kwargs = coercer.coerce(kwargs)
        result = RemoteResult(self._client.run_keyword(name, args, kwargs))
        print "status", result.status
        print "return", result.return_
        print "error", result.error
        print "output", result.output
        print "traceback", result.traceback
        print "fatal", result.fatal
        sys.stdout.write(result.output)
        if result.status != 'PASS':
            raise RemoteError(result.error, result.traceback, result.fatal,
                              result.continuable)
        return result.return_
