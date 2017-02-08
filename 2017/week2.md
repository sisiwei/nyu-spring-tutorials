# Week 2

## Today's Session

### The Internet!

* URLs! Like `https://github.com/mtigas/nyu-spring-tutorials/`. Your browser gets a lot of information out of this:
  * **Protocols** (`https`, `http`).  
    - How is my browser going to communicate?
  * **Domain names** (`github.com`).  
    - What server is my browser communicating with?  
    - These get looked up in DNS (the "domain name system") and get turned into an IP address, which is the server your browser tries to connect to. Because nobody's going to remember to type in something like `http://54.82.124.250`.
  * **Paths** (`/mtigas/nyu-spring-tutorials/`).  
    - OK, what page is my browser that server asking for?

(Showing off difference between HTTP and HTTPS with [Wireshark](https://www.wireshark.org); you don't need to follow along. And I'll come back to this in a later week when we do a cybersecurity workshop.)

### Publishing with GitHub Pages

We're going to use GitHub Pages https://pages.github.com/ to put some HTML pages on the internet!

* We'll make a repo named `week2` in the GitHub Desktop app. (If you're on one of the lab computers, do it in the GitHub website; make sure you select "Initialize this repository with a README.")
* In this `week2` repo folder, create a file called `index.html`.
* From the GitHub Desktop app, commit this file and click "Publish" on the upper-right. (Reminder: you have to be on the "Uncommitted Changes" tab, not the "History" tab.)
* Then, go to your repo in the GitHub website. (From the app you can get to it by right-clicking your repo and clicking "View on GitHub".) Then go into the Settings tab.
* In the "GitHub Pages" section, see the "Source" dropdown. Set it to `master branch` and hit save.
* Refresh the settings page until the GitHub Pages section says "Your site is published at _link_"

### Other ways to publish your HTML on the web

* FTP, SFTP, SCP
  * You have an account with a service and you use these protocols to copy your files to their server.
  * You use an app like [Fetch](http://fetchsoftworks.com/) (Mac; [NYU download here](http://www.nyu.edu/its/software/#fetch)) or [WinSCP](http://winscp.net/eng/index.php) (Windows)or [CyberDuck](https://cyberduck.io/).

    Once you're logged in, it works like another Finder/Explorer; you can create folders, move and delete files, etc. You can copy files to your space by dragging them into the app window.
  * Theoretically there's some NYU space you maybe get access to, but I haven't tried it myself.
    * https://www.nyu.edu/employees/resources-and-services/media-and-communications/digital-communications/web-guide/web-site-development/tutorials/ssh-file-transfer-protocol.html
    * https://www.nyu.edu/employees/resources-and-services/media-and-communications/digital-communications/web-guide/web-site-development/tutorials/ssh-file-transfer-protocol/connect-to-i4-sftp.html

### HTML refresher

Basic HTML tags:
* `<html>`
* `<head>`
* `<body>`
* `<title>`
* `<h1>`
* `<p>`
* `<img>`
* `<a>`
* `<ul>`
* `<!-- Comments -->`

Basic HTML template:
```html
<html>
  <head>
    <title></title>
  </head>
  <body>
    Hello there!
  </body>
</html>
```

Exercises:
* Create a basic HTML file and use the following tags:
  * `<h1>`
  * `<h2>`
  * `<h3>`
  * `<p>`
  * `<img>`
  * `<a>`
  * `<ul>`
  * `<!-- Comments -->`
* Go to this JSFiddle and follow the instructions to format the page: https://jsfiddle.net/kJHdt/86/
* Something's wrong with this code. Can you fix it? https://jsfiddle.net/dVYtK/20/

### Web Inspector

Every modern browser comes with an Inspector view, but we'll be focusing on the Chrome version.

#### Why use it?
- Debug your code
- Test your code
- Test performance

#### What are some things can we do in it?
- Locate elements
    + Highlight both code and what it creates on the page
    + Scroll to view elements
    + Ctrl+F within the inspector

- DOM modification
    + Change text
    + Change tags
    + Change attributes
    + Delete anything

- Edit CSS for testing purposes
    + Stylesheet styles
    + Hover styles
    + Computed styles
    + Built-in color selector
    + Add any new styles on the fly
    + Verify/check CSS hierarchy

- Emulate different screen sizes
    + Mobile, tablet and laptop testing

- Look at what resources a page is loading
- Inspect cookies
- Investigate load times

### Resources

- [W3Schools HTML reference & tutorials](http://www.w3schools.com/html/default.asp)

- Slides: [How Websites Work](https://projects.propublica.org/graphics/images/data-institute/presentations/how-websites-work.pdf)
- Slides: [HTML](https://projects.propublica.org/graphics/images/data-institute/presentations/html.pdf)
- [HTML Tutorial from Code with me](http://codewithme.us/austin/main-curriculum/04-css-intro.html#/)

**Inspector**

- [Video tutorial](http://discover-devtools.codeschool.com/)
- [Text tutorial](http://code.tutsplus.com/tutorials/chrome-dev-tools-markup-and-style--net-27149)
- [Official Chrome page](https://developer.chrome.com/devtools)
