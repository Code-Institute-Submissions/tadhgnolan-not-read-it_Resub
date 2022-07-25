# Not Read It
## by Tadhg Nolan

[Live Site](https://not-read-it.herokuapp.com/)

[Wireframe](static/not-read-it_wireframe.pdf)
# Table of Contents
1. [Intro](#intro)
2. [Technologies](#technologies)
3. [Testing](#testing)
4. [Credits](#credits)
5. [Deployment](deployment)

## Intro

 - Not Read It is a socail media website similar to Reddit.  

### Design

[Entity Relationship Diagram (ERD)](static/pp4_erd.drawio.png)

### User Stories

- View post list: As a Site User I can view a list of posts so that I can select one to read.
- Open a post: As a Site User I can click on a post so that I can read the full text.
- View likes: As a Site User / Admin I can view the number of likes on each post so that I can see which is the most popular or viral.
- View comments: As a Site User / Admin I can view comments on an individual post so that I can read the conversation.
- Account registration: As a Site User I can register an account so that I can comment and like.
- Comment on a post: As a Site User I can leave comments on a post so that I can be involved in the conversation.
- Like / Unlike: As a Site User I can like or unlike a post so that I can interact with the content.
- Manage posts: As a Site User / Admin I can create, read, update and delete posts so that I can manage my blog content.
- Select Category: As a Site User / Admin I can select a topic category when creating a post.
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
- [Django-AllAuth](https://django-allauth.readthedocs.io/en/latest/)
## Features 

### Existing Features

### Features Left to Implement

## Testing

### Manual testing

- Manually testing each each path.  										

### Validator Testing 

### Unfixed Bugs


### Using Heroku

- Create an account and login to [Heroku](https://id.heroku.com/login)
- Create a new app, with an appropriate app name and choose a region.
- In Resources add Heroku Postgres.
- Within your newly created app go to settings and click Config Vars. Use the DATABASE_URL Value and add it to your env.py file also you need to connect it via settings.py.
- Create a SECRET_KEY Key and the Value as the desired key.
- Then go to the Deploy tab next to Deployment Method, click GitHub to connect your account and repository.
- At the bottom of the page hit deploy branch making sure it is set to main.
- Also "Enable Automatic Deploys" can be clicked to keep the app up to date with your Github repository.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.
   
   

## Credits 

 - A social media site designed by Tadhg Nolan
 
### Content 

- [Django Blog](https://github.com/Code-Institute-Solutions/Django3blog/tree/master/12_final_deployment)
- Used  and modified code from this Github repository.
- [Stackoverflow](https://stackoverflow.com/questions/6045021/django-forms-getting-a-select-box-from-a-different-model)
- used and modified code from this webpage.