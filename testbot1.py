import requests
import json

def send_message(access_token, recipient_id, message_text):
    params = {
        "access_token": access_token
    }

    headers = {
        "Content-Type": "application/json"
    }

    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": message_text
        }
    })

    r = requests.post("https://graph.facebook.com/v12.0/me/messages", params=params, headers=headers, data=data)

    if r.status_code != 200:
        print("Error sending message:", r.text)
    else:
        print("Message sent successfully.")

def main():
    access_token = input("Enter your access token: ")
    recipient_id = input("Enter the recipient ID: ")
    message_text = input("Enter the message to send: ")

    send_message(access_token, recipient_id, message_text)

if __name__ == "__main__":
    main()
