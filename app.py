from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/run")
def run():
    user_input = request.args.get("cmd")

    #subprocess.run(f"ls {user_input}", shell=True)
    return "done"
