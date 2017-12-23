# HPDF-Task1

# Requirements
1. Python 3.x (You can download it here-> https://www.python.org/downloads)
2. Flask

# Steps to use this repository
1. Download and install Python 

2. Install Flask by following the steps from -> http://flask.pocoo.org/docs/0.12/installation/#installation

3. Make a directory for the project

4. Create a virtual environment inside the directory using the command:  
     >virtualenv venv

5. Clone or download the repository inside venv 

6. Change directory into Scripts folder of venv and activate the virtual environment 
    >cd scripts
    
    >activate
   
7. Then run the app inside the Task1 folder

    /Task1>python task1.py
    
8. Thats it! Open any browser and go to the url http://localhost:5000 to see the app running.

9. You can deactivate the virtual environment by using the command

     >deactivate

# Sub tasks of the application
1. http://localhost:5000/ prints a simple Hello world.

2. http://localhost:5000/authors gives a list of authors and number of posts using the json at                                              https://jsonplaceholder.typicode.com/users
   and https://jsonplaceholder.typicode.com/posts
   
3. http://localhost:5000/setcookie sets two cookies:
   name= your-first-name and age= your-age.
   
4. http://localhost:5000/getcookies displays the set key value pairs

5. Request to http://localhost:5000/robots.txt is denied

6. http://localhost:5000/html displays an HTML page

7. There is a text box at http://localhost:5000/input which sends the entered data as post to the endpoint /output

8.  http://localhost:5000/output logs the received data from textbox to stdout
    
    

   
