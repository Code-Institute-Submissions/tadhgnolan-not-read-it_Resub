# Not Read It
## by Tadhg Nolan

[Live Site]()

# Table of Contents
1. [Intro](#intro)
2. [Technologies](#technologies)
3. [Testing](#testing)
4. [Credits](#credits)
5. [Deployment](deployment)

## Intro

 - Not Read It is a socail media website similar to Reddit.  

### Design



### User Stories

- View post list: As a Site User I can view a list of posts so that I can select one to read.
- Open a post: As a Site User I can click on a post so that I can read the full text.
- View likes: As a Site User / Admin I can view the number of likes on each post so that I can see which is the most popular or viral.
- View comments: As a Site User / Admin I can view comments on an individual post so that I can read the conversation.
- Account registration: As a Site User I can register an account so that I can comment and like.
- Comment on a post: As a Site User I can leave comments on a post so that I can be involved in the conversation.
- Like / Unlike: As a Site User I can like or unlike a post so that I can interact with the content.
- Manage posts: As a Site User / Admin I can create, read, update and delete posts so that I can manage my blog content.
- Select Catagory: As a Site User / Admin I can select a topic catagory when creating a post.
- Create drafts: As a Site Admin I can create draft posts so that I can finish writing the content later.
- Approve comments: As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments.

## Technologies

### Languages

- [Python](https://www.python.org/about/)

### Other Technologies and Libraries 

- [GitHub](https://github.com/)
- [GitPod](https://www.gitpod.io/about/)
- [Heroku](https://heroku.com)
- [Django](https://www.djangoproject.com/)

## Features 

### Existing Features

Registration Page - allows new users to register an account with username and password.

Login page - registered user can login.

Home page - usersers can view list of posts. 

Add post - registered users can add new posts, enter a title and select a category from a drop down menu.

Update post - registered users can update their existing posts.

Delete post - registered users can delete their existing posts

Admin functionality - admins can update and delete categories

### Features Left to Implement

Like / Unlike

View Likes

Comment on a Post

Approve Comments

## Testing

### Manual testing

- Manually testing each each path. 

---
**Manual Test of post paths**

---
![Manual Test Image](static/Documentation/Testing/images/Manual_test_post.gif)

---
- ### Repeated real world testing performed with:
---
### **Google Pixel 3aXL (2160 × 1080px)**
---  
![Pixel 3aXL Image 1](static/Documentation/Testing/images/Pixel_3a_1.png)
![Pixel 3aXL Image 2](static/Documentation/Testing/images/Pixel_3a_2.png)

---
### **Nokia 3 (720 x 1280)**
---
![Nokia 3 Image 1](static/Documentation/Testing/images/Nokia_3_1.jpg)
![Nokia 3 Image 2](static/Documentation/Testing/images/Nokia_3_2.jpg)

---
### **Lenovo Ideapad Duet Chromebook (1080 x 1200px)**
---
**Laptop mode**

![Chromebook Laptop Mode Image 1](static/Documentation/Testing/images/chromebook_1.png)
![Chromebook Laptop Mode Image 2](static/Documentation/Testing/images/chromebook_2.png)

**Tablet mode**

![Chromebook Tablet Mode Image 1](static/Documentation/Testing/images/chromebook_3.png)
![Chromebook Tablet Mode Image 2](static/Documentation/Testing/images/chromebook_4.png)

---
### **Desktop PC (1920 x 1080px + 2560 × 1440) representing a mixture of age plus hardware capability & were readily available.**
---

**1920 x 1080px**

![1920 x 1080px Image 1](static/Documentation/Testing/images/Desktop_1920_1.png)
![1920 x 1080px Image 2](static/Documentation/Testing/images/Desktop_1920_2.png)

---

**2560 x 1440px**

![2560 x 1440px Image 1](static/Documentation/Testing/images/Desktop_1440_1.png)
![2560 x 1440px Image 2](static/Documentation/Testing/images/Desktop_1440_2.png)

---

### In Chrome Dev Tools, tested repeatedly with all available presets

This functionality testing involved:

- Verifying all navbar & other links functioned as expected.

---
**iPhone X**

---
![iPhone X Image](static/Documentation/Testing/images/iPhone_X.gif)

---
**Samsung Galaxy S20 Ultra**

---
![Samsung Galaxy S20 Ultra Image](static/Documentation/Testing/images/Samsung_Galaxy_S20_Ultra.gif)

---
**iPhone 6/7/8**

---
![iPhone 6/7/8 Image](static/Documentation/Testing/images/iPhone_6_7_8.gif)

---

- Using Chrome Dev Tools Elements tab to test out small styling changes before adding.

- Checking that fonts scaled correctly for each display size.

- Checking for overflow.

- Tested html & CSS at https://validator.w3.org.

### Validator Testing 

Used [PEP8 online](http://pep8online.com/) code checker to correct any errors in my code. 

### Unfixed Bugs


The live deployed application can be found at [not read it](https://not-read-it.herokuapp.com/).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select *New* in the top-right corner of your Heroku Dashboard, and select *Create new app* from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select *Create App*.
- From the new app *Settings*, click *Reveal Config Vars*, and set the following key/value pairs:
  - `DATABASE_URL` (this comes from the **Resources** tab, you can get your own Postgres Database using the Free Hobby Tier)
  - `SECRET_KEY` (this can be any random secret key)

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's requirements (where applicable) using: `pip3 install -r requirements.txt`. If you have your own packages that have been installed, then the requirements file needs updated using: `pip3 freeze --local > requirements.txt`

The Procfile can be created with the following command: `echo web: gunicorn notreadit.wsgi > Procfile`

For Heroku deployment, follow these steps to connect your GitHub repository to the newly created app:

Either:
- Select "Automatic Deployment" from the Heroku app.

Or:
- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a <app_name>` (replace app_name with your app, without the angle-brackets)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type: `git push heroku main`

The frontend terminal should now be connected and deployed to Heroku.

### Local Deployment

*Gitpod* IDE was used to write the code for this project.

To make a local copy of this repository, you can clone the project by typing the follow into your IDE terminal:
- `git clone https://github.com/tadhgnolan/not-read-it.git`

You can install this project's requirements (where applicable) using: `pip3 install -r requirements.txt`.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/tadhgnolan/not-read-it)

Additionally, you'll need to create your own `env.py` file with the following keys:

- `SECRET_KEY` (can be any secret value)
- `DATABASE_URL` (this comes from the "Resources" tab on your Heroku app)
   
   

## Credits 

 - A social media site designed by Tadhg Nolan
 
### Content 

- [Django Blog](https://github.com/Code-Institute-Solutions/Django3blog/tree/master/12_final_deployment)
- Used  and modified code from this Github repository.

### Special Thanks

- Cormac Nolan - Feedback and advice.
- Tim Nelson - Mentor.