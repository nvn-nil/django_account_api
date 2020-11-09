=====
Accounts
=====

This is a Django app to enable toke authentication end-points for a django project. This app would expose
rest api endpoints for login, logout and registering a user.

Was a part of a higher django-react application and separated out for code reuse and to help user bootstrap
and impement auth as an extension.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "accounts" and "knox" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'knox',
        'polls',
    ]

2. Include the accounts URLconf in your project urls.py like this::

    path('board', include('board.urls')),
    path('', include('accounts.urls')),
    path('', include('another.urls')),

note: accounts urls are internally prefixed with 'api', keep this line above your other 'api' paths
    
    path('', include('accounts.urls')),
    path('api', include('other_api.urls')),

3. Run ``python manage.py migrate`` to create the accounts models and knox migrations (for tokens, etc).

4. Start the development server and now you can access the account endpoints.


=====
API
=====

User register
-----------

Request

url: /api/auth/register
method: POST
content-type: application/json
body:
{
    "username": "userNameHere",
    "first_name": "Brad",
    "last_name": "NoChad",
    "email": "brad@chad.com",
    "password": "superstrongpassword"
}

Response

content-type: application/json
body:
{
    "user": {
        "id": 1,
        "username": "userNameHere",
        "email": "brad@chad.com"
    },
    "token": "bc1aksjna2fba56be605d324a59f531c47dcoij3bcc162aksjdaskdljalskd48"
}

Note: Registration returns token so the user can be validated immediately if need be


User Login
-----------

Request

url: /api/auth/register
method: POST
content-type: application/json
body:
{
	"username": "userNameHere",
	"password": "superstrongpassword"
}

Response

content-type: application/json
body:
{
    "user": {
        "id": 1,
        "username": "userNameHere",
        "email": "brad@chad.com"
    },
    "token": "bc1aksjna2fba56be605d324a59f531c47dcoij3bcc162aksjdaskdljalskd48"
}


User Information
-----------

Request

url: /api/auth/user
method: GET
headers: {
    Authorization: "Token bc1aksjna2fba56be605d324a59f531c47dcoij3bcc162aksjdaskdljalskd48"
}

Response

content-type: application/json
body:
{
  "id": 1,
  "username": "userNameHere",
  "email": "brad@chad.com"
}


User Logout
-----------

Request

url: /api/auth/logout
method: POST
headers: {
    Authorization: "Token bc1aksjna2fba56be605d324a59f531c47dcoij3bcc162aksjdaskdljalskd48"
}

Response

No Content

Note: This will invalidate the sent in the header so subsequent call to '/api/auth/user' using
this token will return a '404 Unauthorized' response with body:
{
  "detail": "Invalid token."
}
