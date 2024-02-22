# Project Structure

The MLOP-ASSIGNMENT project follows a structured directory layout:

- **BoYu/:** This directory contains data and files related to the BoYu project component:
`data/`: 

  - Contains the `01_homely_resort_listing.csv` file, which is part of the BoYu project.

  
- **data/:** This directory stores project data files.

- **docs/:** Contains documentation files relevant to the project.

- **models/:** Contains trained model files.
    - boyu_model.pkl: A trained model file for predicting rental price.
    - final_mushroom_model.pkl: A trained model to identification and classification for mushrooms.

- **notebooks/:** Contains Jupyter notebooks used for data exploration, analysis, and model training. For example, `214322H_Assignment.ipynb`.

- **WebApp/:** Holds files for the web application component:
  - **static/:** Stores static files like CSS, images, and JavaScript.
  - **css/:** Includes CSS stylesheets such as formstyle.css, style.css, and svg.css.
  - **images/:** Houses images like ‘mushroom1.jpg’, ‘mushroom2.jpg’, ‘rental_1.jpg’, and ‘rental_2.jpg’ used in the web app.
  - **‘js/’:** Contains JavaScript file named ‘base.js’.
  - **templates/:** Holds HTML template files like ‘base.html’, ‘home.html’, ‘mushroom.html’, and ‘rental.html’ used by Flask to generate web pages.
  - **‘app.py’:** The main Python file running the Flask web application.
  
- **poetry/:** This folder cotains all the poetry requirements for dependency management.

- **installed_packages.txt** This file contains all my libraries installed in Visual Studio Code.
  
- **logs.log:** A log file capturing events or errors while running applications.
  
- **pyproject.toml:** A configuration file containing settings for building packages among other things.
  
- **README.md:** Provides an overview of the project including instructions or details about the project.
  
- **requirements.txt:** Lists Python dependencies required for executing or developing applications within this project environment.

Please refer to the individual directories for more detailed information.

GitHub link: [MLOP-ASSIGNMENT](https://github.com/cheeboyu/mlop-assignment)

Render link:
https://boyu-mlop-assignment.onrender.com/