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

- Repeated real world testing performed with Google Pixel 3aXL (2160 × 1080px), Nokia 3 (720 x 1280), Asus Nexus 7 (1920 x 1200px) & Desktop PC (1920 x 1080px + 2560 × 1440) representing a mixture of age plus hardware capability & were readily available.

### In Chrome Dev Tools, tested repeatedly with all available presets

This functionality testing involved:

- Verifying all navbar & other links functioned as expected.

- Using Chrome Dev Tools Elements tab to test out small styling changes before adding.

- Checking that fonts scaled correctly for each display size.

- Checking for overflow.

- Tested html & CSS at https://validator.w3.org.

### Validator Testing 

Used [PEP8 online](http://pep8online.com/) code checker to correct any errors in my code. 

### Unfixed Bugs


## Deployment 

- The site was deployed via Heroku. The steps to deploy are as follows: 
  
  -  Enter following command in terminal: 'Pip3 freeze > requirements.txt'.
  - From Heroku Dashboard: Create new app. Select region. Go to settings tab => add buildpacks for Python and NodeJS. Make sure Python is on top and NodeJS beneath.
  - Go to deploy section and select Github.
  - Search for repository name => click connect => click automatic or manual deploy.
  
- To clone to a local machine follow these steps:
  
  - On GitHub, navigate to the main page of the repository.
  - Above the list of files, click download Code.
  - To clone the repository using HTTPS, under "Clone with HTTPS", click the clipboard icon.
  - Open Git Bash.
  - Change the current working directory to the location where you want the cloned directory.
  - Type git clone, and then paste the URL you copied earlier.
    `$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY`
  - Press Enter to create your local clone. 
  	`$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY`
    ``> Cloning into `Spoon-Knife`...``
    `> remote: Counting objects: 10, done.`
    `> remote: Compressing objects: 100% (8/8), done.`
    `> remove: Total 10 (delta 1), reused 10 (delta 1)`
    `> Unpacking objects: 100% (10/10), done.`
   
   

## Credits 

 - A social media site designed by Tadhg Nolan
 
### Content 

- [Django Blog](https://github.com/Code-Institute-Solutions/Django3blog/tree/master/12_final_deployment)
- Used  and modified code from this Github repository.

### Special Thanks

- Cormac Nolan - Feedback and advice.
- Tim Nelson - Mentor.