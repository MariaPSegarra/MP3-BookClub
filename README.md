# 3rd Milestone project - Data Centric - Book Club 4Readers

For this 3rd milestone project I'm creating an app with Flask based on a Book Club concept.
Every user can register a profile. When the user logs in can read all user's posts, can add new books and can edit and update his own data entries. 
The logged in user won't be able to manipulate data that it's not his own. He'll also be able to post comments that all users with a profile can read.
Only the user Admin who can manage the Genres.
Visitors can read all book content. They won't be able to comment or create any content unless they register in the system.
Visitors and all users can contact the admin user via contact page.

## Motivation for the project

The idea is based on one of the suggestions the course made. It was originally a book store but I thought it'd be a more interesting app if I implemented some interaction with the user. So the idea of the Book Club was born.

I encountered many problems following the old course videos for this Data Centric Module. I wasted a lot of time trying to work out the videos based on Cloud9, while I've been using Gitpod (as per course instructions).
I finally got access to the new videos and I was able to follow the instructions to connect to MongoDB and deploy to Heroku without any problems. 

## Techonologies 

- Gitpod 
Development environment
- HTML5
- CSS
- [Materializecss](https://materializecss.com/)
- [FontAwesome v5.15](https://fontawesome.com/)
- Javascript
- Jquery
- Python
- Jinja
- [Emailjs API](https://www.emailjs.com/)
For the contact form
- [Github](https://github.com/MariaPSegarra/MP3-BookClub) 

The Flask app is connected to the MONGODB noSQL and deployed on [Heroku](https://book-readers-mp3.herokuapp.com/)

### Resources

- [W3schools](https://www.w3schools.com/)
Code Library. General Knowledge.
- [StackOverflow](https://stackoverflow.com/)
Answers to questions and code examples provided by experienced coders.
- [Videos]
New videos for the Data Centric Module were available recently.


## Data Model

I created a Data Base in MongoDB named book_library.
There are four main entities: Books, users, genres and comments. Each with their own attributes.
I created a diagram with the relationship between entities so I could structure the functions of the app around them.

![Entities](/images/entities.jpg)
![Attributes](/images/attributes.jpg)

## Features

Features and access for different users:

[Navigation]
For all users:
- Homepage
Where all books entered by all users are displayed. A search function is also available.
- contact
All users and visitors can contact the Admin user via emailjs function.
- log in
- register

For logged in users
- log out
- Add new book
- Profile page
where the app lands once the user logs in. It displays a welcome message and basic buttons to navigate.

For admin user
- Manage genres

[Homepage]
All users can search and read content.
Logged in users can also update and delete their own data entries.
Also, they can post comments for other logged in user to read.

[Footer]
Displays copyright information and Social media links. (not active at the moment as no social media pages were created for this project)

### Features left to implement

[Pagination] was a feature I wish I had time to implement. I got hands on pagination code from my mentor but i kept getting a system error:
*pymongo.errors.InvalidOperation: cannot set options after executing query*
I didn't have time to fix this error so I moved on.
Also the materialize pagination feature didn't seem suitable what the type of pagination that I needed.  

## Testing

All CRUD funstions in the app work well.
All user funtions to register, log in and log out work well.
The app is responsive in all screen sizes.

The contact form works at this time. It sends the message via Emailjs API.

[Comments]
I do have a problem with the comments that due to time restrictions I won't have time to solve before handing in the project.
Even though comments are properly created in MongoDB and to my understanding of python at this time the route and function on the app.py file 
and the html and jinja seem correct, I wasn't able to display the comments on the homepage.

## Deployment

I've used Gitpod for the development stage.
The app is deployed on [Heroku](https://book-readers-mp3.herokuapp.com/) following instructions from the new Data Centric Module videos.

## Credits

All [content] and [images] come from wikipedia pages.

