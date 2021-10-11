# DjangoGram

DjangoGram, is a project created by Aden Lehman, Andrew Watkins, Kevin Newson, and Billy Yip as a Instagram clone as our final project at Kenzie Academy. The goal of this project is to allow a user to do the following:

- Create an account
- Log in via created account
- Make a post with an image
- Comment on own post or other's posts
- Delete your own post
- Delete your own comments or any comments that is made in your posts
- Like a post
- Unlike a post
- Display total like(s) for a post
- Check out your own or another user's profile page
- Make edits to your own profile page (bio & e-mail)

## Installation

Run in the venv

```
poetry install
```

Now we need to go into our venv:

```
poetry shell
```

Next we will need to install dotenv and Pillow.

dotenv allows you to run the secret key that has now been hidden.

```
pip install python-dotenv
```

You will need to create your own .env file and pass in the following:

```
SECRET_KEY= (Ask a team member for the secret key!)
```

Next install Pillow, this will allow you to see and upload the photos and is required to run the project.

```
python -m pip install Pillow
```

Again be sure to be in the venv.
Now try running the server via:

```
python manage.py runserver
```

## Insert Photos of Sample
