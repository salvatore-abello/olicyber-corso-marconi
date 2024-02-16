from flask import Flask, request

app = Flask(__name__) 


#? è una post o una get?
@app.get("/")
def index():
    #! Args è di tipo 'dict' -> /?arg1=hello&arg2=world
    #! "Hello World" in questo caso è il valore di default
    data = request.args.get("query", "Hello World") 

    # Rispondo al client con il contenuto di data
    #> Content-Type: text/html
    return data 

if __name__ == "__main__":
    # Vado ad avviare il server
    app.run("0.0.0.0", 1337)