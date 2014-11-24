# Instructions
### app.py
To run the application: where 02108 can be any zipcode
```bash
python app.py 02108
```
Required python modules
* lxml
* requests
* datetime 

### pool.py
To run the multithreaded test:
```bash
python pool.py 02108
```
Required python modules
* lxml
* requests
* datetime 
* multiprocessing 

The modules can be installed via pip
```
pip install module_name
```
# Project Description
The current app.py is setup in three main classes; MovieParser, IMDBParser, and Parser. My design going in was to make it as modular as possible so that pieces could be replaced if needed.

The Parser is the lowest level, it handles general requests parsing requests and has no Movie/IMDB specific code. It accepts URL templates, variables for URL, selector to find content on the page, and a callback incase the final values need some extra massaging. It could be used separate from the rest of this program.

IMDBParser is a child class of parser and also has some IMDB specific methods to request parsing specific information and registering the requests to get that information. At this is the level at which everything IMDB should stay, Higher levels shouldn’t care where info is coming from only to choose and lower levels shouldn’t depend on it.

The MovieParser is what creates the actual Movie and Actor objects, it knows what methods to call to get that data and bundles it up into objects. In its constructor it takes in what type of parser it will be using. The app is the highest level, Getting data out is as simple as creating a new MovieParser setting the Parser to IMDBParser and running GetMovies with your zipcode as a parameter.

This app was designed originally with feasibility to update in mind in case a service goes down or URL changes. The modifications to fix that and get it up and running again would be minimal. Since this app is all about making requests I designed it with the ability to cache the contents of a request for later use. If another request is made to the same URL but has different parsing requirements it will use the cached version instead of making a duplicate request.

The one downside to the app currently is the time it takes to retrieve the data (forever). The current method is requesting a URL and scraping the page for the correct info. This it highly locked into how the page is laid out and format of the content. Since each actors age is on its own page a lot of requests are needed to get all the information for just one movie. Along with the request output size the app only runs on a single thread, it can only go through a list and request one URL at a time.

A better method going forward would be to find the API endpoint that it uses to retrieve its data (if available) so the data returned would be much less. Another method to speed things along would be to use multithreading. Instead of running one request at a time launch multiple requests in parallel to a thread pool and wait for the results.
I have started implementing this in pool.py though it worked so well that IMDB blocked me for spamming them with requests. The overall speed increase was massive, in the time it use to take to just get the data for one movie I would have the data for all of them (about 36). Going forward there should be some speed limiting put in.

