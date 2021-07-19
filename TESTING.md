## Testing

## Code Validation
- [W3C Mark-up Validation](https://validator.w3.org/) was used for checking for validity and to ensure there were no errors in the html code. 
- [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) was used for checking errors in the CSS. 
- [JSHint](https://jshint.com/) was used to check for validity of the JavaScript. 
- [Pep8 Online](http://pep8online.com/) was used to check for errors in Python. 

## User Story Tests

As a user – 
•	I want to be able to search for recipes –
- There is a search bar on the recipes page which allows users to search recipes by name and ingredients. 

•	I want to see a variety of dessert recipes – 
- 12 initial desserts were added the to the original database for the user to browse. This number will likely grow as users add their own recipes to the website. 

•	I want to be able to navigate the website easily
- The website has a navbar at the top of each page with links to navigate the website. These links are clearly named and easily accessible from all pages on the website. The navbar is also available in a dropdown menu on smaller viewports for easy navigation. 
•	I want an attractive layout and colours for the website
- The layout and design has been created to attract users and to make them want to upload their own recipes. As mentioned before, the background colors were chosen as such in order to make the dessert images pop out, rather than detract from the main features. 
•	I want to be able to see images of the desserts and ingredients/methods to make these, in further detail 
The recipes page contains photos of the desserts. These can then be hovered over for a further description of the desserts and a “Full Recipe” link allows the user to look at the full recipe of the dessert, including the ingredients, method and a larger image of the dessert clicked. 
•	I want to be able to register an account for myself 
- Users are able to register for an account with a password and username. This account is then accessible again to the user, after logging out. 
•	I want to be able to upload and amend recipes of my own
- Users can upload their own recipes via the ‘Upload’ page with details such as ingredients, method and even an image url. Once a recipe has been uploaded, users are able to view them on their account page and are able to edit a recipe as desired. 
•	I want to be able to delete recipes I have uploaded
- Users can delete their own recipes via the account page, which permanently deletes the recipe. 
•	I want to be able to easily access recipes I have previously uploaded
- Each user’s uploaded recipes are accessible on the ‘Account’ page. However, users can only access their own recipes on the account page, whereas they can view all recipes from all users and the original database via the ‘Recipes’ page.
•	I want to be able to log back into my account once I have registered
- Users are remembered an are able to log back into their accounts. 
•	I want social media links for the website so I can follow them
- The footer contains social media links, which are accessible via the social media icons. 
As an admin – 
•	I want to be able to add categories
- The admin is able to add new categories to the recipe website, via the “Manage Categories” page, via the “Add Category” button, which redirects the admin to an upload page, similar to the upload page for recipes. 
•	I want to be able to edit categories
- Categories are editable to the admin only, again accessible from the ‘Manage Categories’ Page. 
•	I want to be able to delete categories
- The admin is able to delete categories, again from the ‘Manage Categories’ page. Once the admin choses to delete a category, it is permanently deleted. 
## Responsiveness
## Browser Compatibility 
## Bugs and solutions
- the description for the ‘Upload’ page was not displaying. 
	* This was because ‘recipe_description’ was written in the dictionary pair rather than just ‘description’. Resolved by updated the dictionary to the correct name. 
- User recipes were not showing on the accounts page. 
	* Resolved by adding the code - recipes = list(mongo.db.recipes.find()) from the get_recipes function to the account function. 
- the card images in the recipes page were stacking ontop of one another instead of displaying as columsn and rows. 
	* resolved by correctly placing the {% endfor %} in the recipes template code. 
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


