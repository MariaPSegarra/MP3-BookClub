# 3rd Milestone project - Data Centric - Book Club 4Readers

For this 3rd milestone project I'm creating an app with Flask based on a Book Club concept.
Every user can register a profile. When the user logs in can read all user's posts, can add new books and can edit and update his own data entries. 
The logged in user won't be able to manipulate data that it's not his own. He'll also be able to post comments that all users with a profile can read.
Only the user Admin who can manage the Genres.
Visitor's can read all book content. They won't be able to comment or create any content unless they register in the system.
Visitor's and all users can contact the admin user via contact page.

## Motivation for the project

The idea is based on one of the suggestions the course made. It was originally a book store but I thought it'd be a more interesting app if I implemented some interaction with the user. So the idea of the Book Club was born.

I encountered many problems following the old course videos for this Data Centric Module. I wasted a lot of time trying to work out the videos based on Cloud9, while I've been using Gitpod (as per course instructions).
I finally got access to the new videos and I was able to follow the isntruction to connect to MongoDB and Heroku without any problems. 

## Techonologies 

- HTML5
- CSS
- Javascript
- Jquery
- Python
- 

The Flask app is connected to the MONGODB noSQL and deployed on Heroku.

## Data Model

I created a Data Base in MongoDB named book_library.
There are four main entities: Books, users, genres and comments. Each with their own attributes.
I created a diagram with the relationship between entities so I could structure the functions of the app around them.

![Entities](/images/entities.jpg)
![Attributes](/images/attributes.jpg)




