This is a very simple combination of a GAE Standard app and a Cloud Run container to test authentication.
GAE app is a simple Flask app that returns the code [shown here](https://developers.google.com/identity/sign-in/web/)
to generate a token.

This guide assumes 2 things:
1. You're project owner
1. Using Python 3.7

Steps to follow:
1. Set environment variable $RUNPROJECTID to the project you're deploying this on.  
`$ export RUNPROJECTID=[PROJECTID]`
1. Follow steps on this page: [Using Google Sign-in](https://cloud.google.com/run/docs/authenticating/end-users#using_google_sign-in)
 to set up a OAuth Client ID. (Steps 1 & 2 there)
1. Add the appspot URL to the `Authorized JavaScript Origins` in the OAuth Client ID settings:    
`http://[PROJECTID]`
1. Put the generated Client ID in main.py
1. Deploy the app (`-q` flag will do a silent deploy):  
`gcloud app deploy -q --project $RUNPROJECTID`
1. Build the Cloud Run image:  
`gcloud builds submit --tag gcr.io/$RUNPROJECTID/headers`
1. Deploy the image to Cloud Run.  
`gcloud beta run deploy --image gcr.io/$RUNPROJECTID/headers --platform managed --no-allow-unauthenticated`
1. Visit the GAE app to get a token. It's in the dev console after going through the OAuth2.0 login flow.
1. Set an environment variable for the token:  
`$ export RUNTOKEN=[TOKEN]`
1. curl the Cloud Run endpoint with the token:  
`curl -H "Authorization: Bearer $RUNTOKEN" -i  https://[RUNURL]/`      

Curl the tokeninfo endpoint:  
`curl https://oauth2.googleapis.com/tokeninfo?id_token=$RUNTOKEN`
