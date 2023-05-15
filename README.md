# mgs406_project

This creates a website for a restaraunt.
The home page has a header and three buttons to create a reservation, view the menu, and a managers page. There are three pages because I misread the requirements and felt it would be easier to add on to the code rather than delete things. 

  The menu is a table pulled from sql, there is also a button which brings you back to the home page.
  
  The reservation page is a form, is uses a script for the date which gives you a calender to pull from, similarly there is a popper script for the number of people in your party. 
    All scripts are credited in the code.
  Once you submit the form you are redirected to a confirmation page which displays the values you entered, there is also an option to return to the home page. 
    
  The managers page is a list of the reservations, the table is based in sql and updates whenever soemone fills out the form, there is also a home button there as well. 
  
  


app.py runs on gunicorn, manage.py and managers.py only run on the 5000 localhost server
