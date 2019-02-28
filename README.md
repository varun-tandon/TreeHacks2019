# TreeHacks2019

## Inspiration

We were sick and tired of Congress listening to money and lobbyists over their own constiuents. It was almost like Congress didn't even want to be contacted. Of the 535 Congresspersons, only approximately 50 had actual email addresses. 

How do you contact the rest? 

Fax. 

When's the last time you sent a fax message???

Our app allows users to quickly fax or email their representative; however, it goes beyond this functionality. We wanted to ensure that Congress was not inundated with paper, instead taking advantage of numerous APIs and data aggregation tools to give Congress a concise, yet powerful snapshot of their constituency. Moreover, by implementing a visually pleasing user interface and plans for a more social component to our app, we hope to appeal to a younger audience, promoting political engagement among the youth. 

## What it does

At its most basic level, it allows constituents to easily like or dislike potential acts of legislation and or their representatives. With a clean UI, it makes it simple and easy for people of all ages to engage in politics and allow their voices to be heard. 

Equally important though, InSession delivers a simple, elegant, and powerful data aggregation and presentation for representatives to be more informed of their constituents’s beliefs. Not only can users of the application vote and downvote bills or legislators, but using Azure Text and the Twitter API, we scan through the most recent tweets and analyze text sentiment to monitor current popular opinion on the legislators. This information is readily accessible through infographics that are attached to faxes and links on the web HTML.

## How we built it

We are all beginners to developing complete web applications, but our team had some familiarity with Java, Python, and JavaScript from CS classes. After some research, we settled on Flask (Python module) as our backend system, with client-side rendering with JS, HTML, CSS. The Web framework we used for styling our application was Ionic. 

### Backend: 

User data is stored in a PostgreSQL database facilitated by SQLAlchemy ORM. We took care to ensure user data was protected against potential data breaches by implementing the hashlib and uuid Python modules to encrypt passwords and other sensitive information in SHA-512. 

Flask enabled us to create an array of internal API endpoints, including ones to: 

1. Handle login and sign up flows (including anti-bot verification through Twilio)
2. Access data about US Senators, Representatives, and bills through the Phone2Action and ProPublica APIs
3. Handle faxing to representatives (Twilio)
4. Send emails to representatives (SendGrid)
5. Analyze User Sentiment (Microsoft Azure)
6. Scrape initial data from Twitter searches (Twitter API)
7. Deployment to Azure (Unimplemented)

### Frontend
1) CSS and Responsive JS powered by Ionic
2) HTML templating rendered via the Python backend
3) AJAX POST and GET requests through JQuery

## Challenges we ran into
Time limitations. 

A large chunk of our initial time was devoted to reading documentation pages for Flask, Microsoft Azure, and learning about web programming languages. At the beginning, the team members who were strong in Python began working on Python, and the team members who were strong in Web began working on web, and while we were able to develop a lot of functionality on both the backend and frontend sides, we did not have enough time to link the two together. Ultimately, a lot of the features we had initially envisioned were sidelined or left in the codebase as unimplemented or not fully implemented. 
## Accomplishments that we're proud of
We're incredibly proud of how we were able to setup a PostgreSQL database, Flask backend, and develop user interfaces using Web programming languages. We were also impressed with the implementation of API endpoints and Python modules to send fax messages to Congresspersons, scrape data from Twitter and conduct sentiment analysis, protection against spam and bots through text message verification, and data security through password hashing. 

## What we learned

Connor: I learned a great deal about full stack development through this experience. It was incredibly challenging to understand how we would be able to test our Flask app locally, setup a database on our machines, and link our frontend to our backend. 

Varun: My biggest learnings from this experience related to using SQLAlchemy and Flask to store data in our servers, as well as to manipulate POST and GET requests on our Python backend through the requests module and JavaScript frontend through JQuery Ajax. It was also rewarding to learn about deploying to Microsoft Azure, although we were unable to succesfully do that in the end. 

Roberto: I had never worked with Python before, with all of my previous experience having been in JavaScript (without any HTML), so it was really cool to adapt the skills I had learned in my Intro CS class at Stanford to a new programming language. Moreover, it was really interesting learning about POST and GET requests, and using APIs in this way. 

Ryan: For me, the biggest thing I learned was how to develop UIs in HTML, CSS, and JS. Although I had never worked with these before, I was excited to learn and it was incredibly rewarding to see my code represented in visuals on the site. Manipulating the Ionic components was at times tricky, but thanks to many Youtube videos and StackOverflow forums, I was able to accomplish what I wanted. 

## What's next for InSession
We have a lot of really cool features sitting under the hood in our backend, waiting to be linked to our frontend, and to be accessible to our users. In the coming weeks, we are excited to continue working on this project to bring it to a state where we can begin to acquire users and slowly transition away from the existing sample data scraped from Twitter. 

Here are some of the things you can look forward to seeing from us very soon:
1) Full deployment to Azure
2) Dynamic charts pages powered by Plotly
3) Full integration of our existing API endpoints with currently unused HTML templates
4) General bug and security fixes (boring, but necessary)
5) Implenentation of a social feature, involving a political engagement score, and the ability for users to view the political engagement of their contacts

