import code
import sys

def interact(locals=None):
    savestdout = sys.stdout
    sys.stdout = sys.stderr

    try:
        import bpython
        banner = open(locals['__file__']).read()
        bpython.embed(locals, banner=banner)
    except ImportError:
        console = code.InteractiveConsole(locals)
        console.interact()

    sys.stdout = savestdout 
