# downup test

## Requirements:

- Register and log-in using a username and password
- Upload files, allowing the user to select whether the file is ‘public’, or ‘private’
- View a list of the users previously uploaded files, and files uploaded as ‘public’, including upload time/date, 
and a link to the original upload
- Provide an API endpoint that allows a valid user to search by filename over any files they have permission to see, 
returning paths that can be used to download matching files

## Instructions:

To install dependencies and activate virtual environment:
```
pip install pipenv

pipenv install
pipenv shell
```

Create migrations
```
python downup/manage.py makemigrations
```
Apply migrations

```
python downup/manage.py migrate
```
To run a development server:
```
python downup/manage.py runserver
```

 
To access the endpoint mentioned at point 4:
`http://127.0.0.1:8000/<file name>`  
