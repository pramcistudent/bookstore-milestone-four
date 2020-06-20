# [Bookstore](https://pram-bookstore.herokuapp.com/)

[![Build Status](https://travis-ci.org/pramcistudent/bookstore-milestone-four.svg?branch=master)](https://travis-ci.org/pramcistudent/bookstore-milestone-four)

**Love Reading Books?**

The Bookstore holds a vast collection of reading material from some of the greatest authors such William Shakespeare, Stephen King, J.K. Rowling and many many more, you'll be sure to find the book you are looking for.

---
## Table of Contents
1. [**Why This Project**](#why-this-project) 
2. [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Wireframes**](#Wireframes)
    - [**Database Schema**](#design)
3. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)
4. [**Technologies Used**](#technologies-used)
    - [**Version Control**](#version-control)
    - [**Hosting**](#hosting)
5. [**Testing**](#testing)

6. [**Deployment**](#deployment)
    - [**Local Deployment**](#local-deployment)
    - [**Remote Deployment**](#remote-deployment)
7. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Acknowledgements**](#acknowledgements)
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
- [Home](https://github.com/pramcistudent/bookstore-milestone-four/blob/master/wireframes/Home%20Page.pdf)
- [Browse all books](https://github.com/pramcistudent/bookstore-milestone-four/blob/master/wireframes/Browse%20Page.pdf)
- [Book detail](https://github.com/pramcistudent/bookstore-milestone-four/blob/master/wireframes/Book%20Detail%20Page.pdf)
- [View cart](https://github.com/pramcistudent/bookstore-milestone-four/blob/master/wireframes/Cart%20Page.pdf)
- [Profile](https://github.com/pramcistudent/bookstore-milestone-four/blob/master/wireframes/Profile%20Page.pdf)

### Database Schema
Before building my project, I created an Entity Relationship Diagram (ERD) to outline the database schema for the various tables that I would use.
Link to the file is below:
- [Bookstore Database Schema]()

## Features
### Existing Features

#### Home Page - serves as the initial landing page for all users
- **Navigation bar** - The navbar links vary depending on whether the user is logged in or not. If the user isn't logged in, the 'Home', 'Browse', 'Register' and 'Login' links are shown. When the user is logged in, the 'Home', 'Browse', 'Profile' and 'Logout' links are shown.
- **Featured Books** - This section displays 3 of the newest featured books the site has to offer to the user. Images are clickable to allow the user to view more information about the book.
- **More Info** - Visible to users not logged in, allows the user to click the button and redirects them to the selected book detail page.
- **Add to cart** - Visible to users logged in, clicking this button will add the selected book to shopping cart and redirects the user to cart summary view.

#### Browse all books - this page displays a wide collection of books
- **Search** - The search function allows the user to search by book title, or filtered by author or category.
- **Books** - Displays a selection of books, images are clickable to allow the user to view more information about the book.
- **More Info** - Visible to users not logged in, allows the user to click the button and redirects them to the selected book detail page.
- **Add to cart** - Visible to users logged in, clicking this button will add the selected book to shopping cart and redirects the user to cart summary view.
- **Pagination** - Has been added to allow the user to view 6 books per page.

#### Single book view - all users are able to view this page, display more information about the selected book
- **Book image** - Displays an image of the book cover.
- **Book details** - displays the book title, book description, price, category, book author and description about the author.
- **Register** - Visible to users not logged in, informs the user that they can register to buy this book. Clicking the link redirects the user to the register page.
- **Add to cart** - Visible to users logged in, clicking this button will add the selected book to shopping cart and redirects the user to cart summary view.
- **Add review** - Only users logged in are able to write and submit a review comment. Users not logged in will see a link asking them to 'Register' which redirects the user to the register page.
- **Reviews** - All user are able to see review comments.

#### Cart - shows the user a summary of the books that were added to the cart
- **Your items** - Display a summary of the books in cart with each book showing the book image, book title, and price.
- **Amend quantity** - User can amend the quantity of the book by clicking the '-' or '+' to increasing or decreasing the quantity in cart.
- **Remove from cart** - Allows the user to remove the book from cart using a two-step process.
- **Continue shopping** - Redirects the user back to the browse all books page to continue shopping.
- **Pay with card** - Allows the user to make a card payment.

#### Stripe - allows the user to pay securely using Stripe payment
- **Purchase Form** - This form connects to the Stripe API to process a user's card details. No card details are stored locally or on the server, they are only sent to Stripe and then discarded.

#### Thank You - after completing payment redirect the user to the Thank You page
- **Thank You page** - User receives confirmation that the order has been placed and is given a order reference number.
- **Email** - This function has not been implemented due to an error with connecting to Gmail. An issue ticket has been raised with Gmail support.

#### Registration - allow new user to register for an account
- **Register** - User must provide a unique username and email address, which are checked against existing entries in the database. A password is required, which must be entered twice to check it has been input correctly.
- **Message** - On successfully registering the user will be redirected to the home page. An alert message will notify the user that the account has been created and they are now logged in.

#### Login - allow existing user to login to their account
- The login page only requires the user to input there username and password. There is a link to the register page so a user can create an account, and a password reset link if a user has forgotten or lost their password.

#### Profile - only available to logged in user
- **Password** - Users can change their password by inputting the old password and then the new password which must be entered twice to check it has been input correctly.
- **Order History**- Users are able to view a summary of their previous orders placed. Users can click on icon link 'View order' which provides a detail view of the selected order which can be printed. Users can click icon 'Track order' this feature is currently unavailable and is out of the scope of this project. Clicking the link opens a model to informs the user this feature is under development.

#### 404 and 500 Error Pages
-  I've included custom 404 and 500 error messages and error handlers to catch these errors. My custom messages allow the user to redirect back to the home page.

### Features Left to Implement
Due to a change in my personal circumstances and with more time and knowledge, I would have liked to implement some additional features to the app:
- **Track my order** - This feature is currently out of the scope of this project. I have added a link to the project to show potential of how it could be used. I feel this is an important feature to have, a user making any purchase online would generally want to be able to track there order.
- **Email confirmation** - As with all online purchases email confirmation should be sent to a user detailing out a summary of the purchase. Currently not implemented due to an issue with connecting to Gmail. An issue ticket has been raised with Gmail support.

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


##### [back to top](#table-of-contents)
---

## Deployment
I used GitHub for my version control and Heroku to host the live version of my project. To deploy my website to Heroku, 
I used the following steps:

1. Created the app using a unique name in Heroku.

2. Went to the **Resources** tab in Heroku and searched for **Heroku Postgres** in the 'Add-Ons' section.

3. Selected the free **Hobby** level.

4. Updated the `env.py` file within my local workspace with the `DATABASE_URL` details, and the `settings.py` to connect to the database using the `dj_database_url` package.

5. Ran the `python manage.py makemigrations`, `python manage.py migrate`, `python manage.py createsuperuser` commands to migrate the models into Heroku Postgres and create a new super user in the new PostgreSQL database.

6. Went to the **Settings** tab in Heroku and clicked on the **Reveal Config Vars** button.

7. Copied and pasted all of the `env.py` default variables into Heroku's Config Vars settings.

KEY | VALUE
--- | -----
DATABASE_URL | link to db |
AWS_ACCESS_KEY_ID | aws access key |
AWS_SECRET_ACCESS_KEY | aws secret key |
AWS_STORAGE_BUCKET_NAME | aws bucket name |
SECRET_KEY | site secret key |
STRIPE_PUBLISHABLE_KEY | stripe key |
STRIPE_SECRET_KEY | stripe secret key |

8. Went to the **Deploy** tab in Heroku, connected my app to my GitHub repository and selected **Enable Automatic Deployment** as the deployment method.

9. Went to the **Developers** section in Stripe and clicked on **API Keys**.

10. Copied and pasted the **Publishable Key** and **Secret Key** and set them as the `STRIPE_PUBLISHABLE_KEY` and `STRIPE_SECRET_KEY` environment variables in the `env.py` file within my local workspace. These were also added to the Heroku's Config Vars settings.

11. Updated the `settings.py` with the new Stripe environment variables.

12. Went to the **S3** section of AWS and created a new S3 bucket.

13. Within the relevant bucket's permissions, changed the **CORS Configuration** to the following:
    ```
    <?xml version="1.0" encoding="UTF-8"?>
    <CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <CORSRule>
        <AllowedOrigin>*</AllowedOrigin>
        <AllowedMethod>GET</AllowedMethod>
        <AllowedMethod>HEAD</AllowedMethod>
        <MaxAgeSeconds>3000</MaxAgeSeconds>
        <AllowedHeader>Authorization</AllowedHeader>
    </CORSRule>
    </CORSConfiguration>
    ```

14. Still in the **S3** section, changed the **Bucket Policy** to the following:
    ```
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "PublicReadGetObject",
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::<my-bucket-name>/*"
            }
        ]
    }
    ```
15. Replaced the `<my-bucket-name>` in the `Resource` line with my S3 bucket's name instead.

16. Went to the **IAM** section of AWS, created a 'New Group' and attached my S3 bucket to it.

17. Still in the **IAM** section, created a 'New Policy' and a 'New User' and attached these to the newly created group.

18. Updated the `settings.py` file in my local workspace with the relevant S3 bucket details:
    ```
    AWS_S3_OBJECT_PARAMETERS = {
        "Expires": "Thu, 31 Dec 2099 20:00:00 GMT",
        "CacheControl": "max-age=94608000",
    }
    AWS_STORAGE_BUCKET_NAME = "<s3-bucket-name>"
    AWS_S3_REGION_NAME = "<region-name>"
    AWS_ACCESS_KEY_ID = <access-key-id>
    AWS_SECRET_ACCESS_KEY = <secret-access-key>
    AWS_DEFAULT_ACL = None
    AWS_S3_CUSTOM_DOMAIN = "%s.s3.amazonaws.com" % AWS_STORAGE_BUCKET_NAME
    ```

19. Created a `custom_storages.py` file with classes to route to the relevant location settings for static and media files.

20. Updated the `settings.py` file with the relevant configuration for static and media file storage.

21. Ran the `python manage.py collectstatic` command to push the static files to my S3 bucket.

22. Created a requirements.txt file using the following command in the terminal window:
    ```pip3 freeze --local > requirements.txt```

23. Created a Procfile using the following command in the terminal window:
    ```echo web: gunicorn bookstore.wsgi:application > Procfile```

24. Ran the `git add .`, `git commit -m "<commit-message>"` and `git push` commands to push all changes to my GitHub repository.

The app was successfully deployed to Heroku at this stage.

### Repository Link

Click the link below to visit my project's GitHub repository:

[Bookstore Repository](https://github.com/pramcistudent/bookstore-milestone-four)

### Running Code Locally

To run my code locally, users can download a copy of my code to their desktop by completing the following steps:

1. Go to my [GitHub repository](https://github.com/pramcistudent/bookstore-milestone-four)

2. Click on 'Clone or download' under the repository name.

3. Copy the clone URL for the repository in the 'Clone with HTTPs section'.

4. Open 'Git Bash' in your local IDE.

5. Change the current working directory to the location where you want the cloned directory to be made.

6. Type `git clone`, then paste the URL you copied in Step 
    
    ```git clone https://github.com/USERNAME/REPOSITORY```

7. Press `Enter` to complete the process and clone the repository.

8. Complete one of the two below steps in your local workspace to set your own credentials for the environment variables:
    - Create a `env.py` file with your own credentials and import this into the `settings.py` file

9. Install the `requirements.txt` file by running the below command in your CLI Terminal:

    ```pip3 install -r requirements.txt```

10. Run one of the following commands in your Terminal to launch the Django project:

    ```python manage.py runserver```

11. Click the `http://` link that loads, and the project should load. If it doesn't load when you click the link, copy and paste it into a new browser tab instead.

12. Run the following commands to migrate the database models and create a super user:
    ```
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    ```

Once the migrations are completed and the super user has been created successfully, the site should be running locally. To deploy the site remotely, follow the instructions in the [Deployment](#Deployment) section.

##### [back to top](#table-of-contents)
---

## Credits
#### Content


#### Acknowledgements
<!-- - I would like to thank my mentor [Guido Cecilio](https://github.com/guidocecilio) for all his help and support during the development of this project.
- Thanks to the Slack community for their feedback and help on how to debug my Python code. -->

### Disclaimer
This project is for educational purposes only.

##### [back to top](#table-of-contents)
---