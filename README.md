# mgs406_project

This creates a website for a restaraunt.
The home page has a header and two buttons for a menu and to create a reservation.

  The menu is a table pulled from sql, there is also a button which brings you back to the home page.
  The reservation page is a form, is uses a script for the date which gives you a calender to pull from, similarly there is a popper script for the number of people in your party. 
  All scripts are credited in the code.
  
Once you submit the form you are redirected to a confirmation page which displays the values you entered, there is also an option to return to the home page. 

app.py runs on gunicorn, manage.py only runs on the 5000 localhost server
