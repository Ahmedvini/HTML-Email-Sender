# Gmail Draft Creator

This Python script allows you to create Gmail drafts from HTML files. It uses the Gmail API and requires users to provide their own Google Cloud credentials.

## Features

*   Creates Gmail drafts from user-selected HTML files.
*   Uses a file dialog to select both the `credentials.json` and the HTML file.
*   Handles the OAuth 2.0 authentication flow.

## Requirements

*   Python 3.6+
*   `google-api-python-client` library
*   `google-auth-oauthlib` library
*   `tkinter` (usually comes pre-installed with Python, but might need to be installed separately on some Linux distributions. See setup steps.)

## Setup

### 1. Create a Google Cloud Project

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Sign in with the Google account you want to use for creating drafts.
3. Click the project dropdown (usually says "Select a project").
4. Click "New Project".
5. Give your project a name (e.g., "Gmail Draft Creator").
6. Click "Create".

### 2. Enable the Gmail API

1. In the Google Cloud Console, make sure your newly created project is selected.
2. Go to "APIs & Services" -> "Library" (in the left-hand menu).
3. Search for "Gmail API".
4. Click on "Gmail API".
5. Click "Enable".

### 3. Create OAuth 2.0 Credentials

1. In the Google Cloud Console, go to "APIs & Services" -> "Credentials".
2. Click "+ Create Credentials" and select "OAuth client ID".
3. Select "Desktop app" as the "Application type".
4. Give your client ID a name (e.g., "Gmail Draft Creator Client").
5. Click "Create".
6. Click the download button (downward-pointing arrow) next to the client ID you just created. This will download a JSON file.
7. Rename the downloaded file to `credentials.json`. *Keep this file safe and do not share it with anyone.*

### 4. Configure OAuth Consent Screen

1. In the Google Cloud Console, go to "APIs & Services" -> "OAuth consent screen".
2. Choose "External" for the User Type and click "Create".
3. Fill in the required information:
    *   **App name:** (e.g., "Gmail Draft Creator")
    *   **User support email:** Your email address
    *   **Developer contact information:** Your email address.
4. Click "Save and Continue".
5. Click "Add or Remove Scopes".
6. In the "Manually add scopes" box, paste: `https://www.googleapis.com/auth/gmail.compose`
7. Click "Add to table"
8. Click "Update".
9. Click "Save and Continue".
10. Click "+ Add Users" under test users.
11. Add your email.
12. Click "Save and Continue".

### 5. Install Python and Dependencies

1. Make sure you have Python 3.6 or higher installed. You can check by running `python3 --version` in your terminal.
2. Install the required libraries using `pip`:
    ```bash
    pip install -r requirements.txt
    ```
3. **Install `tkinter` (if needed):**
    On some Linux distributions, you might need to install `tkinter` separately:
    *   **Debian/Ubuntu/Pop!_OS:**
        ```bash
        sudo apt-get update
        sudo apt-get install python3-tk
        ```
    *   **Fedora/CentOS/RHEL:**
        ```bash
        sudo dnf install python3-tkinter
        ```

## Usage

1. Run the script:
    ```bash
    python your_script_name.py
    ```
    (Replace `your_script_name.py` with the actual name of your Python file.)

2. A file dialog will open. Select your `credentials.json` file.

3. You'll be redirected to a Google sign-in page in your browser. Sign in with the same Google account you used to create the project.

4. Grant the application permission to access your Gmail account (specifically, to create drafts).

5. Another file dialog will open. Select the HTML file you want to use for your draft.

6. The script will create a draft in your Gmail account.

## Troubleshooting

*   **`ModuleNotFoundError: No module named 'tkinter'`:**  See the "Install Python and Dependencies" section for instructions on installing `tkinter`.
*   **`FileNotFoundError: [Errno 2] No such file or directory: 'credentials.json'`:** Make sure you have downloaded the `credentials.json` file, renamed it correctly, and that you are selecting the correct file in the file dialog.
*   **`HttpError 403` (accessNotConfigured):**  Make sure you have enabled the Gmail API for your project in the Google Cloud Console. Wait a few minutes after enabling the API before running the script again.
*   **Other Errors:** Carefully read the error messages. They often provide clues about what went wrong.

## Contributing

If you'd like to contribute to this project, please feel free to submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details. (You'll need to create a LICENSE file - see step 5 below).
