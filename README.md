# Flask Restaurant Menu API

This is a simple API for managing restaurant menus, built with Flask, SQLAlchemy, Marshmallow, and APIFairy.

## Requirements

- Python 3.7+
- Pip
- Virtualenv

## Local Setup

### 1. Create a Python Virtual Environment

First, clone this repository and navigate into the newly created directory. Then create a virtual environment using the following command:

```bash
python3 -m venv venv
```

This will create a new Python virtual environment in a folder named `venv`.

### 2. Activate the Virtual Environment

Activate the virtual environment with this command:

On Windows:

```bash
venv\Scripts\activate
```

On Unix or MacOS:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

Use pip to install the dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Environment Variables

Make a copy of `.env.example` file:

```bash
cp .env.example .env
```

Edit the `.env` file with your local MySQL database details and other configurations:

```env
FLASK_APP=main.py
FLASK_ENV=development
FLASK_RUN_PORT=5000
DATABASE_DEV_URL=mysql+pymysql://username:password@localhost/dev_database
DATABASE_PROD_URL=mysql+pymysql://username:password@localhost/prod_database
SECRET_KEY=<YOUR_SECRET_KEY>
```

Here, `DB_USER` and `DB_PASSWORD` correspond to your MySQL username and password. You need to replace `your_username` and `your_password` with your actual MySQL username and password.

### 5. Database Setup

Create a new MySQL database as specified in the `.env` file. SQLAlchemy will handle the creation of tables based on your models.

### 6. Run Database Migrations

We'll be using Flask-Migrate for handling database migrations. Initialize Flask-Migrate with this command:

```bash
flask db init
```

Then, each time you make changes to your SQLAlchemy models, generate a migration script with:

```bash
flask db migrate
```

You can customize the migration script if needed, then apply the migrations to the database using:

```bash
flask db upgrade
```

### 7. Running the Application

Finally, use the following command to run the application:

```bash
flask run
```

By default, the application will run on `localhost:5000`. You can view the API documentation by navigating to `http://localhost:5000/api/docs` in your web browser.