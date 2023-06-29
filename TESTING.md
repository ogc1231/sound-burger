# Testing

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

Unfortunately, pages that require a user to be logged-in and authenticated (CRUD functionality),
will not work using this method, due to the fact that the HTML Validator (W3C) doesn't have
access to login to your pages.

In order to properly validate HTML pages with Jinja syntax for authenticated pages, follow these steps:

- Navigate to the deployed pages which require authentication
- Right-click anywhere on the page, and select **View Page Source** (usually `CTRL+U` or `⌘+U` on Mac).
- This will display the entire "compiled" code, without any Jinja syntax.
- Copy everything, and use the [validate by input](https://validator.w3.org/#validate_by_input) method.

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fsoundburger.herokuapp.com%2F) | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/html-home.png) | Pass: No Errors |
| Menu | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fsoundburger.herokuapp.com%2Fmenu%2F) | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/html-menu.png) | Pass: No Errors |
| Cart | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fsoundburger.herokuapp.com%2Fcart%2F) | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/html-cart.png) | Pass: No Errors |
| Checkout | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fsoundburger.herokuapp.com%2Fcheckout%2F) | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/html-checkout.png) | Pass: No Errors |
| Reviews | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fsoundburger.herokuapp.com%2Freviews%2F) | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/html-reviews.png) | Pass: No Errors |
| Add Review | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fsoundburger.herokuapp.com%2Fadd%2F) | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/html-add.png) | Pass: No Errors |
| Edit Review | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fsoundburger.herokuapp.com%2Fedit%2F) | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/html-edit.png) | Pass: No Errors |
| Signup | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fsoundburger.herokuapp.com%2Faccounts%2Fsignup%2F) | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/html-signup.png) | Pass: No Errors |
| Signin | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fsoundburger.herokuapp.com%2Faccounts%2Flogin%2F) | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/html-login.png) | Pass: No Errors |
| Signout | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fsoundburger.herokuapp.com%2Faccounts%2Flogout%2F) | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/html-logout.png) | Pass: No Errors |

### CSS

I used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate my CSS files, style.css was validated with no errors found.

| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| style.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fogc1231.github.io%2Fsound-burger) | ![screenshot](documentation/css-validation-style.png) | Pass: No Errors |
| checkout.css | n/a | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/css-jigsaw-validator.png) | Pass: No Errors |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| admin.py (home) | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ogc1231/sound-burger/main/home/admin.py) | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/home-admin.png) | All clear, no errors found|
| models.py (home) | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ogc1231/sound-burger/main/home/models.py) | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/home-models.png) | All clear, no errors found|
| views.py (home) | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ogc1231/sound-burger/main/home/views.py) | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/home-views.png) | All clear, no errors found|
| admin.py (menu) | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ogc1231/sound-burger/main/menu/admin.py) | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/menu-admin.png) | All clear, no errors found|
| models.py (menu) | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ogc1231/sound-burger/main/menu/models.py) | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/menu-models.png) | All clear, no errors found|
| views.py (menu) | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ogc1231/sound-burger/main/menu/views.py) | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/menu-views.png) | All clear, no errors found|
| admin.py (reviews) | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ogc1231/sound-burger/main/reviews/admin.py) | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/reviews-admin.png) | All clear, no errors found|
| models.py (reviews) | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ogc1231/sound-burger/main/reviews/models.py) | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/reviews-models.png) | All clear, no errors found|
| views.py (reviews) | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ogc1231/sound-burger/main/reviews/views.py) | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/reviews-views.png) | All clear, no errors found|
| forms.py (reviews) | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ogc1231/sound-burger/main/reviews/forms.py) | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/reviews-forms.png) | All clear, no errors found|
| contexts.py (soundburger) | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ogc1231/sound-burger/main/soundburger/contexts.py) | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/soundburger-context.png) | All clear, no errors found|
| settings.py (soundburger) | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ogc1231/sound-burger/main/soundburger/settings.py) | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/soundburger-settings.png) | All clear, no errors found|
| urls.py (soundburger) | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ogc1231/sound-burger/main/soundburger/urls.py) | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/soundburger-urls.png) | All clear, no errors found|

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Screenshot | Notes |
| --- | --- | --- |
| Chrome | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/chrome.PNG) | Works as expected |
| Firefox | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/firefox.png) | Works as expected |
| Edge | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/edge.jpeg) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Screenshot | Notes |
| --- | --- | --- |
| Mobile (DevTools) | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/mobile-menu-closed.png) | Works as expected |
| Mobile (DevTools) | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/mobile-menu-open.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/tablet-checkout.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/tablet-menu-open.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/tablet-food-menu.png) | Works as expected |
| Razer Blade 15 | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/laptop-reviews.png) | Works as expected |
| Razer Blade 15 | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/laptop-menu.png) | Works as expected |
| 2k Monitor | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/xl-monitor-home.png) | Scaling starts to have minor issues with font sizes |
| 2k Monitor | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/xl-monitor-menu.png) | Scaling starts to have minor issues with font sizes |

## Lighthouse Audit

The deployed project was tested using the Lighthouse Audit tool to check for any major issues.

| Page | Size | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | Mobile | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/mobile-home.PNG) | Some minor warnings |
| Home | Desktop | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/desktop-home.PNG) | No major warnings |
| Menu | Mobile | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/mobile-menu.PNG) | No major warnings |
| Menu | Desktop | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/desktop-menu.PNG) | No major warnings |
| Cart | Mobile | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/mobile-cart.PNG) | No major warnings |
| Cart | Desktop | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/desktop-cart.PNG) | No major warnings |
| Checkout | Mobile | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/mobile-checkout.PNG) | No major warnings |
| Checkout | Desktop | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/desktop-checkout.PNG) | No major warnings |
| Reviews | Mobile | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/mobile-reviews.PNG) | No major warnings |
| Reviews | Desktop | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/desktop-reviews.PNG) | No major warnings |
| Add Review | Mobile | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/mobile-add.PNG) | No major warnings |
| Add Review | Desktop | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/desktop-add.PNG) | No major warning |
| Edit Review  | Mobile | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/mobile-edit.PNG) | No major warnings |
| Edit Review  | Desktop | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/desktop-edit.PNG) | No major warnings |
| Signin  | Mobile | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/mobile-signin.PNG) | No major warnings |
| Signin | Desktop | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/desktop-signin.PNG) | No major warnings |
| Signout  | Mobile | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/mobile-signout.PNG) | No major warnings |
| Signout  | Desktop | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/desktop-signout.PNG) | No major warnings |
| Signup  | Mobile | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/mobile-signup.PNG) | No major warnings |
| Signup  | Desktop | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/desktop-signup.PNG) | No major warnings |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Home Page/Navbar/Footer | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Click on Home link | Redirection to Home page | Pass | |
| | Click on Menu link in navbar | Redirection to Menu page | Pass | |
| | Click on Reviews link in navbar | Redirection to Reviews page | Pass | |
| | Click on Basket icon in navbar | Redirection to Cart page | Pass | |
| | Click on Logout link in navbar | Redirection to Logout page | Pass | |
| | Click on Signup link in navbar | Redirection to Signup page | Pass | |
| | Click on Signin  link in navbar | Redirection to Signin page | Pass | |
| | Click on Order Now link in hero section | Redirection to Menu page | Pass | |
| | Click on Instagram Icon in footer | Redirection to Instagram Homepage | Pass | |
| | Click on Facebook Icon in footer | Redirection to Facebook Homepage | Pass | |
| | Click on Twitter Icon in footer | Redirection to Twitter Homepage | Pass | |
| | Click on Tik Tok Icon in footer | Redirection to Tik Tok Homepage | Pass | |
| | Click on Oliver Craigie link in footer | Redirection to Oliver Craigie github page | Pass | |
| Signup Page | | | | |
| | Enter Username | Username is required | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click Sign Up button on sign up page | Redirection to Home page | Pass | |
| | Click Sign In link on sign up page | Redirection to Sign In page | Pass | |
| Login Page | | | | |
| | Enter correct username | Only accept correct username | Pass | |
| | Enter correct password | Field will only accept correct password | Pass | |
| | Click Login button on sign up page | Redirection to Home page | Pass | |
| | Click Sign Up link on sign In page | Redirection to Sign Up page | Pass | |
| Signout Page | | | | |
| | Click on Logout button | Logs user out and redirects to Home page | Pass | |
| Menu Page | | | | |
| | Click Add to cart button | Adds item to cart and redirects to Cart Page | Pass | |
| Cart Page | | | | |
| | Click Bin icon button | Removes item from cart and stays on Cart Page | Pass | |
| | Click Continue Shopping Button | Redirection to Menu page | Pass | |
| | Click Checkout Button | Redirection to Checkout page | Pass | |
| Checkout Page | | | | |
| | Click return to cart Button | Redirection to Cart page | Pass | |
| | Click Confirm Order Button | Submits order and redirects to Homepage | Pass | |
| | Enter Name | Name is required | Pass | |
| | Enter valid email address | Field will only accept email address format, email is required | Pass | |
| | Enter Address line 1 | Address line 1 is required | Pass | |
| | Enter Address line 2 | Address line 2 is NOT required | Pass | |
| | Choose District | District is required | Pass | |
| | Choose Eircode/Postcode | Eircode/Postcode is required | Pass | |
| Reviews Page | | | | |
| | Click Add a review Button | Redirection to Add Review page | Pass | |
| | Click Edit Review Button | Redirection to Edit Review page | Pass | |
| | Click Delete Review Button | Condirmation Modal pops up | Pass | |
| Delete Review Confirmation modal | | | | |
| | Click Cancel Button | Closes Modal and returns to Reviews Page | Pass | |
| | Click Delete Button | Closes Modal, Deletes Review and returns to Reviews Page | Pass | |
| Add Review Page | | | | |
| | Click Cancel Button | Redirection to Review page | Pass | |
| | Enter Title | Title is required | Pass | |
| | Enter Content | Content is required | Pass | |
| | Click Submit Review Button | Submits Review and redirects to Review page | Pass | |
| Edit Review Page | | | | |
| | Click Cancel Button | Redirection to Review page | Pass | |
| | Click Update Review Button | Updates Review and redirects to Review page | Pass | |
| Unauthenticated Users | | | | |
| | Unauthenticated Users Tries to access Cart Page | Returns Server Error (500) | Pass | |
| | Unauthenticated Users Tries to access Checkout Page | Returns Server Error (500) | Pass | |
| | Unauthenticated Users Tries to access Add_Review Page | Can access Add Review Page | Fail | |
| | Unauthenticated Users Tries to submit a Review | Returns Server Error (500) | Pass | | 
| | Unauthenticated Users Tries to access Edit_Review Page | Returns Not Found Error | Pass | |

## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a site administrator, I can access the admin panel so that I can see all users, orders, reviews, menu items & edit menus. | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/user-26.png) |
| As a new site user, I can view the menu so that I can see what items are available. | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/user-1.png) |
| As a new site user, I can register for an account so that I can become an authenticated user & order food.  | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/user-2.png) |
| As a new site user, I can read other reviews so that read about other people's experiences. | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/user-3.png) |
| As a new site user, I want to have a user-friendly interface so that I can access the information I need easily and be guided towards registering for an account. | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/user-4.png) |
| As a new site user I can see and click on social media links so that view the social media pages of SoundBurger. | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/user-5.png) |
| As a authenticated user I can login in my account so that order food. | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/user-6.png) |
| As a authenticated user I can logout of my account so that my data is safe.| ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/user-7.png) |
| As a authenticated user I can view add to cart buttons so that I can add food to cart. | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/user-8.png) |
| As a authenticated user I can edit/update my reviews so that change my reviews in case of grammar/spelling mistakes or to add extra information. | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/user-9.png) |
| As a authenticated user I can delete reviews I have written so that my reviews are deleted and able to be seen by anyone visiting the webpage. | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/user-10.png) |
| As a authenticated user I can access my cart so that I can see a list of all the items I have in my cart. | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/user-11.png) |
| As a authenticated user I can view the quantity of each item I have added to my cart so that so I know I have added to many or few items of each type selected.  | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/user-12.png) |
| As a authenticated user I can view the total price of items in cart so that I know the final cost of my order.  | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/user-13.png) |
| As a authenticated user I can delete items from the cart so that I can update my cart to have the correct quantity of items. | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/user-14.png) |
| As a authenticated user I can easily proceed to checkout page so that so checkout my order. | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/user-15.png) |
| As a authenticated user I can view the total quantity of items in my cart from any page so that I always know how many items are in my cart. | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/user-16.png) |
| As a authenticated user I can easily continue shopping when in the cart so that add more items to my cart.  | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/user-17.png) |
| As a authenticated user I can easily return to cart when in checkout so that so that I can adjust my order.  | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/user-18.png) |
| As a authenticated user I must confirm deletion of review so that I make sure I actually want to delete it and not just delete it by mistake. | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/user-19.png) |
| As a authenticated user I can cancel updating my review so that I don't have change my review if I decide I don't need to. | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/user-20.png) |
| As a authenticated user I can see order complete message so that I know my order has been made. | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/user-21.png) |
| As a authenticated user I can can see successfully signed out message so that I know I have been signed out.  | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/user-22.png) |
| As a authenticated user I can can see successfully signed in message so that I know I have been signed in.  | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/user-23.png) |
| As a authenticated user I can see removed item from cart message so that I know the item have been removed from cart. | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/user-24.png) |
| As a authenticated user I can see added item to cart message so that I know the item have been added to cart.  | ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/user-25.png) |

## Automated Testing

I have conducted a series of automated tests on my application.

I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### Python (Unit Testing)

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

Adjust the code below (file names, etc.) to match your own project files/folders.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

I have used Django's built-in unit testing framework to test the application functionality.

In order to run the tests, I ran the following command in the terminal each time:

`python3 manage.py test reviews`

To create the coverage report, I would then run the following commands:

`coverage run --source=name-of-app manage.py test`

`coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

`coverage html`

`python3 -m http.server`

Below are the results from the various apps on my application that I've tested:

| App | File | Coverage | Screenshot |
| --- | --- | --- | --- |
| Bag | test_forms.py | 99% | ![screenshot](documentation/py-test-bag-forms.png) |
| Bag | test_models.py | 89% | ![screenshot](documentation/py-test-bag-models.png) |
| Bag | test_urls.py | 100% | ![screenshot](documentation/py-test-bag-urls.png) |
| Bag | test_views.py | 71% | ![screenshot](documentation/py-test-bag-views.png) |
| Checkout | test_forms.py | 99% | ![screenshot](documentation/py-test-checkout-forms.png) |
| Checkout | test_models.py | 89% | ![screenshot](documentation/py-test-checkout-models.png) |
| Checkout | test_urls.py | 100% | ![screenshot](documentation/py-test-checkout-urls.png) |
| Checkout | test_views.py | 71% | ![screenshot](documentation/py-test-checkout-views.png) |
| Home | test_forms.py | 99% | ![screenshot](documentation/py-test-home-forms.png) |
| Home | test_models.py | 89% | ![screenshot](documentation/py-test-home-models.png) |
| Home | test_urls.py | 100% | ![screenshot](documentation/py-test-home-urls.png) |
| Home | test_views.py | 71% | ![screenshot](documentation/py-test-home-views.png) |
| Products | test_forms.py | 99% | ![screenshot](documentation/py-test-products-forms.png) |
| Products | test_models.py | 89% | ![screenshot](documentation/py-test-products-models.png) |
| Products | test_urls.py | 100% | ![screenshot](documentation/py-test-products-urls.png) |
| Products | test_views.py | 71% | ![screenshot](documentation/py-test-products-views.png) |
| Profiles | test_forms.py | 99% | ![screenshot](documentation/py-test-profiles-forms.png) |
| Profiles | test_models.py | 89% | ![screenshot](documentation/py-test-profiles-models.png) |
| Profiles | test_urls.py | 100% | ![screenshot](documentation/py-test-profiles-urls.png) |
| Profiles | test_views.py | 71% | ![screenshot](documentation/py-test-profiles-views.png) |
| x | x | x | repeat for all remaining tested apps/files |

#### Unit Test Issues

## Bugs

### Unfixed Bugs

- BUG: Incorrect times on reviews

    ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/bug.PNG)

    - Attempted to fix by adding "F d, Y @ H:m" form to updated & created times with no luck.

- BUG: Checkout page should be in two columns Shipping Address & Order Summary NOT two rows

    ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/bug-2.png)

    - Attempted to fix by adding flexbox to no result.

There are no more remaining bugs that I am aware of.

### GitHub **Issues**

**Open Issues**

Any remaining open issues can be tracked [here](https://github.com/ogc1231/sound-burger/issues).

| Issue | Status |
| --- | --- |
| [USER STORY: Can view contact info of SoundBurger](https://github.com/ogc1231/sound-burger/issues/68) | Open |
| [USER STORY: Choose to pickup order](https://github.com/ogc1231/sound-burger/issues/59) | Open |
| [USER STORY: Reset password](https://github.com/ogc1231/sound-burger/issues/58) | Open |
| [USER STORY: Delete account](https://github.com/ogc1231/sound-burger/issues/57) | Open |
| [BUG: Incorrect times on reviews](https://github.com/ogc1231/sound-burger/issues/69) | Open |
| [BUG: Checkout page should be in two columns Shipping Address & Order Summary NOT two rows](https://github.com/ogc1231/sound-burger/issues/70) | Open |

**Closed Issues**

| Issue | Status |
| --- | --- |
| [STYLING: Style Add Review page](https://github.com/ogc1231/sound-burger/issues/55) | Closed |
| [STYLING: Style Edit Review page](https://github.com/ogc1231/sound-burger/issues/54) | Closed |
| [STYLING: Style Reviews page](https://github.com/ogc1231/sound-burger/issues/53) | Closed |
| [STYLING: Style Cart & Checkout page](https://github.com/ogc1231/sound-burger/issues/51) | Closed |
| [STYLING: Style Menu page](https://github.com/ogc1231/sound-burger/issues/50) | Closed |
| [STYLING: Style Homepage](https://github.com/ogc1231/sound-burger/issues/49) | Closed |
| [SETUP: Install Django](https://github.com/ogc1231/sound-burger/issues/1) | Closed |
| [SETUP: Install psycopg2](https://github.com/ogc1231/sound-burger/issues/2) | Closed |
| [SETUP: Install Cloudinary](https://github.com/ogc1231/sound-burger/issues/3) | Closed |
| [SETUP: Create Project (soundburger)](https://github.com/ogc1231/sound-burger/issues/4) | Closed |
| [SETUP: Deploy to Heroku](https://github.com/ogc1231/sound-burger/issues/6) | Closed |
| [SETUP: Create ElephantSQL account](https://github.com/ogc1231/sound-burger/issues/7) | Closed |
| [SETUP: Create required folders and files](https://github.com/ogc1231/sound-burger/issues/8) | Closed |
| [SETUP: Create Admin Super User](https://github.com/ogc1231/sound-burger/issues/9) | Closed |
| [SETUP: Link Bootstrap](https://github.com/ogc1231/sound-burger/issues/14) | Closed |
| [SETUP: Link Bulma CSS](https://github.com/ogc1231/sound-burger/issues/15) | Closed |
| [SETUP: Install Summernote](https://github.com/ogc1231/sound-burger/issues/16) | Closed |
| [SETUP: Install AllAuth](https://github.com/ogc1231/sound-burger/issues/17) | Closed |
| [SETUP: Install Pillow](https://github.com/ogc1231/sound-burger/issues/23) | Closed |
| [SETUP: Create Burger Model](https://github.com/ogc1231/sound-burger/issues/24) | Closed |
| [SETUP: Create Drink Model](https://github.com/ogc1231/sound-burger/issues/25) | Closed |
| [SETUP: Create Side model](https://github.com/ogc1231/sound-burger/issues/26) | Closed |
| [SETUP: Install Crispy Forms](https://github.com/ogc1231/sound-burger/issues/27) | Closed |
| [SETUP: Create Reviews App](https://github.com/ogc1231/sound-burger/issues/28) | Closed |
| [SETUP: Create Home App](https://github.com/ogc1231/sound-burger/issues/47) | Closed |
| [SETUP: Create Menu App](https://github.com/ogc1231/sound-burger/issues/48) | Closed |
| [SETUP: Convert burger, side & drink models into one group model](https://github.com/ogc1231/sound-burger/issues/30) | Closed |
| [DOCUMENTATION & TESTING: Add README.md template](https://github.com/ogc1231/sound-burger/issues/11) | Closed |
| [DOCUMENTATION & TESTING: Create TESTING.md](https://github.com/ogc1231/sound-burger/issues/10) | Closed |
| [DOCUMENTATION & TESTING: Complete TESTING.md](https://github.com/ogc1231/sound-burger/issues/32) | Closed |
| [DOCUMENTATION & TESTING: Complete README.md](https://github.com/ogc1231/sound-burger/issues/31) | Closed |

**Milestones**

Milestones were used to break the development down into small managable chunks focusing on the most important elements first.

| Milestone | Status |
| --- | --- |
| [MVP Release](https://github.com/ogc1231/sound-burger/milestone/1) | Closed |
| [Second Iteration](https://github.com/ogc1231/sound-burger/milestone/2) | Closed |
| [Third Iteration](https://github.com/ogc1231/sound-burger/milestone/5) | Closed |
| [Bugs](https://github.com/ogc1231/sound-burger/milestone/6) | Open |
| [https://github.com/ogc1231/sound-burger/milestone/4](https://github.com/ogc1231/sound-burger/milestone/6) | Closed |
| [Documentation & Testing](https://github.com/ogc1231/sound-burger/milestone/3) | Closed |