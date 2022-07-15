from flask import Flask
from flask_mail import Mail, Message

mail = Mail()

app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'roujanmavarani@gmail.com'
app.config['MAIL_PASSWORD'] = '*******'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail.init_app(app)



@app.route("/")
def index():
  msg = Message('Hello from the other side!',
                sender =   'roujanmavarani@gmail.com',
                recipients = ['mavarani@hotmail.co.uk'])
  msg.body = "Hey Paul, sending you this email from my Flask app, lmk if it works"
  mail.send(msg)
  return "Message sent!"
  
    
