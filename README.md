# Flask Web Framework for Game Catalog

This repository contains a simple Flask project that displays information about video games, such as name, category, and console. It allows users to add or remove games from their own catalog and upload an image for each game. The project utilizes a local MySQL database to store data.

This project was developed by the student during the "Flask: framework web de Python" training, which can be accessed at [Alura](https://cursos.alura.com.br/formacao-flask).

## Project Overview
The project aims to demonstrate basic CRUD operations (Create, Read, Update, Delete) using Flask and MySQL. Users can interact with the web application to manage their game catalog effectively.

## Technologies Used
- Python
- Flask
- MySQL
- HTML/CSS
- JavaScript

## Environment Variables
Before running the project, create a `.env` file in the root directory of the project and define the following variables:

```
USER_SECRET_KEY=your_secret_key
SGBD=mysql
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_SERVER=localhost
DB_NAME=your_db_name
```

Make sure to replace `your_secret_key`, `your_db_user`, `your_db_password`, and `your_db_name` with your actual values.

## Project Structure
The directory structure of the project is as follows:
```
flask-framework-web-de-python/
├── templates/
│   └── ... (HTML templates)
├── static/
│   ├── ... (css files)
│   └── ... (js files)
├── config.py
├── helpers.py
├── jogoteca.py
├── models.py
├── prepara_banco.py
├── views_game.py
├── views_user.py
├── requirements.txt
├── .gitignore
└── README.md
```

## How to Run the Project
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/flask-framework-web-de-python.git
   ```
2. Navigate to the project directory:
   ```sh
   cd flask-framework-web-de-python
   ```
3. Create a virtual environment:
   ```sh
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
5. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

6. Run the Flask application:
   ```sh
   python jogoteca.py
   ```

## Learn More
To learn more about Flask and how to develop web applications with Python, visit the [Flask documentation](https://flask.palletsprojects.com/).

Feel free to explore, modify, and use this project as a foundation for your own Flask applications!
