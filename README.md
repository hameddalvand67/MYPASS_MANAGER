
# Vault — Local Password & Credential Management Website

A simple and complete Django website for storing login credentials and information for servers, services, and various accounts.

The data can only be managed (add/edit/delete) through the Django Admin Panel. However, a clean and dedicated interface is provided for viewing and searching stored information, with a copy button for each individual field.

## Data Model

* **Entry**: A general item, such as a server, email account, bank account, hosting service, etc. Each entry contains a title, category, and general notes.
* **Section**: Each entry can contain multiple sections. For example, a server can have SSH, a hosting panel, and a database. Each section can have its own URL, username, password, and additional information.

This structure is designed specifically for scenarios where a single server or service has multiple separate components, each with its own login credentials.

## Installation and Local Setup

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create database tables
python manage.py migrate

# Create an admin user
python manage.py createsuperuser

# Start the development server
python manage.py runserver
```

After starting the server:

* **Main page (list and search):** `http://127.0.0.1:8000/`
* **Admin Panel (add/edit/delete entries and sections):** `http://127.0.0.1:8000/admin/`

Log in using the username and password you created with `createsuperuser`.

The same user account is used to access both the main website and the Django Admin Panel.

## Sample Data

The project includes two sample entries in the database so you can quickly see how the application works. They contain fake credentials for demonstration purposes.

You can delete them from the Admin Panel whenever you want.

If you want to start completely from scratch, simply delete the `db.sqlite3` file and run:

```bash
python manage.py migrate
python manage.py createsuperuser
```

### Sample Admin Account

A sample admin account is included:

* **Username:** `admin`
* **Password:** `admin12345`

**For security, change this password immediately from the Admin Panel under the Users section.**

## Adding a New Entry

1. Go to `/admin/` and log in.
2. Click **Entries** and select **Add Entry**.
3. Enter the title, category, and general notes.
4. At the bottom of the page, you will find the **Sections** area. Add a separate row for each component, such as SSH, Hosting Panel, Database, FTP, etc.
5. Enter the URL, username, password, and any additional information.
6. Save the entry.

The new entry will now appear on the main page.

## Search

The search feature on the main page searches across all of the following fields:

* Entry title
* Category
* General notes
* Section titles
* URLs
* Usernames
* Additional information

This makes it easy to quickly find a server, service, account, or specific credential.

## Security

Although this application is intended for local use, it still stores sensitive information and should be treated carefully.

* The project is configured with `DEBUG = True`, which is suitable only for local development. **Do not publish this configuration to the Internet.**
* Passwords are currently stored as plain text in the SQLite database. They are **not encrypted** because the application is intended to run only on your local computer.
* If needed, encryption can be added later using a **master password** or another secure key-management mechanism.
* All main pages, including the entry list and entry details, are accessible only to authenticated staff/admin users.
* The Django Admin Panel is used to manage all entries and sections.

> **Important:** If the database file or the computer itself is compromised, the stored credentials may be exposed because passwords are currently stored in plain text.

## Project Structure

```text
vaultsite/                  Main Django project configuration
│
├── vault/                  Main application
│   ├── models.py           Entry and Section models
│   ├── admin.py            Django Admin configuration with Section inline
│   ├── views.py            List, search, and detail views
│   │
│   ├── templates/
│   │   └── vault/          HTML templates
│   │
│   └── static/
│       └── vault/          CSS and JavaScript files
│                            (including copy functionality)
│
├── db.sqlite3              SQLite database
├── manage.py               Django management script
└── requirements.txt        Python dependencies
```
