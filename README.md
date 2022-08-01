# Zoom create instant meeting
>The instant meeting creater without going to zoom app

## Step 1
> Clone the repo

```
git clone https://github.com/MadhabaPatra/django-zoo-app.git
```

## Step 2

```
cd django-zoo-app
```

## Step 3
1. Go to zoo>settings.py
2. Refer this [doc](https://marketplace.zoom.us/docs/guides/build/oauth-app/) and Create an OAuth app on [zoom marketplace](https://marketplace.zoom.us/develop/create)

3. Fill the values with your client details
```
CLIENT_ID="Your client id"
CLIENT_SECRET="Your client secret"
CLIENT_REDIRECT="http://127.0.0.1:8000/callback"
```

## Step 4
> run the command
```
python manage.py runserver
```

## Finished
> Assisted by [Ashish Kumar Sahoo](mailto:a@param.ai)