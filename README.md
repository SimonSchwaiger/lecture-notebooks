# lecture-notebooks
This repository includes interactive Jupyter notebooks that complement my robotics programming courses.

Jupyter notebooks are files that contain text, figures as well as executable code and code output. You can either view the notebooks statically or interactively, which allows you to run and modify code cells.

# Recommended Usage

You can interact with the notebooks in a cloud instance without having to install any software on your PC.

1. Interactive Online Session using [Binder](https://mybinder.org/)
    * Just click on the desired Notebook's Binder widget to launch an interactive online session containing the notebook in Jupyterlab.
    * **Basics Notebook** 
    
        [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/SimonSchwaiger/lecture-notebooks/HEAD?labpath=app%2FNotebooks%2FBasics.ipynb)
    * **Data Manipulation and Visualisation Notebook**
    * **Python and ROS Notebook**

# Alternative Usage Methods

Alternatively, you can view the notebooks using these other methods.

2. Online Preview:
    * You can directly preview them here on GitHub
    * However, the notebooks will not be interactive
    * The notebooks can be fuond in the [`app/Notebooks`](./app/Notebooks/) folder

3. Local Preview using [Visual Studio Code](https://code.visualstudio.com/)
    * Install Visual Studio Code and clone this repository
    * Double-click on the desired notebook in the [`/app/Notebooks`](./app/Notebooks/) folder

4. Local Preview Using Docker and Jupyterlab
    * Install Docker on your platform (Windows + WSL or natively on Linux) and run the [`buildandrun.sh`](./buildandrun.sh) script.
    * Detailed install and run instructions for the docker-based environment are provided [here](https://github.com/SimonSchwaiger/ros-ml-container).
