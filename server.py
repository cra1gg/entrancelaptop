import flask
import os
import pyautogui

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/sleep', methods=['PUT'])
def sleep():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    return "<h1>Command run sucessfully!</h1>"

@app.route('/wake', methods=['GET'])
def keypress():
    pyautogui.press('shift')
    pyautogui.press('shift')
    pyautogui.press('shift')
    return "<h1>Command run sucessfully!</h1>"

app.run(host='0.0.0.0', port=8080)