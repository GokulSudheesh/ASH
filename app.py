from flask import Flask, render_template, request, url_for
import chatBot

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/get')
def reply():
    message = request.args.get("data")
    #print(message)
    try:
        return chatBot.get_response(message)
    except:
        return ("Try again.")


if __name__ == '__main__':
    app.run(debug=True)