import pywhatkit
from flask import Flask, request, render_template_string
from whatsappKit import sendwhatmsg  
from datetime import datetime

app = Flask(__name__)

TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Send WhatsApp Message</title>
</head>
<body>
  <h1>Send WhatsApp Message</h1>
  <form action="/send" method="post">
    <label for="phone_number">Phone Number:</label>
    <input type="text" id="phone_number" name="phone_number" required><br><br>
    
    <label for="message">Message:</label>
    <textarea id="message" name="message" required></textarea><br><br>

    <label for="hour">Hour (24-hour format):</label>
    <input type="number" id="hour" name="hour" min="0" max="23" required><br><br>
    
    <label for="minute">Minute:</label>
    <input type="number" id="minute" name="minute" min="0" max="59" required><br><br>
    
    <input type="submit" value="Send Message">
  </form>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(TEMPLATE)

@app.route('/send', methods=['POST'])
def send():
    phone_number = request.form['phone_number']
    message = request.form['message']
    hour = int(request.form['hour'])
    minute = int(request.form['minute'])
    
    current_time = datetime.now()
    if current_time.hour > hour or (current_time.hour == hour and current_time.minute > minute):
        return "Target time is in the past"
    else:
        sendwhatmsg(phone_number, message, hour, minute)
        return "Message sent!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
