# CIMPS
Scrit to manage CIMPS certificates.

## Before starting
You need to use a UNIX based O.S., the script was used at MacOS Monterey, Manajaro, and Ubuntu.

Elements you need install:

- PDFTK.
- Libre Office.
- Typoghrapy used at certificates.
- MySQL.
- Python requirements text file.

Just in case you don't know how to install requirements text file.
Just need to type at the terminal the following command.
```bash
source env/bin/activate &&
pip install requirements.txt &&
deactivate

```

Elements you need to check:

- Once Installed you need access to google drive API, and authorize your account.
- After that you need to create a Backup to DB used or updated to create the certificates.
- Next, you need to update the query to get the recent information.
- And you need to map the elements at the certertificate, which element correspond to the information you need to show.
- Finally check the folder id in case you need to upload files at drive, and the pwd of email account is the same, otherwise update it.

## ENV file settings

You need the following environment variables to run script:
```
CREDENTIALS = ''
DRIVE_FOLDER_ID = ''
EMAIL_NAME = 'test@example.com'
EMAIL_PWD = test
DB_USER = user
DB_PWD = pwd
DB_PORT = 0000
DB_HOST = 'localhost'
DB_NAME = 'test'
CIMPS_YEAR = 1999
CIMPS_EDITION = 10ma
CIMPS_NEXT_EDITION = 11va
PWD_FILE = 'test'
```
.ENV file must be at the same level as the run.py file

## How to Run it.

Just need to type at the terminal the following command.
```bash
source env/bin/activate &&
python run.py &&
deactivate

```
