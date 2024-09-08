# docker_flask_test
This project is a simple demonstration of how to containerize a Flask application using Docker. It aims to provide a practical example of deploying a minimal Flask web app inside a Docker container for testing and development purposes.



This project demonstrates how to set up a basic Flask web application using `pipenv` for virtual environment and dependency management.

## Project Setup

### 1. Create Project Directory
-Create folder `flask_test`
-Go to directory of project ->pipenv install

```bash
mkdir flask_test
flask_test -> pipenv install
```

<img src="images/1.png" alt="Image 1" width="80%" height="100%">

### Pipenv Installation

When you run the `pipenv install` command, Pipenv will automatically generate the `Pipfile.lock` file.

<img src="images/2.png" alt="Image 2" width="80%" height="100%">

### Pipenv Commands

To activate the virtual environment:

```bash
pipenv shell
```

### Install development pandas dependency
```bash
pipenv install -dev pandas
```
<img src="images/3.png" alt="Image 3" width="80%" height="100%">

### Install Flask depencency
```bash
pipenv install -dev flask
```
<img src="images/4.png" alt="Image 1" width="80%" height="100%">

#### When you check the file, you can see the installed dependencies in the Pipfile and Pipfile.lock files
<img src="images/5.png" alt="Image 4" width="80%" height="100%">

### Create a main.py for testing.
<img src="images/6.png" alt="Image 6" width="80%" height="100%">

### Run the file.

<img src="images/7.png" alt="Image 7" width="80%" height="100%">
&nbsp;&nbsp;&nbsp;&nbsp;

<img src="images/8.png" alt="Image 8" width="80%" height="100%">



## Using `python-dotenv` for Environment Variables

`python-dotenv` is a Python library that allows you to load environment variables from a `.env` file into your Python project's environment. 

This is especially useful for managing sensitive configuration settings like API keys, database credentials, and environment-specific variables without hardcoding them into your code.

### Installation

To install `python-dotenv`

```bash
pipenv install --dev python-dotenv
```

<img src="images/9.png" alt="Image 9" width="80%" height="100%">

### Create .env file and set up variable
<img src="images/10.png" alt="Image 10" width="80%" height="100%">

### To check the environment varible, create test.ipynb.
<img src="images/11.png" alt="Image 11" width="80%" height="100%">

### Update main.py and run.
<img src="images/12.png" alt="Image 12" width="80%" height="100%">

&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;

<img src="images/13.png" alt="Image 13" width="80%" height="100%">