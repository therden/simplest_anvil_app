import anvil.server

SPLASH = '''
Anvil Runtime Server 'Simplest App' is working...

Try the following routes:
    /ping
    /hello
    /hello/{your name here}
'''

@anvil.server.route("/")
def root(**p):
    return SPLASH

@anvil.server.route("/ping")
def ping(**p):
    return "pong"

@anvil.server.route("/hello")
def say_hello_back(**p):
    return "Hello back"

@anvil.server.route("/hello/:input")
def say_hello_back(input, **p):
    if input:
        return f"Hello {input}!"
    else:
        return "Hello [Anonymous]!"

