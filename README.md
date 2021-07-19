README MS3

# Milestone Project 3 – Sweet Tooth
My third milestone project is for a dessert recipe website. It contains a homepage, recipe page, register page, log in, account page, a page to upload a user’s own recipes and a manage categories page for the admin only. This is a full stack website using HTML, CSS, Python, Flask and MongoDB. The aim of the website is for users to be able to browse dessert recipes and upload, amend and/or delete their own recipes. 
[Sweet Tooth](http://sweet-tooth-ms3.herokuapp.com/index)
##UX
The website is for people with a sweet tooth, those who enjoy desserts and who are also looking to make their own desserts or those who wish to share their own recipes with others. Users can simply browse through the recipe collection or add their own by creating an account for the website and uploading them. 
###User Stories
As a user – 
•	I want to be able to search for recipes
•	I want to see a variety of dessert recipes 
•	I want to be able to navigate the website easily
•	I want an attractive layout and colours for the website
•	I want to be able to see images of the desserts and ingredients/methods to make these, in further detail 
•	I want to be able to register an account for myself 
•	I want to be able to upload and amend recipes of my own
•	I want to be able to delete recipes I have uploaded
•	I want to be able to easily access recipes I have previously uploaded
•	I want to be able to log back into my account once I have registered
•	I want social media links for the website so I can follow them

As an admin – 
•	I want to be able to add categories
•	I want to be able to edit categories
•	I want to be able to delete categories



###Wireframes
I used the Balsamiq programme to create my wireframes for the website. These wireframes enabled me to have a foundation of which to build the final website from and give me an idea of what I should be aiming for. It also allowed me to discuss design with my mentor before building the site. 
For the wireframes, I used the Balsamiq programme to create these. These wireframes allowed me to have a foundation on which to build my final website from and also gave me an idea of what I should be aiming for in creating this website. It also allowed me to plan my design with my mentor before starting my project. However, it should be noted that the admin manage categories page was added to a later point in the project and so wireframes had not been made for this feature.
Desktop Wireframes (add wireframe)
Tablet Wireframes (add wireframes)
Mobile Wireframes (add wireframe)

### Design
The design of the website, I aimed to go for a fun, playful design that emulated something similar to an ice cream/dessert parlour. Having looked at other dessert websites online, I felt this was best for my project as other themes didn’t project the look that I had in mind. 
### Font
I used Google Fonts for the fonts that have been used on the website. From here, Sacramento and Montserrat were the finalise fonts used. Sacramento was used mainly for headings and titles while Montserrat was used more for regular text such as for ingredients lists on the website. These two fonts were paired using Google Font’s suggested pairings. 
### Colors
For basic colours, I used a variety of blues and grays. I felt that having the images of colourful desserts against these backgrounds/colour would make the desserts pop out more on the page rather than the focus being on the colours of the website. The original idea for colours was to use the background image colours as a basis to work from. The dark blue used for headings and flash messages is rgb(6, 8, 143), while the light blue used is #84fffa. The light blue has been used for non-heading texts and as borders around the images.


##Features
### Existing Features
### Homepage
The homepage is the first webpage that the user sees when they access the website. The homepage contains a navigation bar, footer, h1, hero image and an image carousel that highlights just some of the possible things a user can make if using a dessert recipe. 
### Navbar
The nav bar contains links to other parts of the website, however if a user has not logged in, the only available navigational links to them are “Home”, “Recipes”, “Register” and “Log In” (this changes to “Home, “Recipes”, “Account” and “Log Out” once a user has logged in via the Log In page). If an admin logged in, they are also able to see the “Manage Categories” link on the navbar. The navbar collapses into a hamburger menu on the mobile viewport, with a list of the links that are available. 
### Carousel 
The carousel has images of desserts, some of which their recipes are on the website to make. The carousel is to draw in users and to attract them to the desserts. The idea behind this is, if they are tempted by the desserts in the carousel, they will perhaps be more likely to want to make a dessert in order to eat it. 
### Footer
The footer contains icons that link to social media, which a user can follow. However, the links just lead to the social media’s homepages as the website doesn’t have any social media links. 
### Recipes Page
Below the h1 for the recipes page, there is a search bar with a reset and search button. The search bar allows users to search for recipes by key names and key ingredients. The option to also reset a search is available via the ‘reset’ button. If no recipe is found, a “No recipe found” message will appear on the page. 
Below the search bar, the next section contains images of the desserts and their names on the image. When the image is hovered over, a description of the dessert appears as does a link for the full recipe. Users can click this link to view the ingredients, method and a larger picture of the dessert. 
### Register Page
This page allows the user to create an account for the website to allow them to upload, amend and/or delete recipes of their own. If the user already has an account, there is a link just under the registration section to log in instead. 
### Log In Page
This page is very similar to the Register page, although instead of registering, the user can log into their account. However, like the Register page, if a user doesn’t have an account there is a link just under the log in section that directs the user to the Registration page.  
### Account page
The Account page is what first appears when a user has logged to their account. On this page, a user can view previous recipes they have uploaded or they can upload new recipes via the “Upload” link, which directs them to the Upload page. Desserts are displayed in a similar way to the recipes page, and when hovered over, three links appear – Full recipe, edit and delete, allowing the user to amend their uploaded recipe. The layout of this page differs from the wireframe. This is because, when discussing my wireframes with my mentor, he advised to avoid whitespace and so the recipes layout was amended. 
### Upload Page
This page is where users can create a new recipe by filling in the relevant fields to their recipe. A user can add the recipe to a certain collection type and fill in the name, ingredients and methods of creating the dessert on the page. There is also the option to add an image url if the user likes. The other fields have to be filled in order to upload a recipe, whereas the image url can be left blank. Once a recipe has been uploaded, the user can then view, edit and delete recipes from the their account on the ‘Account’ Page. 
### Manage Categories

### Features Left to Implement
I would like to implement a page where the desserts or the dessert ingredients can be bought from, by just browsing one page instead of having to search the internet for them. 
A ‘favourites’ system would also be considered for future features, allowing users to save their favourite recipes to access them quickly via a ‘Favourites’ page. 
## Technologies Used
- [HTML](https://en.wikipedia.org/wiki/HTML) To enable the basic building on the website.
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) for styling the website 
- [JavaScript] (https://www.javascript.com/) for the interactivity  
- [MaterializeCSS](add link)
- [GitHub](https://github.com/) Where I can have my repository saved for my project. 
- [Gitpod](https://www.gitpod.io/) My preferred IDE for building the website.
- [GIT](https://git-scm.com/) for version control.
- [Google Fonts](https://fonts.google.com/)   to choose and use different fonts for the website.
- [Font Awesome](https://fontawesome.com/)   For different icon elements used.
- [jQuery](https://jquery.com/) and [Popper.js](https://popper.js.org/) To use alongside Bootstrap.
- [Python](link site)
- [Flask](link site)
Flask-pyMongo
- [MongoDB](link site)
jinja
[Imgur](imgur.com)
Heroku 
Random key generator

## Testing
Testing information can be found at TESTING.md 

## Deployment
### Deployment
The project was deployed by using Heroku, however it is not a matter of simply deploying the website. A few prerequisites are needed in order to deploy. Deploying and the pre-deploying steps are as follows – 
- open Gitpod and in the terminal write pip3 freeze –local > requirements.txt and echo web: python run.py > ProcFile 
- The ProcFile needs to contain the following line without any additional blank lines after it web: python app.py
- Push this to your repository
- create a .gitignore file in your repository if you don’t already have oe and add env.py and __pycache__ to the .gitignore. 
- save the file – this is so no sensitive information is added to the repository by mistake. 
- create an env.py file and add the below information to it – 
--- 
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", " *YOUR SECRET KEY*")
os.environ.setdefault("MONGO_URI", " *YOUR MONGO_URI * ")
os.environ.setdefault("MONGO_DB", " *YOUR MONGO_DBNAME* ")

- login to Heroku
- Select “Create New App” in the top right corner of the browser
- Create an app name and select the region closest to your location, then click “Create App”.  
- From there, go to the ‘Deploy’ tab and then “Deployment Method”, and select ‘GitHub’. 
- Find your GitHub Repository by name and click ‘connect’. However, do NOT enable automatic deployment at this stage (as errors can occur). 
- From the ‘Settings’ Tab, click ‘Config Vars’ and then ‘Reveal Config Vars’. 
- Enter the key value pairs from the env.py, (table shown above). 
-  Go back to the ‘Deploy’ Tab and then click “Enable Automatic Deployment”. 
- In “Manual Deploy”, choose the branch you want to deploy from (ie ‘master/main’). 
- Click “Deploy Brance” and let Heroku build the app (this may take a few minutes). 
- When the app has been built, click on “Open App” at the top of the page to view your website. 
### Forking a Repository 
In order to fork a repository from GitHub, do the following steps – 
- Login/sign up to GitHub
- Find the repository you wish to fork 
- In the top right corner, click the ‘Fork’ button. This will now save a copy to your GitHub. 
### Making a Local Clone 
In order to make a local clone of a repository, follow the steps below – 
- Login/sign up GitHub and locate the repository. 
- Click the  ‘Code’ button, which is just above the listed files. 
- Click the icon button to copy the link of the repository. 
- Open Git Bach and change the current working directory to the location of where you want the cloned directory to go. 
- Type git clone and paste the URL
- Press enter and the clone will be created
Note – you will need to create an env.py file with your own values and a MongoDB database as previously shown. You will also need to install the project requirements, 



## Credits
### Images
[Chocolate-cake](https://unsplash.com/photos/CiyS558EdQ8)
[Ice Cream](https://unsplash.com/photos/idTwDKt2j2o)
[Brownies](https://unsplash.com/photos/TIctev58ij8)
[Chocolate trifle](https://unsplash.com/photos/cLpdEA23Z44)
[Pancakes](https://unsplash.com/photos/6AGlB0wKueg)
[Cupcakes](https://unsplash.com/photos/V4MBq8kue3U)
[Tiered cake](https://unsplash.com/photos/pZZJwwNPy2k)
[Cupcakes](https://unsplash.com/photos/nXKWLn8y9qE)
[Chocolate cake](https://unsplash.com/photos/-4ccYKuvc5A)
### Content 
The dessert recipes and images were taken from the [BBC Good Food]( https://www.bbcgoodfood.com/) website by typing in the name of the desserts or simply searching for ‘desserts’. 
### Code
[HTML for recipes page](https://github.com/AmyOShea/MS3-Cocktail-Hour/blob/master/templates/recipes.html)
[HTML for categories page]](https://github.com/AmyOShea/MS3-Cocktail-Hour/blob/master/templates/all_collections.html)
[CSS for recipe and categories page](https://github.com/AmyOShea/MS3-Cocktail-Hour/blob/master/static/css/style.css)


### Acknowledgements
I would like to thank my mentor, Precious Ijege, for his time, advise and comments in working with me to build my project. I would like to thank the Code Institute Slack forum for all their help and in particular the #peer-review-code channel for the input for my project. I would also like to thank the tutors at Code Institute for their valuable advice. 
## Disclaimer
The content and images on this website are for educational purposes only.

