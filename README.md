# SB-basic-Blog
#As you can see that the app is so small and simple, since i focused mainly on working with database so there is not much images #or effect of HTML and CSS.
To run the app, follow these steps:
-clone the app
-open CMD(only for windows) and move into the path of directory containting files cloned.
-run commands: python manage.py makemigrations (if you're activating virtualenv, type: py -number_of_python_version manage.py runserver e.g: if you using python 3 then type: py -3 manage.py runserver) 
-run command: python manage.py migrate
-run command: python manage.py runserver (if you're activating virtualenv, type: py -number_of_python_version manage.py runserver e.g: if you using python 3 then type: py -3 manage.py runserver) 
-paste url: http://127.0.0.1:8000/ into browser to access the website
-You'll see that there is almost nothing in the index page, that's because you didn't put anything in database so the page has no data to show. Deactivate the server by pressing ctrl+break on CMD. 
-Now run command: python manage.py createsuperuser. Use that account to access admin site with url: http://127.0.0.1:8000/admin so you can create data to be displayed.
-Rerun commands: python manage.py runserver and access the website
