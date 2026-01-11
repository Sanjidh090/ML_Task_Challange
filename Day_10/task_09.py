def bold(func):
    def wrap():
        return "<b>" + func() + "</b>"
    return wrap

def italic(func):
    def wrap():
        return "<i>" + func() + "</i>"
    return wrap
@italic
@bold

def text():
    return "Hello"

print(text())
