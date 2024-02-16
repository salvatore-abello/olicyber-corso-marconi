import subprocess
from flask import Flask, request

app = Flask(__name__) 

@app.get("/")
def index():
    host = request.args.get("host") 

    if host:
        #! :think:
        return subprocess.check_output(f"ping {host}", shell=True).decode()
    else:
        return "Hello World"

if __name__ == "__main__":
    app.run("0.0.0.0", 1337)