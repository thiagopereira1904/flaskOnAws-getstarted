from flask import Flask

app = Flask(_name_)


@app.route("/")
def hello_word():
    return "<p>Hello, Word!</p>"


#Teste