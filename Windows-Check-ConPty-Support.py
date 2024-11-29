import ctypes
try:
    ctypes.windll.kernel32.CreatePseudoConsole
    print("ConPTY is supported!")
except AttributeError:
    print("ConPTY is not supported.")
