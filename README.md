# Video DJ

In build a site in my project where you can checkout, select and view a number of series and episodes.
On this site there are premium episodes for paying customers. There are also 2 episodes per series given for free for every user to see.
Its easy to use for every kind of user. 

## UX
This site is build to quicky be able find and select the serie you want to watch and do nothing else

### User Stories
as a user,:
 - I want to be able to quickly find the serie I want to watch, I have a search button accesable everywhere on the site
 - I want to be able to comment on series and do CRUD operations on them
 - I want to be able to register with clear instructions
 - I don't want distraction of any kind while watching movies
 - I want to be able to buy subscriptions secure

 ## Features
 - Premium, Allows users to buy subscription
 - Register, Allows user to register to the website
 - Videos, Click on an Episode, and enjoy watching
 - Searchbar, Search for anyvideo you want, you can search for name description and genre
 - Add comments to Series, I did not use comments on episodes since they usually spoil the Episode
 - Remove comments form series
 - Edit comments from series
 - Read comments form series
 
 ### Features left to implement
 - Recurring payments, I spent alot of time trying to make this work with no succes

 ## Technologies Used
    arrow==0.17.0
    asgiref==3.3.1
    blessed==1.17.11
    Django==3.1.3
    django-allauth==0.43.0
    django-crispy-forms==1.10.0
    django-picklefield==3.0.1
    django-q==1.3.4
    heroku==0.1.4
    oauthlib==3.1.0
    Pillow==8.0.1
    PyJWT==1.7.1
    python-dateutil==1.5
    python3-openid==3.2.0
    pytz==2020.4
    requests-oauthlib==1.3.0
    sqlparse==0.4.1
    stripe==2.55.1

 ### Testing
    I tested if an Anonymous User can create a subscription
    If an Anonymous User can comment
    If a user can do CRUD operations on comments
    If premium unlocks premium items
    if a payment from a user who is premium already gets extended instead of 30 day reset


 ## Deployment

*-*

 ## Credits

    All Code institute personal which helped me during my project,
    Sorry I dont remmeber all your names :\
    My mentor for always being ready to help me out when im asking( i need to learn to start asking more...)

 ### Content
forms.py in my premium app is from ckz8780
allauth/accounts/base.html is from ckz8780
stripe_elemnts.js is from ckz8780


 ### Media
 All 3 pictures on this website were taken from duckduck go searches for their artist names

 All Videos are taken from youtube from the official arist pages