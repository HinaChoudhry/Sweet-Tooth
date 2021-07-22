# Testing

## Code Validation
- [W3C Mark-up Validation](https://validator.w3.org/) was used for checking for validity and to ensure there were no errors in the html code. While there were no actual errors in the code, due to the Jinja used, the validator was showing some different errors. 
- [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) was used for checking errors in the CSS. There are [no errors](https://github.com/HinaChoudhry/Sweet-Tooth/blob/master/static/images/validation/css.png) in the CSS file.
- [JSHint](https://jshint.com/) was used to check for validity of the JavaScript, and the outcome of the validator is [here](https://github.com/HinaChoudhry/Sweet-Tooth/blob/master/static/images/validation/js.png)
- [Pep8 Online](http://pep8online.com/) was used to check for errors in Python, [no errors](https://github.com/HinaChoudhry/Sweet-Tooth/blob/master/static/images/validation/pythonvalidation.jpg) were found.

## User Story Tests

As a user 
-	I want to be able to search for recipes 
	* There is a search bar on the recipes page which allows users to search recipes by name and ingredients. 

-	I want to see a variety of dessert recipes  
	* 12 initial desserts were added the to the original database for the user to browse. This number will likely grow as users add their own recipes to the website. 

-	I want to be able to navigate the website easily
	* The website has a navbar at the top of each page with links to navigate the website. These links are clearly named and easily accessible from all pages on the website. The navbar is also available in a dropdown menu on smaller viewports for easy navigation. 

-	I want an attractive layout and colours for the website
	* The layout and design has been created to attract users and to make them want to upload their own recipes. As mentioned before, the background colors were chosen as such in order to make the dessert images pop out, rather than detract from the main features. 

-	I want to be able to see images of the desserts and ingredients/methods to make these, in further detail 
	* The recipes page contains photos of the desserts. These can then be hovered over for a further description of the desserts and a “Full Recipe” link allows the user to look at the full recipe of the dessert, including the ingredients, method and a larger image of the dessert clicked. 
-	I want to be able to register an account for myself 
	* Users are able to register for an account with a password and username. This account is then accessible again to the user, after logging out. 
-	I want to be able to upload and amend recipes of my own
	 * Users can upload their own recipes via the ‘Upload’ page with details such as ingredients, method and even an image url. Once a recipe has been uploaded, users are able to view them on their account page and are able to edit a recipe as desired. 
-	I want to be able to delete recipes I have uploaded
	* Users can delete their own recipes via the account page, which permanently deletes the recipe. 
-	I want to be able to easily access recipes I have previously uploaded
	* Each user’s uploaded recipes are accessible on the ‘Account’ page. However, users can only access their own recipes on the account page, whereas they can view all recipes from all users and the original database via the ‘Recipes’ page.
-	I want to be able to log back into my account once I have registered
	* Users are remembered an are able to log back into their accounts. 
-	I want social media links for the website so I can follow them
	* The footer contains social media links, which are accessible via the social media icons. 
As an admin – 
-	I want to be able to add categories
	* The admin is able to add new categories to the recipe website, via the “Manage Categories” page, via the “Add Category” button, which redirects the admin to an upload page, similar to the upload page for recipes. 
-	I want to be able to edit categories
	* Categories are editable to the admin only, again accessible from the ‘Manage Categories’ Page. 
-	I want to be able to delete categories
	* The admin is able to delete categories, again from the ‘Manage Categories’ page. Once the admin choses to delete a category, it is permanently deleted. 

# Responsiveness

## Index.html

### Desktop

In the desktop view, there is the navbar, h1, hero image and a carousel. The navbar is stretched across the top of the page with links being visible on the right side for the user to navigate their way through the website. The navbar is visible on every page of the website, with different links being shown depending on if a user is logged in or out, or is the admin. The h1 spans part of the width of the desktop view, with the hero image doing the same. The text understand is wider than the hero image and under this there is a carousel of dessert images to attract the user. The footer at the bottom of the page, spans the width of the page with social media link icons being shown in the center of the footer. 

### Tablet 

The tablet viewport is similar to the desktop, with navbar being at the top of the page, however instead of links being on the right there is side nav that opens up when clicked on. The h1 and hero text fit the viewport with the use of the 'responsive-img' class for the image. The text below appears in more lines and the carousel has again shrunk down to fit the viewport. The footer still spans the width of the viewport, and the social media links are in presented in a row. 

### Mobile

The navbar now has the name of the website in the middle of the navbar instead of positioned to the left, and the sidebar is still visible instead of the actual links being displayed. When the sidebar is clicked, the links then appear to the user in a column. The hero image fits the mobile viewport, using the 'responsive-img' class and the h1 is still the main text. The text underneath the hero image has followed the viewport and is now smaller to fit the mobile screen. The carousel and images again are responsive in that they too fit the mobile viewport and don't go beyond that. 

## Recipes

### Desktop

Here there is a search bar which spans almost all of the width of the viewport, with the reset and search buttons being displayed next to each other. On the recipes page, there are images of desserts that are displayed. On the desktop viewport, the images are columns of 4 due to the grid system used from Materialize CSS. 

### Tablet 

The search bar and buttons are responsive is that they now fit the tablet viewport and don't go beyond those margins. The dessert images are now in columns of 3 or 2, depending on the tablet. These are responsive as well as they have adjusted to the viewport that they are displayed in. 

### Mobile

The search bar adjusts down to fit the mobile viewport, with the reset and search buttons now being displayed on top of one another instead of side by side. The dessert images are now in one column to support the mobile viewport. 

## Register/Log In

### Desktop

The layout and design for these two pages are the same. The h1 remains centralised to each page and underneath is a responsive form. The form size is restricted having had used the 'container' class from Materialize CSS which reduces the width of the div and containing items. 

### Tablet 

The text and form adjust to fit the tablet viewport with the form being restricted still by the container class. 

### Mobile

On the mobile viewport, the forms are again responsive as they adjust to fit the mobile viewport. 

## Account 

### Desktop

On the desktop view, the items displayed depends on whether a user has uploaded any recipes or not. If they haven't, a message telling the user they haven't added anything and encouraging them to add a recipe is shown, with an image below. The message spans almost the width of the viewport and the image is responsive, yet again using the 'responsive-img' class. 
If a user has uploaded recipes, the layout of the page is similar to that of the recipes page. The image of the dessert appears on the page in the same fashion as the recipes page, and displays in columns of four for the desktop viewport. 

### Tablet 

If the user has no uploaded recipes, the messages, button and image show again. These are responsive as they adjust to fit the tablet viewport but if the user has uploaded recipes, then the dessert images are shown in columns of 2 or 3 depending on the individual tablet size. 

### Mobile

The message, button and image respond to the mobile viewport as they all convert down to the smaller size when on the mobile viewport. If a recipe has been uploaded, it will display in a column of one for the mobile viewport. 

## Add Recipes Page

### Desktop

The 'Add recipes' page has a simple h1 and a form to fill in for the user. The form is again restricted its width with the container class which makes it responsive. 

### Tablet

The form and h1 are smaller for the tablet viewport but big enough for the user to comfortably use. 
 
### Mobile

The h1 and form are again responsive to the mobile viewport, shrinking to fit. 

## Manage Categories

### Desktop

The manage categories page is only accessible to the admin. The cards displayed for the categories are the same as the recipes page, in that they will be presented in columns of 4 on the desktop viewport. 

### Tablet

The categories cards will display on tablet in rows of 3 or 2, depending on the tablet. 

### Mobile

The viewport for mobile devices displayed the categories in columns of one. 

## Browser Compatibility 

### [Google Chrome](https://www.google.co.uk/chrome/?brand=CHBD&gclid=EAIaIQobChMIi5nY65OY6gIVKoBQBh15wQBrEAAYASAAEgKlOvD_BwE&gclsrc=aw.ds)

The website was built using Google Chrome. DevTools were used to check for responsiveness of different viewports. With this browser, there are no bugs found, with the exception of those in the 'Unresolved Bugs' section. 


### [Firefox](https://www.mozilla.org/en-GB/firefox/new/)

The website is also responsive on Firefox and there were no bugs found while using the website in Firefox.

### [Microsoft Edge](https://www.microsoft.com/en-us/edge)

The website is responsive in Microsoft Edge and has no bugs. 

### [Safari](https://www.apple.com/uk/safari/) 

The site is responsive on Safari, with no bugs. 

## Bugs and solutions
- The description for the ‘Upload’ page was not displaying. 
	* This was because ‘recipe_description’ was written in the dictionary pair rather than just ‘description’. Resolved by updated the dictionary to the correct name. 
- User recipes were not showing on the accounts page. 
	* Resolved by adding the code - recipes = list(mongo.db.recipes.find()) from the get_recipes function to the account function. 
- The card images in the recipes page were stacking on top of one another instead of displaying as columns and rows. 
	* Resolved by correctly placing the {% endfor %} in the recipes template code. 
- Similar issue with account page as above – the uploaded recipes were not displaying as they should have been. 
	* Resolved, again by placing the {% endfor %} line in the correct place within the account template code. 
- Deleting categories as the admin was deleting the wrong category instead. Note – this was working before adding a modal confirmation screen, which appeared to be the cause of the problem. 
	* Resolved by changing the a href and modal id both to {{category._id}} so the modal correctly shows the deletion confirmation for the correct category. 
- The image and ‘method’ section on the full recipes page was shifted to the left.
	* Resolved by adding the ‘center-align’ class to the image div and methods div. 
- The background image for the website didn’t load correctly. Left whitespace where the flash messages should be. 
	* H1 margin was removed and the message position was changed to absolute, to remove it from the flow of the page displayed. 
- The edit recipes feature was redirecting the user back to the edit recipe page after saving an edited recipe. 
	* Resolved by adding return redirect(url_for(“account”, username=session[“user”]}} to the edit_recipe function. 
- Search bar had stopped working since adding Pagination
	* Fixed by adding pagination python functionality to the search function. 
- White space was displaying on the bottom of some pages 
	* Resolved by removing extra ‘row’ classes from divs. 
## Unresolved bugs
- When an uploaded recipe it edited, the ingredients and methods section include some [‘’] characters to the form. 


