from socketIO_client import SocketIO, LoggingNamespace

def on_bbb_response(*args):
    print('on_bbb_response', args)

with SocketIO('localhost', 9100) as socketIO:
    socketIO.emit('message', {'xxx': 'yyy'}, on_bbb_response)
    socketIO.wait_for_callbacks(seconds=1)
