from flask import Flask, request, render_template

from whatsappKit import sendwhatmsg

from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    phone_number = request.form['phone_number']
    message = request.form['message']
    hour = int(request.form['hour'])
    minute = int(request.form['minute'])

    if datetime.now().hour > hour or datetime.now().minute > minute:
        return "Target time is in the past"
    else:
        sendwhatmsg(phone_number, message, hour, minute)
        return "Message sent!"
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)