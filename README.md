# You First Wagtail Website

Simple introduction to [Wagtail](https://wagtail.io) based on the [Wagtail tutorial](https://docs.wagtail.io/en/stable/getting_started/tutorial.html).


## Step 1: Setup

Normally you would `pip install wagtail` and run `wagtail start mysite`, but this repo already provides some
demo code. So instead, run:

```
git clone https://github.com/vsalvino/wagtail-tutorial.git
cd wagtail-tutorial/
pip install -r requirements.txt
```

Once that is done, set up wagtail:

```
python manage.py migrate
python manage.py createsuperuser
```

Now you will have a database (`db.sqlite3`) and an admin account. It's finally time to run wagtail:

```
python manage.py runserver
```

Check out your new site in the browser at http://localhost:8000.

To log in to the admin, go to: http://localhost:8000/admin/.


## Step 2: Making a home page

Ok, so our wagtail site is now up and running. But it's pretty useless as-is. Let's add some content
to the home page. To do that, we first have to define some content fields on our page model.

In `home/models.py`, remove the first `#` on each line between STEP 2 and END STEP 2:

``` python
### STEP 2 ###
# ...
# ...
### END STEP 2 ###
```

We have just added a rich text editor called `body` to our home page model. We have also instructed
wagtail to show that `body` field in the `content_panels` in the editing interface. And finally,
we are telling this model to use a specific HTML template.

For these changes to take effect, run:

```
python manage.py makemigrations
python manage.py migrate
```

And now start up `runserver` again to load the new code:

```
python manage.py runserver
```

Now navigate to the HomePage in the wagtail admin, and edit it to fill out our new body field.


## Step 3: Adding some blog pages

Alright, we have a bare-bones home page. But what would any tutorial be without a blog? Let's make
some blog posts that are a bit more robust.

In `home/models.py`, remove the first `#` on each line between STEP 3 and END STEP 3:

``` python
### STEP 3 ###
# ...
# ...
### END STEP 3 ###
```

We have now created a new model, similar to the HomePage model, but with some different fields
and a different HTML template. In addition to a rich text body, our blog page has a date, text
caption, and an image.

Inside of our blog page HTML template, we are going to render all four of those fields with a
little bit of structure.

For these changes to take effect, run:

```
python manage.py makemigrations
python manage.py migrate
```

And now start up `runserver` again to load the new code:

```
python manage.py runserver
```

Now go to the admin, navigate to the home page, and click "create child page" to add a new blog
page. Pages follow a tree structure in wagtail, so the blog page should live below the HomePage.


## Step 4: Show a list of blog pages on the home page

Now that we have some blog pages, it would be nice to actually be able to navigate to them.
Let's show a preview of each blog page on the home page.

In `home/models.py`, remove the first `#` on each line between STEP 4 and END STEP 4:

``` python
### STEP 4 ###
# ...
# ...
### END STEP 4 ###
```

We have now just over-ridden the default `get_context()` method of the HomePage.
The `get_context()` method is called on every page load to determine what data to
pass to the HTML template. We are altering it to include a list of all published
blog pages ordered by date from newest to oldest.

Now that our HTML template will have access to a list of blog pages called `blogpages`,
let's modify it to render those in a preview.

In `home/templates/home/my_homepage.html`, remove the following lines:

```
<!-- {% comment STEP 4 %}
```

and

```
{% endcomment %} -->
```

Now the code in between those comment blocks will render a preview of our blog pages.


## Step 5: Make it shiny

You'll notice that our templates (`my_homepage.html` and `my_blogpage.html`) both have
a line at the top: `{% extends "base.html" %}`. This base HTML template always gets rendered,
and encapsulates each template inside the "content" block. Since `base.html` is shared,
this is an ideal place to put our CSS and JavaScript.

In `templates/base.html`, you'll see that it is already contains much boilerplate code,
and references a static file `css/mysite.css`.

In `mysite/static/css/mysite.css`, remove the following lines:

```
/*** STEP 5
```

and

```
END STEP 5 ***/
```

Now the code in between those comments will add some styling to our page. Some of the CSS
classes here should look familiar from our `my_homepage.html` and `my_blogpage.html` templates.

Load up the page in your browser, and it should look much prettier now (or uglier - remember design
is not a standard but a matter of opinion)


# So you like wagtail! What next?

There are many wagtail resources out there, including the friendly wagtail slack group.
Best place to start is https://wagtail.io.

If you find yourself enjoying wagtail, but feel like defining all the models and templates
is a lot of tedium, you're not alone. Check out [CodeRed CMS](https://github.com/coderedcorp/coderedcms),
which is essentially wagtail on steroids with tons of features that work out of the box for
building marketing-centric websites.