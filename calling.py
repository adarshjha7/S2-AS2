import numpy as np
import cv2 
from twilio.rest import Client

# Twilio credentials
account_sid = 'Enter_your_id'
auth_token = 'Enter_your_token'
client = Client(account_sid, auth_token)

# Function to initiate a voice call using Twilio
def initiate_voice_call():
    try:
        call = client.calls.create(
            to='+917355578308',  # Recipient's phone number
            from_='+14326140859',  # Your Twilio phone number
            url='http://demo.twilio.com/docs/voice.xml'  # TwiML URL or call instructions
        )
        print(f"Voice call initiated successfully. Call SID: {call.sid}")
    except Exception as e:
        print(f"Error initiating voice call: {str(e)}")

# Function to send an SMS with a message
def send_sms_with_message():
    try:
        message = client.messages.create(
            to='+917355578308',  # Recipient's phone number
            from_='+14326140859',  # Your Twilio phone number
            body='sPa-s MESSAGE NOTIFICATION : https://drive.google.com/drive/u/1/folders/1oQ5z-Pnlp9V0KKdi0wKIbvRJlFQ5vpwK',
        )
        print(f"SMS sent successfully. Message SID: {message.sid}")
    except Exception as e:
        print(f"Error sending SMS: {str(e)}")

# Open the camera
cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        out.write(frame)
        cv2.imshow('output', frame)
        
        # Break loop on 'q' key press
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    else:
        break

# Release camera and video writer resources
cap.release()
out.release()
cv2.destroyAllWindows()

# After camera loop, initiate voice call and send SMS
initiate_voice_call()
send_sms_with_message()
