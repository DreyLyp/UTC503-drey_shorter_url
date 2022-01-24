
# Drey_shorter_url

## Description
This program will allow you to locally host your own url shortener using Django


## Authors

- [@Drey](https://www.github.com/DreyLyp)


## Installation

Download git repository and install requirements :

```bash
  git clone https://github.com/DreyLyp/UTC503-drey_shorter_url.git
  cd UTC503-drey_shorter_url
  sudo pip3 install -r requirements.txt
```


    
## Deployment

After this, you can now start ther server :

```bash
  cd drey_short_url/
  python3 manage.py runserver
```

The server will start on our localhost at port 8000, so put http://127.0.0.1:8000/ on your navigator.


## Usage

    1) put your link (ex : https://google.com) in the section 
    2) click on the "transform" button.
    3) copy the new link and put this on your navigator

If you want to view all the link that you created you can access at the admin page.
For that, you have a link at the index.html, or you can juste access with http://127.0.0.1:8000/admin/

ID for admin page :

    username : drey
    password : admin


## Information

In this folder you will find two other folders.

-drey_short_url : it's the main folder for Django server, so it was created by Django with some little modification

-drey_shorter : it's the folder for my app Djago, in this file you will be able to see all that I have been able to do


## For the future

To improve this url reducer, I think it would be good to add a feature that checks if a long link is already present in the database in order to avoid creating a new idd for the same long link.