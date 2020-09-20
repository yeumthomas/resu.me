# resu.me

https://www.youtube.com/watch?v=5gesqc56Xag

## Inspiration
The socioeconomic disparity present in the world we live in has become increasingly evident, now more than ever. Having witnessed the social effects, and more importantly, the financial setbacks of a global pandemic on both a personal and widespread scale, we were driven to build a platform that would serve those in need: resu.me.

## What it does
resu.me is a platform that provides those with few resources or little academic background with the tools to build a successful career. resu.me custom tailors each user's experience to their individual skills as well as aspirations, building a personal portfolio of suggested courses and potential job opportunities. Beginning to work towards a meaningful career can be very overwhelming, especially for those with little experience or guidance, and resu.me serves to make the entire process seamless.

## How we built it
resu.me is built with a Vue.js frontend that interfaces with two separate API servers in the backend. One server is built with NodeJS/Express, communicates with MongoDB, and manages most of the site administration, such as authentication and database operations. The other server is built in Python with the Flask microframework, and focuses exclusively on web scraping. After receiving those results, the frontend communicates with the Node server for any remaining tasks, such as saving bookmarked courses and jobs to MongoDB and updating the profile accordingly.

## Challenges we ran into
A concern that we had as we conceptualized and began working on the course and job scraper was latency issues. Initially, in order to display a significant amount of results for both course options and job opportunities, we had relatively long wait times. We ultimately addressed this by implementing a parallel programming model, and ran the scraping functions simultaneously on different threads; this effectively doubled the efficiency of our scraping process.

## What's next for resu.me
resu.me still has tons of room for improvement as a platform. We'd like to implement a wider reach, and the capability of providing users with various types of resources, ranging from useful articles to event notices to mentor connections. We'd also plan to focus on fine-tuning our suggestions to each user even more, ultimately just seeking to create a platform that can truly inspire and create change.

