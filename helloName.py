def greeting(name):
    return f"Hello, {name}!"

def multilang_greeting(lang="en"):
    if lang == "en":
       return f"Hello!"
    elif lang == "ru":
        return "Привет!"
    else:
        return r"¯\_(ツ)_/¯"

imya = input("What is your name?\n")
print(greeting(imya))