import os
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import tkinter as tk
from tkinter import filedialog

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.compose']

def create_message(sender, to, subject, html_content):
    """Create a message for an email.

    Args:
      sender: Email address of the sender.
      to: Email address of the receiver.
      subject: The subject of the email message.
      html_content: The HTML content of the email message.

    Returns:
      An object containing a base64url encoded email object.
    """
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject

    msg = MIMEText(html_content, 'html')
    message.attach(msg)

    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw_message}

def create_draft(service, user_id, message_body):
    """Create a draft email.

    Args:
      service: Authorized Gmail API service instance.
      user_id: User's email address. The special value "me"
      can be used to indicate the authenticated user.
      message_body: The body of the email message, including headers.

    Returns:
      Draft object, including draft id and message meta data.
    """
    try:
        message = {'message': message_body}
        draft = service.users().drafts().create(userId=user_id, body=message).execute()

        print('Draft id: %s\nDraft message: %s' % (draft['id'], draft['message']))

        return draft
    except Exception as error:
        print('An error occurred: %s' % error)
        return None
def get_file(title, filetypes):
    """Opens a file dialog to let the user choose a file."""
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename(
        title=title,
        filetypes=filetypes
    )
    return file_path

def main():
    """Shows basic usage of the Gmail API."""
    creds = None

    # Always prompt for credentials.json
    credentials_path = get_file(
        "Select credentials.json",
        (("JSON files", "*.json"), ("all files", "*.*"))
    )
    if not credentials_path:
        print("No credentials file selected. Exiting.")
        return

    flow = InstalledAppFlow.from_client_secrets_file(
        credentials_path, SCOPES)
    creds = flow.run_local_server(port=0)

    try:
        # Call the Gmail API
        service = build('gmail', 'v1', credentials=creds)

        # Get HTML file using the file dialog
        html_file_path = get_file(
            "Select HTML File",
            (("HTML files", "*.html"), ("all files", "*.*"))
        )

        if html_file_path:  # Check if a file was selected
            with open(html_file_path, "r") as f:
                html_content = f.read()

            # Create the email message
            message = create_message("me", "recipient@example.com", "My HTML Email", html_content)

            # Create the draft
            create_draft(service, "me", message)
        else:
            print("No HTML file selected.")

    except HttpError as error:
        print(f'An error occurred: {error}')

if __name__ == '__main__':
    main()