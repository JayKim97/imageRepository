# Image Repository

Simple Image Repository with image detection

## LIVE DEMO LINK

MAY TAKE UP TO 30 SECONDS FOR HEROKU TO REACTIVATE THE BACKEND
Live demo is missing image detection classifier

https://shopify-frontend.netlify.app/

Signin to checkout all the features  
Please use regular sign up page  
google signup credentials domain verification is in progress

## Feature

Authentication:

- User Login
- User Signup
- Google SignUp (due to security policy on google api currently does not work on live demo)

Images:

- Image Post (AUTH REQUIRED)
- Image Detail (Click on the image)
- Image Download
- Image Edit (AUTH REQUIRED)
- Image Like (AUTH REQUIRED)
- Image content detection

## installation

```bash
gh repo clone JayKim97/shopifyChallenge
cd shopifyChallenge
cd client && npm install
npm start
```

```bash
cd shopifyChallenge
cd server && npm install
npm start
```

server/.env FILE must be populated for the application to work  
template in .env-example
