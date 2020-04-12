# Movie-Web-App
This is a movie web application using Django REST Framework.

Where a user can signup/login to create movie database through browsable REST API. 
- Users can edit and delete their own entry only, in database.
- Movie data can be seen (but cannot be edited) by anyone. (without even signup/login).

## Follow these steps to run the project locally.

- Install python
    ```bash
      sudo apt-get install python3.6
    ```
- Install virtual environment
    ```bash
      sudo apt-get install virtualenv
    ```
- Clone the Demo-Movie-App
    ```bash
      git clone https://github.com/Harirai/Demo-Movie-App.git
    ```
- Change the directory to Movie-Web-App
    ```bash
      cd Movie-Web-App
    ```
- Activate the virtual env
    ```bash
      source myenv/bin/activate
    ```
- Change the directory to movieapp
    ```bash
      cd movieapp
    ```
- Run following commands to add fields to db.sqlite3
    ```bash
      python manage.py makemigrations
      python manage.py migrate
    ```
- Run the website 
    ```bash
      python manage.py runserver
    ```  
- Check that the project is running correctly by browsing to
    ```
      http://127.0.0.1:8000
    ```
 

<h2>Author</h2>
<blockquote>
  Harirai Mahajan<br>
</blockquote>
<a href='https://github.com/Harirai'> @Harirai </a>



 
