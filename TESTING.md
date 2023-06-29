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

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

Defensive programming (defensive design) is extremely important!

When building projects that accept user inputs or forms, you should always test the level of security for each.
Examples of this could include (not limited to):

Forms:
- Users cannot submit an empty form
- Users must enter valid email addresses

PP3 (Python-only):
- Users must enter a valid letter/word/string when prompted
- Users must choose from a specific list only

Flask/Django:
- Users cannot brute-force a URL to navigate to a restricted page
- Users cannot perform CRUD functionality while logged-out
- User-A should not be able to manipulate data belonging to User-B, or vice versa
- Non-Authenticated users should not be able to access pages that require authentication
- Standard users should not be able to access pages intended for superusers

You'll want to test all functionality on your application, whether it's a standard form,
or uses CRUD functionality for data manipulation on a database.
Make sure to include the `required` attribute on any form-fields that should be mandatory.
Try to access various pages on your site as different user types (User-A, User-B, guest user, admin, superuser).

You should include any manual tests performed, and the expected results/outcome.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Home Page | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Click on Home link in navbar | Redirection to Home page | Pass | |
| Gallery Page | | | | |
| | Click on Gallery link in navbar | Redirection to Gallery page | Pass | |
| | Load gallery images | All images load as expected | Pass | |
| Contact Page | | | | |
| | Click on Contact link in navbar | Redirection to Contact page | Pass | |
| | Enter first/last name | Field will accept freeform text | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter message in textarea | Field will accept freeform text | Pass | |
| | Click the Submit button | Redirects user to form-dump | Pass | User must click 'Back' button to return |
| Sign Up | | | | |
| | Click on Sign Up button | Redirection to Sign Up page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click on Sign Up button | Asks user to confirm email page | Pass | Email sent to user |
| | Confirm email | Redirects user to blank Sign In page | Pass | |
| Log In | | | | |
| | Click on the Login link | Redirection to Login page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button | Redirects user to home page | Pass | |
| Log Out | | | | |
| | Click Logout button | Redirects user to logout page | Pass | Confirms logout first |
| | Click Confirm Logout button | Redirects user to home page | Pass | |
| Profile | | | | |
| | Click on Profile button | User will be redirected to the Profile page | Pass | |
| | Click on the Edit button | User will be redirected to the edit profile page | Pass | |
| | Click on the My Orders link | User will be redirected to the My Orders page | Pass | |
| | Brute forcing the URL to get to another user's profile | User should be given an error | Pass | Redirects user back to own profile |

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

Repeat for all other tests, as applicable to your own site.
The aforementioned tests are just an example of a few different project scenarios.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

## User Story Testing

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

Testing user stories is actually quite simple, once you've already got the stories defined on your README.

Most of your project's **features** should already align with the **user stories**,
so this should as simple as creating a table with the user story, matching with the re-used screenshot
from the respective feature.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

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

`python3 manage.py test name-of-app `

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

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

Use this section to list any known issues you ran into while writing your unit tests.
Remember to include screenshots (where possible), and a solution to the issue (if known).

This can be used for both "fixed" and "unresolved" issues.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

## Bugs

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

It's very important to document any bugs you've discovered while developing the project.
Make sure to include any necessary steps you've implemented to fix the bug(s) as well.

For JavaScript and Python applications, it's best to screenshot the errors to include them as well.

**PRO TIP**: screenshots of bugs are extremely helpful, and go a long way!

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- JS Uncaught ReferenceError: `foobar` is undefined/not defined

    ![screenshot](documentation/bug01.png)

    - To fix this, I _____________________.

- JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).

    ![screenshot](documentation/bug02.png)

    - To fix this, I _____________________.

- Python `'ModuleNotFoundError'` when trying to import module from imported package

    ![screenshot](documentation/bug03.png)

    - To fix this, I _____________________.

- Django `TemplateDoesNotExist` at /appname/path appname/template_name.html

    ![screenshot](documentation/bug04.png)

    - To fix this, I _____________________.

- Python `E501 line too long` (93 > 79 characters)

    ![screenshot](documentation/bug04.png)

    - To fix this, I _____________________.

### GitHub **Issues**

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

An improved way to manage bugs is to use the built-in **Issues** tracker on your GitHub repository.
To access your Issues, click on the "Issues" tab at the top of your repository.
Alternatively, use this link: https://github.com/ogc1231/sound-burger/issues

If using the Issues tracker for your bug management, you can simplify the documentation process.
Issues allow you to directly paste screenshots into the issue without having to first save the screenshot locally,
then uploading into your project.

You can add labels to your issues (`bug`), assign yourself as the owner, and add comments/updates as you progress with fixing the issue(s).

Once you've sorted the issue, you should then "Close" it.

When showcasing your bug tracking for assessment, you can use the following format:

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

**Fixed Bugs**

All previously closed/fixed bugs can be tracked [here](https://github.com/ogc1231/sound-burger/issues?q=is%3Aissue+is%3Aclosed).

| Bug | Status |
| --- | --- |
| [JS Uncaught ReferenceError: `foobar` is undefined/not defined](https://github.com/ogc1231/sound-burger/issues/1) | Closed |
| [Python `'ModuleNotFoundError'` when trying to import module from imported package](https://github.com/ogc1231/sound-burger/issues/2) | Closed |
| [Django `TemplateDoesNotExist` at /appname/path appname/template_name.html](https://github.com/ogc1231/sound-burger/issues/3) | Closed |

**Open Issues**

Any remaining open issues can be tracked [here](https://github.com/ogc1231/sound-burger/issues).

| Bug | Status |
| --- | --- |
| [JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).](https://github.com/ogc1231/sound-burger/issues/4) | Open |
| [Python `E501 line too long` (93 > 79 characters)](https://github.com/ogc1231/sound-burger/issues/5) | Open |

## Unfixed Bugs

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

You will need to mention unfixed bugs and why they were not fixed.
This section should include shortcomings of the frameworks or technologies used.
Although time can be a big variable to consider, paucity of time and difficulty understanding
implementation is not a valid reason to leave bugs unfixed.

If you've identified any unfixed bugs, no matter how small, be sure to list them here.
It's better to be honest and list them, because if it's not documented and an assessor finds the issue,
they need to know whether or not you're aware of them as well, and why you've not corrected/fixed them.

Some examples:

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- On devices smaller than 375px, the page starts to have `overflow-x` scrolling.

    ![screenshot](documentation/unfixed-bug01.png)

    - Attempted fix: I tried to add additional media queries to handle this, but things started becoming too small to read.

- For PP3, when using a helper `clear()` function, any text above the height of the terminal does not clear, and remains when you scroll up.

    ![screenshot](documentation/unfixed-bug02.png)

    - Attempted fix: I tried to adjust the terminal size, but it only resizes the actual terminal, not the allowable area for text.

- When validating HTML with a semantic `section` element, the validator warns about lacking a header `h2-h6`. This is acceptable.

    ![screenshot](documentation/unfixed-bug03.png)

    - Attempted fix: this is a known warning and acceptable, and my section doesn't require a header since it's dynamically added via JS.

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

If you legitimately cannot find any unfixed bugs or warnings, then use the following sentence:

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

There are no remaining bugs that I am aware of.
