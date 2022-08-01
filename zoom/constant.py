# This file contains all the constant variables which are useful through application

# Zoom Authentication url Endpoint
ZOOM_AUTH_URL="https://zoom.us/oauth/authorize?response_type=code&client_id={0}&redirect_uri={1}"

# Zoom Access token url Endpoint
ZOOM_ACCESS_TOKEN_URL="https://zoom.us/oauth/token?grant_type=authorization_code&code={0}&redirect_uri={1}"

# Zoom Get details of Current user Endpoint url
ZOOM_GET_USER_ENDPOINT="https://api.zoom.us/v2/users/me"

# Zoom Create a meeting Endpoint url
ZOOM_CREATE_MEETING_ENDPOINT="https://api.zoom.us/v2/users/me/meetings"