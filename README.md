# WhatsApp Message Scheduler

A web application built with Flask to schedule WhatsApp messages for future delivery.

## Features
- Schedule WhatsApp messages with specific time (24-hour format)
- Simple web interface for user input
- Basic validation for past time entries
- Responsive design with CSS styling

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/whatsapp-scheduler.git
cd whatsapp-scheduler
```

2. Install dependencies:
```bash
pip install flask pywhatkit
```

3. Run the application
```bash 
python app.py
```

4. Access the web interface at: 
- http://localhost:4000 

## Usage
1. Ensure you're logged in to WhatsApp Web in your default browser

2. Fill in the recipient's phone number (with country code)

3. Enter your message

4. Set the delivery time in 24-hour format based on the server's local timezone

5. Click "Send Message"

6. Keep the application running until the scheduled time

## Important Notes
- ⚠️ Time input must be in the 24-hour format and should match the server's local timezone

- Phone number format: +[countrycode][number] (e.g., +1234567890)

- The application must remain running until message delivery

- Browser must stay open for WhatsApp Web integration

- Time validation checks against the server's clock, not your local time

- Ensure the scheduled time is in the future according to the server's timezone

## Directory Structure 
```
your-project/
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── app.py
├── whatsappKit.py
└── README.md
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first.




