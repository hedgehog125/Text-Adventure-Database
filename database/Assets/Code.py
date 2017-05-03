def runFile(file):
    exec(compile(open(file, "rb").read(), file, 'exec'))

runFile("Text adventure.py")