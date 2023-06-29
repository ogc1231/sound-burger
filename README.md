# SOUND BURGER

This is the website for SoundBurger, a burger delivery only resturant based in Dublin, Ireland. The aim of the website is to allow users to create an account and order food from am updateable menu which can be added to a cart, checkedout and delivered to their address. It also functions as place where users can leave reviews about their experinces with SoundBurger, the food and the service. 

The website aim was to build a fullstack website with CRUD functionality using the Django framework and agile methodologies.

[Live link to website](https://soundburger.herokuapp.com/)

![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/screenshots/mockup.PNG)

## UX

### Colour Scheme

- `#FFE08A` used for main background.
- `#4A4A4A` used for main text.
- `#f14668` used for buttons.
- `#00d1b2` used for buttons and burger background.
- `#3E8ED0` used for buttons and drink background.
- `#48C78E` used for side background.
- `##ffffff` used for review card background.
- `#FAFAFA` used for footer background.

I used [coolors.co](https://coolors.co/f14668-ffe08a-3e8ed0-48c78e-00d1b2-4a4a4a-fafafa-ffffff) to generate my colour palette.

![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/screenshots/coolors.PNG)

### Typography

- [Baloo Tamma 2](https://fonts.google.com/specimen/Baloo+Tamma+2?query=Baloo+Tamma+2) was used for the primary headers and titles.

- [Lato](https://fonts.google.com/specimen/Lato) was used for all other secondary text.

- [Font Awesome](https://fontawesome.com) icons were used throughout the site, except icons in the footer.

- [Bootstrap](https://icons.getbootstrap.com/) icons were used only for icons in the footer.

## User Stories

### New Site Users

- As a new site user, I can view the menu so that I can see what items are available. `(MUST HAVE)`
- As a new site user, I can register for an account so that I can become an authenticated user & order food. `(MUST HAVE)`
- As a new site user, I can read other reviews so that read about other people's experiences. `(MUST HAVE)`
- As a new site user, I want to have a user-friendly interface so that I can access the information I need easily and be guided towards registering for an account. `(SHOULD HAVE)`
- As a new site user I can see and click on social media links so that view the social media pages of SoundBurger. `(COULD HAVE)`
- As a user I can view contact contact info of SoundBurger so that contact them to ask questions. `(WON'T HAVE)`

### Authenticated?Registered Site Users

- As a authenticated user I can login in my account so that order food. `(MUST HAVE)`
- As a authenticated user I can logout of my account so that my data is safe. `(MUST HAVE)`
- As a authenticated user I can view add to cart buttons so that I can add food to cart. `(MUST HAVE)`
- As a authenticated user I can edit/update my reviews so that change my reviews in case of grammar/spelling mistakes or to add extra information. `(MUST HAVE)`
- As a authenticated user I can delete reviews I have written so that my reviews are deleted and able to be seen by anyone visiting the webpage. `(MUST HAVE)`
- As a authenticated user I can access my cart so that I can see a list of all the items I have in my cart. `(MUST HAVE)`
- As a authenticated user I can view the quantity of each item I have added to my cart so that so I know I have added to many or few items of each type selected. `(MUST HAVE)`
- As a authenticated user I can view the total price of items in cart so that I know the final cost of my order. `(MUST HAVE)`
- As a authenticated user I can delete items from the cart so that I can update my cart to have the correct quantity of items. `(MUST HAVE)`
- As a authenticated user I can easily proceed to checkout page so that so checkout my order. `(MUST HAVE)`
- As a authenticated user I can view the total quantity of items in my cart from any page so that I always know how many items are in my cart. `(SHOULD HAVE)`
- As a authenticated user I can easily continue shopping when in the cart so that add more items to my cart. `(SHOULD HAVE)`
- As a authenticated user I can easily return to cart when in checkout so that so that I can adjust my order. `(SHOULD HAVE)`
- As a authenticated user I must confirm deletion of review so that I make sure I actually want to delete it and not just delete it by mistake. `(SHOULD HAVE)`
- As a authenticated user I can cancel updating my review so that I don't have change my review if I decide I don't need to. `(SHOULD HAVE)`
- As a authenticated user I can see order complete message so that I know my order has been made. `(SHOULD HAVE)`
- As a authenticated user I can can see successfully signed out message so that I know I have been signed out. `(COULD HAVE)`
- As a authenticated user I can can see successfully signed in message so that I know I have been signed in. `(COULD HAVE)`
- As a authenticated user I can see removed item from cart message so that I know the item have been removed from cart. `(COULD HAVE)`
- As a authenticated user I can see added item to cart message so that I know the item have been added to cart. `(COULD HAVE)`
- As a authenticated user I can delete my account so that my account and my information is deleted. `(WON'T HAVE)`
- As a authenticated user I can reset my password so that change my password if forgotten or need to update for other reasons. `(WON'T HAVE)`
- As a authenticated user I can choose to pickup my order so that I don't have wait for food to be delivered. `(WON'T HAVE)`

### Site Admin

- As a site administrator, I can access the admin panel so that I can see all users, orders, reviews, menu items & edit menus. `(MUST HAVE)`

## Wireframes

To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.
I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

### Home Page Wireframes

| Size | Screenshot |
| --- | --- |
| Mobile | ![screenshot](documentation/wireframes/mobile-home.png) |
| Tablet | ![screenshot](documentation/wireframes/tablet-home.png) |
| Desktop | ![screenshot](documentation/wireframes/desktop-home.png) |

### Menu Page Wireframes

| Size | Screenshot |
| --- | --- |
| Mobile | ![screenshot](documentation/wireframes/mobile-about.png) |
| Tablet | ![screenshot](documentation/wireframes/tablet-about.png) |
| Desktop | ![screenshot](documentation/wireframes/desktop-about.png) |

### Review Page Wireframes

| Size | Screenshot |
| --- | --- |
| Mobile | ![screenshot](documentation/wireframes/mobile-contact.png) |
| Tablet | ![screenshot](documentation/wireframes/tablet-contact.png) |
| Desktop | ![screenshot](documentation/wireframes/desktop-contact.png) |

### Add Review Page Wireframes

| Size | Screenshot |
| --- | --- |
| Mobile | ![screenshot](documentation/wireframes/mobile-contact.png) |
| Tablet | ![screenshot](documentation/wireframes/tablet-contact.png) |
| Desktop | ![screenshot](documentation/wireframes/desktop-contact.png) |

### Edit Review Page Wireframes

| Size | Screenshot |
| --- | --- |
| Mobile | ![screenshot](documentation/wireframes/mobile-contact.png) |
| Tablet | ![screenshot](documentation/wireframes/tablet-contact.png) |
| Desktop | ![screenshot](documentation/wireframes/desktop-contact.png) |


### Cart Page Wireframes

| Size | Screenshot |
| --- | --- |
| Mobile | ![screenshot](documentation/wireframes/mobile-contact.png) |
| Tablet | ![screenshot](documentation/wireframes/tablet-contact.png) |
| Desktop | ![screenshot](documentation/wireframes/desktop-contact.png) |

### Ckeckout Page Wireframes

| Size | Screenshot |
| --- | --- |
| Mobile | ![screenshot](documentation/wireframes/mobile-contact.png) |
| Tablet | ![screenshot](documentation/wireframes/tablet-contact.png) |
| Desktop | ![screenshot](documentation/wireframes/desktop-contact.png) |

## Features

### Existing Features

- **Home Page**

    - This is where the user will be brought to when first entering the website. The user eyes will be drawn to the hero section and order now call to action, from the homepage user has access to the required pages such as menu, reviews, login and signup pages.

![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/screenshots/homepage.png)

- **Home Page Logged In**

    - Same as homepage except now the user can logout of their account and had access the cart which is available for logged in users only.

![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/screenshots/homepage-loggedin.png)

- **Menu Page**

    - Shows menu items available at SoundBurger, burgers, drinks & sides.

![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/screenshots/menu-page.png)

- **Menu Page Logged In**

    - Logged users can see add to cart buttons, when clicked this will add that items to the users cart.

![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/screenshots/menu-page-loggedin.png)

- **Empty Cart Page**

    - If user has not added any items to their cart, the cart will be empty.

![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/screenshots/cart-empty.png)

- **Full Cart Page**

    - Shows all items user has added to their cart including items type, quanity, price, total items and total price. User can also continue to checkout or continue shopping by clicking the corresponding buttons. User can also remove items from cart by pressing red bin buttons beside each item in the cart.

![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/screenshots/cart-full.png)

- **Checkout Page**

    - Similiar to the cart page but instead has an order summary of items added the cart and allows users to enter in shipping address and confirm order.

![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/screenshots/checkout-page.png)

- **Reviews Page**

    - Shows reviews left by users, can leave a review if user has an account.

![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/screenshots/review-page.png)

- **Reviews Page Logged In**

    - User will see option to add a review or edit/delete a review if they have already posted a review.

![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/screenshots/review-page-loggedin.png)

- **Write Review Page**

    - Logged in user can write a review or cancel which will return them to the review page.

![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/screenshots/add-review-page.png)

- **Edit Review Page**

    - If user have prevousily left a review they can edit the review by clicking the edit button on their review. They can then choose to post the updates or cancel the update.

![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/screenshots/edit-review-page.png)

- **Delete Review Confirmation Modal**

    - User can delete prevousily posted review by clicking the delete button the review, a modal will appear confirming user wants to the delete the review, they can confirm delete or cancel so review is not deleted.

![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/screenshots/message-delete.png)

- **Signup Page**

    - New user can signup for an account.

![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/screenshots/signup-page.png)

- **Login Page**

    - Returning users can sign into their accounts.

![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/screenshots/login-page.png)

- **Logout Page**

    - Users can logout of their accounts when they want, signout must confirmed before signout in completed.

![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/screenshots/signout-page.png)

- **Successfully Signed In Message**

    - Message appears when user has successfully signed in, the message will show what username they have signed in with.

![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/screenshots/message-signin.png)

- **Successfully Signed Out Message**

    - Message appears when user has successfully signed out.

![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/screenshots/message-signout.png)

- **Added To Cart Message**

    - Message appears when user has added an item to the cart.

![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/screenshots/message-added.png)

- **Removed From Cart Message**

    - Message appears when user has removed an item from the cart.

![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/screenshots/message-removed.png)

- **Order Complete Message**

    - Message appears when user correctly entered shipping address and clciked confirm order button.

![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/screenshots/message-complete.png)

- **Navbar**

    - Links to all main pages users need access to, logged in user will see the basket and logout link/button, while new users will not see the basket and instead of logout will see signup and login buttons.

![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/screenshots/navbar-full.png)

- **Navbar Mobile**

    - Navbar transforms into a burger menu on mobile and tablet, which expands/closes on click.

![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/screenshots/navbar-mobile.png)

- **Footer**

    - Social media and developer links.

![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/screenshots/footer.png)


### Future Features

- Reset Password
    - User can reset their password.
- Delivery Tracking
    - User can track order on the website, including cooking and delievry updates via website, email & text.
- Delete Account
    - User can delete their own account if needed.
- About Page
    - Page explaing the background and mission of SoundBurger.
- Pickup Option
    - User can choose to pickup order instead of having it delivered.
- Click to reorder
    - User can at a press of button reorder a previously placed order.
- Contact information
    - Add contact information to the site.
- Dark Mode
    - User can switch between normal and dark colour schemes based on preference.

## Tools & Technologies Used

- [HTML](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [CSS](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [Python](https://www.python.org) used as the back-end programming language.
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- [Gitpod](https://gitpod.io) used as a cloud-based IDE for development.
- [Bootstrap](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [Bulma](https://bulma.io/) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [Django](https://www.djangoproject.com) used as the Python framework for the site.
- [PostgreSQL](https://www.postgresql.org) used as the relational database management.
- [ElephantSQL](https://www.elephantsql.com) used as the Postgres database.
- [Heroku](https://www.heroku.com) used for hosting the deployed back-end site.
- [Cloudinary](https://cloudinary.com) used for online static file storage.

## Database Design

Entity Relationship Diagrams (ERD) help to visualize database architecture before creating models.
Understanding the relationships between different tables can save time later in the project.


- [Draw.io](https://draw.io) was used to create the Entity Relationship Diagram

![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/testing/ERD.png)

```python
class Food(models.Model):
    TYPES = (('burger', 'Burger'), ('side', 'Side'), ('drink', 'Drink'))
    food_type = models.CharField(
        choices=TYPES, max_length=10, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    desc = models.TextField()
    price = models.FloatField()
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    item_image = CloudinaryField('image', default='placeholder')
    is_public = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name
```
- Table: **Product**

    | **PK** | **id** (unique) | Type | Notes |
    | --- | --- | --- | --- |
    | **FK** | customer | ForeignKey | FK to imported **User** model |
    | | sku | CharField | |
    | | name | CharField | |
    | | desc | TextField | |
    | | price | FloatField | |
    | | last_modified | DateTimeField| |
    | | created | DateTimeField | |
    | | item_image | ImageField | |
    | | is_public | BooleanField | |

```python
class Order(models.Model):
    customer = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
```
- Table: **Order**

    | **PK** | **id** (unique) | Type | Notes |
    | --- | --- | --- | --- |
    | **FK** | customer | ForeignKey | FK to imported **User** model |
    | | date_ordered | DateField | |
    | | complete | BooleanField | |

```python
class OrderItem(models.Model):
    product = models.ForeignKey(
        Food, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product.name

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
```
- Table: **Product**

    | **PK** | **id** (unique) | Type | Notes |
    | --- | --- | --- | --- |
    | **FK** | product | ForeignKey | FK to **Food** model |
    | **FK** | order | ForeignKey | FK to **Order** model |
    | | quantity | IntegerField | |
    | | date_added | DateField | |
  

```python
class Review(models.Model):
    title = models.CharField(max_length=100, null=False, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posted", null=True)
    content = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.title
```
- Table: **Product**

    | **PK** | **id** (unique) | Type | Notes |
    | --- | --- | --- | --- |
    | **FK** | author | ForeignKey | FK to imported **User** model |
    | | title | CharField | |
    | | content | TextField | |
    | | created | DateTimeField | |
    | | updated | DateTimeField | |
    | | is_public | BooleanField | |

## Agile Development Process

### GitHub Projects

[GitHub Projects](https://github.com/users/ogc1231/projects/4) served as an Agile tool for this project.

Through it, user stories, issues, and milestone tasks were planned, then tracked on a weekly basis using the basic Kanban board.

![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/screenshots/projectboard.PNG)

### GitHub Issues

[GitHub Issues](https://github.com/ogc1231/sound-burger/issues) served as an another Agile tool.
There, I used my own **User Story Template** to manage user stories.

It also helped with milestone iterations.

- [Open Issues](https://github.com/ogc1231/sound-burger/issues)

    ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/screenshots/issues-open.PNG)

- [Closed Issues](https://github.com/ogc1231/sound-burger/issues?q=is%3Aissue+is%3Aclosed)

    ![screenshot](https://github.com/ogc1231/sound-burger/blob/main/documentation/screenshots/issues-closed.PNG)

### MoSCoW Prioritization

I've decomposed my Epics into stories prior to prioritizing and implementing them.
Using this approach, I was able to apply the MoSCow prioritization and labels to my user stories within the Issues tab.

- **Must Have**: guaranteed to be delivered (*max 60% of stories*)
- **Should Have**: adds significant value, but not vital (*the rest ~20% of stories*)
- **Could Have**: has small impact if left out (*20% of stories*)
- **Won't Have**: not a priority for this iteration

## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://soundburger.herokuapp.com).

### ElephantSQL Database

This project uses [ElephantSQL](https://www.elephantsql.com) for the PostgreSQL Database.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:
- Click **Create New Instance** to start a new database.
- Provide a name (this is commonly the name of the project: sound-burger).
- Select the **Tiny Turtle (Free)** plan.
- You can leave the **Tags** blank.
- Select the **Region** and **Data Center** closest to you.
- Once created, click on the new database name, where you can view the database URL and Password.

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.
- For *Primary interest*, you can choose *Programmable Media for image and video API*.
- Optional: *edit your assigned cloud name to something more memorable*.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | user's own value |
| `DATABASE_URL` | user's own value |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `SECRET_KEY` | user's own value |

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:
- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:
- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:
- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace **app_name** with the name of your primary Django app name; the folder where settings.py is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:
- Select **Automatic Deployment** from the Heroku app.

Or:
- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.
- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("CLOUDINARY_URL", "user's own value")
os.environ.setdefault("DATABASE_URL", "user's own value")
os.environ.setdefault("SECRET_KEY", "user's own value")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:
- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/ogc1231/sound-burger) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/ogc1231/sound-burger.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/ogc1231/sound-burger)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/ogc1231/sound-burger)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

## Credits

### Content

| Source | Location | Notes |
| --- | --- | --- |
| [Markdown Builder](https://traveltimn.github.io/markdown-builder) | README and TESTING | tool to help generate the Markdown files |
| [YouTube](https://www.youtube.com/watch?v=OLhqlxHFhWs) | Inspiration | help inspire the aesthetic and design of website |
| [YouTube](https://www.youtube.com/watch?v=UVI1neD6YCc) | Inspiration | help inspire the aesthetic and design of website|
| [YouTube](https://www.youtube.com/watch?v=CqGg_cK41HI&list=PLPSM8rIid1a14qlP9BSnh970pEn40abTZ) | Models | how build models in Django |
| [YouTube](https://www.youtube.com/watch?v=msmtduZfAHo&t=285s) | Models/Views | how to build models and views for food delivery app |
| [YouTube](https://www.youtube.com/watch?v=PgCMKeT2JyY) | shopping cart | how to build a shopping cart in Django |
| [YouTube](https://www.youtube.com/watch?v=PgCMKeT2JyY) | cart quantity icon | design of shopping cart quantity icon |

### Media

| Source | Location | Type | Notes |
| --- | --- | --- | --- |
| [Favicon](https://gauger.io/fonticon/) | entire site | image | favicon on all pages |
| [Hero Image](https://www.freepik.com/free-photo/burger-hamburger-cheeseburger_40824438.htm#query=burger&position=1&from_view=search&track=sph) | homepage | image | hero image  |
| [Hamburger](https://www.freepik.com/premium-photo/hamburger-with-lettuce-tomato-onion-it_44910559.htm#query=hamburger%20burgers&position=21&from_view=search&track=ais) | menu | image | hamburger menu item |
| [Double Hamburger](https://www.freepik.com/premium-photo/hamburger-with-lettuce-it-white-background_45316456.htm#page=2&query=double%20hamburger&position=22&from_view=search&track=ais) | menu  | image | double hamburger menu item |
| [Cheeseburger](https://www.freepik.com/premium-photo/beef-burger-isolated-illustration-generative-ai_38217221.htm#query=burger&position=19&from_view=search&track=sph) | menu  | image | cheeseburger menu item |
| [Double Cheeseburger](https://www.freepik.com/premium-photo/beef-burger-isolated-illustration-generative-ai_38217276.htm#query=burger&position=18&from_view=search&track=sph) | menu | image | double cheeseburger menu item |
| [Coca Cola](https://www.google.com/search?client=firefox-b-d&sxsrf=APwXEddnqMaKW_sTsunp1BpkU7Qleh6e2g:1687273543201&q=coca+cola+can&tbm=isch&sa=X&ved=2ahUKEwiiubnhj9L_AhWlS0EAHVcDDbYQ0pQJegQIDBAB&biw=1536&bih=711&dpr=1.25#imgrc=hm5WpAAVuvRrKM) | menu  | image | coca cola menu item |
| [Sprite](https://www.google.com/search?q=sprite+can&tbm=isch&ved=2ahUKEwjs9K3yjNL_AhV0olwKHZPGAJEQ2-cCegQIABAA&oq=sprite+can&gs_lcp=CgNpbWcQAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BAgjECc6BwgAEIoFEEM6BggAEAcQHjoICAAQCBAHEB5QkBFY-ShghC5oA3AAeACAAXyIAf0HkgEDNy40mAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=Rb2RZKy-FfTE8gKTjYOICQ&bih=711&biw=1519&client=firefox-b-d&hl=en#imgrc=HNt-9-hEQFXLPM) | menu  | image | sprite menu item |
| [Fanta Orange](https://www.google.com/search?q=fanta+can&tbm=isch&ved=2ahUKEwiC7IaDjdL_AhXLTEEAHfj4CTcQ2-cCegQIABAA&oq=fanta+can&gs_lcp=CgNpbWcQAzIHCAAQigUQQzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoECCMQJzoGCAAQBxAeOggIABAIEAcQHjoJCAAQGBCABBAKOgcIABCABBAKUMkHWNAdYI4faANwAHgAgAF7iAH7BpIBAzUuNJgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=aL2RZIKYFsuZhbIP-PGnuAM&bih=711&biw=1519&client=firefox-b-d&hl=en#imgrc=y1jLxovYANeKkM&imgdii=8Byf56u8DMXJgM) | menu | audio | fanta orange menu item |
| [Milkshake](https://www.freepik.com/premium-psd/psd-cappuccino-coffee-with-whipped-cream-chocolate-isolated-alpha-layer_39077355.htm#query=milkshake&position=26&from_view=search&track=sph) | menu  | video | milkshake menu item |
| [Hand Cut Fries](https://www.freepik.com/premium-photo/french-fries_44970832.htm#query=frenchfries&position=32&from_view=search&track=ais?log-in=google) | menu  | image | hand cut fries menu item |
| [Shoestring Fries](https://www.freepik.com/premium-photo/paper-container-french-fries-with-white-paper-bag-that-says-french-fries_41796067.htm#query=sweet%20potato%20fries&position=14&from_view=search&track=ais_ai_generated) | menu  | image | shoestring fries menu item |
| [Nuggets - 6pcs](https://www.freepik.com/premium-photo/nuggets-meal_44996584.htm#page=2&query=mozarella%20stick&position=7&from_view=search&track=ais) | menu  | image | nuggets - 6pcs menu item |


### Acknowledgements

- I would like to thank my Code Institute mentor, [Tim Nelson](https://github.com/TravelTimN) for their support and guidance throughout the development of this project.