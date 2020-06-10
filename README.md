# [Bookstore](https://**/)

[![Build Status](https://travis-ci.org/pramcistudent/bookstore-milestone-four.svg?branch=master)](https://travis-ci.org/pramcistudent/bookstore-milestone-four)

**Love Reading Books?**

The Bookstore holds a vast collection of reading material from some of the greatest authors such William Shakespeare, Stephen King, J.K. Rowling and many many more, you'll be sure to find the book you are looking for.

---
## Table of Contents
1. [**UX**](#ux)
    <!-- - [**User Stories**](#user-stories)
    - [**Design**](#design)
    - [**Wireframes**](#Wireframes) -->
2. [**Features**](#features)
    <!-- - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement) -->
3. [**Technologies Used**](#technologies-used)
    <!-- - [**Version Control**](#version-control)
    - [**Hosting**](#hosting) -->
4. [**Testing**](#testing)
    <!-- - [**Login Page**](#login-page)
    - [**Home Page**](#home-page)
    - [**Add Recipe Page (Registered users only)**](#add-recipe-page)
    - [**Recipe Details Page**](#recipe-details-page)
    - [**Username (Registered users only)**](#username)
    - [**Responsiveness Testing**](#responsiveness-testing) -->
5. [**Code Validation**](#code-validation)
    <!-- - [**Cross Browser Testing**](#cross-browser-testing) -->
6. [**Deployment**](#deployment)
    <!-- - [**Local Deployment**](#local-deployment)
    - [**Remote Deployment**](#remote-deployment) -->
7. [**Credits**](#credits)
    <!-- - [**Content**](#content)
    - [**Acknowledgements**](#acknowledgements) -->
---
### Why This Project
I created this app as part of the Full Stack Frameworks project of [**_Code Institute's_**](https://codeinstitute.net/) Full Stack Software Development course. The project scope was to create a online bookstore, which allows users to search and view books. Users can register to create an account which would then allow for the user to make a purchase.

The front-end display and functionality uses HTML, CSS and JavaScript. The back-end functionality uses Python, Django, SQLite3 and PostgreSQL.

## UX
Bookstore the online store for book lovers across the world. Users can register, login, browse or search for the book they want to read. Order your book, pay online, see your order history via the profile page. Loved reading that book why don't you leave a book review?

Bookstore is designed to give the user a clean modern experience with quick access to user needs with the browse or search functionality. The navigation bar provides one click links to the homepage, registration, login and browse all books. Only registered and logged in users can see the profile link.

### User Stories
"**_As a user, I would like to_** _____"
- see links to the registration, login pages.
- search the site by book title, author or category.
- create my own account as a registered user.
- see my profile page and order history.
- see the price of each book and be able to read more information about the book.
- be able to see user reviews to help me decide if I want to purchase the book.
- receive and email as order confirmation for my purchase.
- be able to track my order.

### Wireframes
I drew my wireframes using Powerpoint. I have different wireframes to show how to make my website/app responsive. The links to the files are below:
- [Home]()
- [Browse all books]()
- [Book detail]()
- [View cart]()
- [Checkout]()
- [Profile]()

### Database Schema
Before building my project, I created an Entity Relationship Diagram (ERD) to outline the database schema for the various tables that I would use.
Link to the file is below:
- [Bookstore Database Schema]()

## Features
### Existing Features

#### Home Page - serves as the initial landing page for all users
- **Navigation bar** - The navbar links vary depending on whether the user is logged in or not. If the user isn't logged in, the 'Home', 'Browse', 'Register' and 'Login' links are shown. When the user is logged in, the 'Home', 'Browse', 'Profile' and 'Logout' links are shown.
- **Featured Books** - This section displays 3 of the newest featured books the site has to offer to the user. Images are clickable to allow the user to view more information about the book.
- **Add to cart** - Allows the user to add the selected book into the cart.

#### Browse all books - this page displays a wide collection of books
- **Search** - The search function allows the user to search by book title, or filtered by author or category.
- **Books** - Displays a selection of books, images are clickable to allow the user to view more information about the book.
- **Pagination** - Has been added to allow the user to view 6 books per page.
- **Add to cart** - .

#### Single book view - all users are able to view this page, display more information about the selected book
- **Book image** - Displays an image of the book cover.
- **Book details** - displays the book title, book description, price, category, book author and description about the author.
- **Add to cart** - Clicking this button will add the selected book to cart and redirect the user to cart summary view.

#### Cart - shows the user a summary of the books that were added to the cart
- **Your items** - Display a summary of the books in cart with each book showing the book image, book title, and price.
- **Amend quantity** - User can amend the quantity of the book by clicking the '-' or '+' to increasing or decreasing the quantity in cart.
- **Remove from cart** - Allows the user to remove the book from cart.
- **Continue shopping** - Redirects the user back to the browse all books page to continue shopping.
- **Pay with card** - Allows the user to make a card payment.

#### Stripe - allows the user to pay securely using Stripe payment
- **Purchase Form** - This form connects to the Stripe API to process a user's card details. No card details are stored locally or on the server, they are only sent to Stripe and then discarded.

#### Thank You - after completing payment redirect the user to the Thank You page
- **Thank You page** - User receives confirmation that the order has been placed and is given a order reference number.
- **Email** - Email confirmation is sent to the user.

#### Registration - allow new user to register for an account
- **Register** - User must provide a unique username and email address, which are checked against existing entries in the database. A password is required, which must be entered twice to check it has been inputted correctly.
- **Message** - On successfully registering the user will be redirected to the home page. An alert message will notify the user that the account has been created and are now logged in.

#### Login - allow existing user to login to their account
- The login page only requires the user to input there username and password. There is a link to the register page so a user can create an account, and a password reset link if a user has forgotten or lost their password.

#### Profile - only available to logged in user
- **Password** - Users can change their password by inputting the old password and then the new password which must be entered twice to check it has been inputted correctly.
- **Order History**- Users are able to view a summary of their previous orders placed. 'View order' link provides a detail view of the selected order which can be printed. 'Track order' this feature is currently unavailable and is out of the scope of this project. Clicking the link opens a model to informs the user this feature is under development.

### Features Left to Implement
Due to a change in my personal circumstances and with more time and knowledge, I would have liked to implement some additional features to the app:
- **Track my order** - This feature is currently out of the scope of this project. I have added a link to the project to show potential of how it could be used. I feel this is an important feature to have, a user making any purchase online would generally want to be able to track there order.
- **Email confirmation** - As with all online purchases email confirmation should be sent to a user detailing out a summary of the purchase.

##### [back to top](#table-of-contents)
---
## Technologies Used
- [**HTML**](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
    - The project uses **HTML** to create the basic elements and content of my app.

- [**CSS**](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)
    - The project uses **CSS** to apply the custom styles to my app.

- [**Bootstrap**](https://getbootstrap.com/)
    - The project uses the **Bootstrap** framework to add a responsive grid system, prebuilt components, plugins built on jQuery, and Bootstrap styles, before adding my custom styles.

- [**jQuery**](https://jquery.com)
    - The project uses **jQuery** as the primary JavaScript functionality. This is both the standard jQuery that is built with Bootstrap components.

- [**Python**](https://www.python.org/)
    - The project uses **Python** as the back-end programming language for my app.

- [**Jinja**](https://jinja.palletsprojects.com/en/2.10.x/)
    - The project uses **Jinja** for templating with Flask in the HTML code. I used **Jinja** to simplify my HTML code, avoid repetition, and allow simpler linking of the back-end to the front-end.

- [**Font Awesome**](https://fontawesome.com/)
    - The project uses **Font Awesome** for the visual icons used in my app.

- [**SQLite**](https://www.sqlite.org/index.html)
    - The project uses **SQLite** as the relational database to hold the backend information for the varions models used, when running locally.

- [**PostgreSQL**](https://www.postgresql.org/)
    - The project uses Heroku's **PostgreSQL** relational database to hold the backend information for the various models used, when deployed remotely.

- [**Google Fonts**](https://fonts.google.com/)
    - The project uses **Google Fonts** for the typography. The font styles used in the app were *_Roboto_* font and the rest of the site uses the *_Noto Serif_* font.

- [**Stripe API**](https://stripe.com/gb)
    - The project uses **Stripe** to make secure payments for my app.

- [**Visual Studio Code**](https://code.visualstudio.com/)
    - I've used **Visual Studio Code** as the development environment to write the code for my app.

### Version Control
- [**Git**](https://git-scm.com/)
    - I've used **Git** as a version control system to regularly add and commit changes made to my project in Visual Studio Code, before pushing to GitHub.

- [**GitHub**](https://github.com/)
    - I've used **GitHub** as a remote repository to push and store the committed changes to my project from Git.

### Hosting
- [**Heroku**](https://www.heroku.com/)
    - I've used **Heroku** as the hosting platform to deploy my app.
##### [back to top](#table-of-contents)
---
## Testing
<!-- All tests were carried out manually. Testing process was as follows:
##### Login Page
###### Logo
* 
###### Guest User
* 
###### Sign In
* 
###### Sign Up
* 
##### Home Page
###### Navigation links
* 
###### All Recipes
* 
###### Filtered Recipes
* 
###### Pagination/Search result summary
* 
###### Recipe cards
* 
##### Add Recipe Page (Registered users only)
* 
##### Recipe Details Page
* 
##### Username (Registered users only)
###### My recipes 
* 
###### Logout 
*  -->

##### Responsiveness Testing


### Code Validation
- 

##### Cross Browser Testing


##### [back to top](#table-of-contents)
---

## Deployment
### Local Deployment


### Remote Deployment


##### [back to top](#table-of-contents)
---

## Credits
#### Content


#### Acknowledgements
<!-- - I would like to thank my mentor [Guido Cecilio](https://github.com/guidocecilio) for all his help and support during the development of this project.
- I would also like to thank other code institute students for sharing their projects which was extremely useful in designing this website.
- Thanks to the Slack community for their feedback and help on how to debug my Python code. -->

### Disclaimer
This project is for educational purposes only.

##### [back to top](#table-of-contents)
---