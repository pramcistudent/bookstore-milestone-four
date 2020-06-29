<p align="center">
  <img src="https://pram-bookstore.s3.eu-west-2.amazonaws.com/static/img/logo.png">
</p>

### Manual Testing

#### Home Page (Logged Out)

##### Navigation Bar
- Correct links are displayed `Home`, `Browse`, `Register`, `Login`, clicking the links redirect to the correct page.

##### Featured Books
- Book images are clickable and redirect to the correct page.
- `More Info` button is displayed and clicking redirects to the correct page.

##### Footer
- The links in the footer open a new tab and link to the correct page.

#### Browse Books Page

##### Search
- Search `by title`, inputting a book title into the search field and clicking the search button redirects to the correct search page with the filtered results.
- Search `by author`, clicking the dropdown menu and select the author. Clicking the search button redirects to the correct search page with the filtered results.
- Search `by category`, inputting a category into the search field and clicking the search button redirects to the correct search page with the filtered results.
- Search page clicking the `reset` button redirects to the correct page. 

##### Browse Books
- Book images are clickable and redirect to the correct page.
- `More Info` button is displayed and clicking redirects to the correct page.

##### Pagination
- Is only displayed when there are more than 6 books to be displayed per page.
- Is visible both above and below the list of books displayed. 
- Clicking the pagination buttons work as expected.

#### Book Detail Page

##### Book Information
- `Register here and buy this book!` is displayed, clicking the link redirects to the correct page.
- Write a review displays the correct instructions to notify the user they need to `sign in` to write a review. Clicking the link redirects to the correct page.

#### User Authentication

##### New User Registration
- Confirmed account creation works and upon successful creation of account, user is logged in and redirected the the home page.
- If details are missing or entered incorrectly, no account is created, and the incorrect field(s) tell the user what went wrong.
- `Already have an account? Login` correctly links to the login page.

##### Log In System
- Confirmed login system works for registered users.
- If a user enters incorrect details, this is communicated to them.
- Link for `Forgot Password?` redirects to the correct page.
- Link for `Register` redirects the the correct page.

#### Home Page (Logged In)

##### Navigation Bar
- Correct links are displayed `Home`, `Browse`, `Profile`, `Logout`, clicking the links redirect to the correct page.

##### Featured Books
- `Add to Cart` button is displayed and clicking adds the selected book to cart then redirects the correct page.

#### Browse Books Page

##### Browse Books
- `Add to Cart` button is displayed and clicking adds the selected book to cart then redirects the correct page.

#### Book Detail Page

##### Book Information
- `Add to Cart` button is displayed and clicking adds the selected book to cart then redirects to the correct page.
- `Write a review` form is visible and can only be completed by authenticated user. Tested and works correctly once submitted the review is displayed under the `Review` tab.

#### Cart Page

##### Your Shopping Cart
- Amending the quantity by clicking the `-` or `+` icons changes the quantity in cart. 
- The cart quantity and total price are update to reflect the changes made. 
- Tooltips appear when hovered over each icon.
- Two step confirmation is used when the `Delete` icon is clicked. A popup is displayed asking the user `Are you sure you want to remove the item from cart?`. 
- Clicking ok removes the item from cart and updates the basket total value to reflect changes made.
- `Continue Shopping` button redirects to the correct page.
- Clicking the `Pay with Card` button brings up the stripe payment interface. Using the Stripe Test Payment method I used the below Visa numbers to test the stripe payment:

```
Card Number - 4242 4242 4242 4242
Expiry MM/YY - 01/21
CVC - 111
```
- Payment was successful using the Test Payment method and redirects to the Thank You page.
- Confirmed email is generated on successfully processing an order and is sent to the specified user email account.

#### Profile Page

##### Profile Tab
- `Change my password` button redirects to the correct page.
- Password reset form checks the old password matches the current  password in database. New password must be entered twice and is checked that it has been input correctly. An error is shown if the passwords do not match.
- Confirmed the password reset change works and user is able to login using the new password.

##### Order History Tab
- `Order Details` link redirects to the correct page.
- `Track Order` link brings up the pop up modal to inform user "This feature is currently under development".
- Tooltips appear when hovered over each icon.

##### Order Details Page
- `Back to Profile` button redirects to the correct page.
- `Print Order` brings up the correct print preview page.
- Printing the page was successful.

---
Return back to main [README.md](README.md)