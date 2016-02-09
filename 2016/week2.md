# Week 1 - HTML/CSS

### What You'll Learn
* Where to write code
* How to write basic HTML tags
* How to write basic CSS
* How to structure a basic website
* If we have time: Finishing up Github

## Today's Session

### Where to Write Code
* [Codepen](http://codepen.io/) or [JSFiddle](https://jsfiddle.net)
  * Always hosted online
  * Cannot directly work with Github
* [Sublime Text](https://www.sublimetext.com/)
  * For use on your computer only

### HTML

Concepts:
* Opening and closing tags
* What happens if you forget to close a tag

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

Exercise:
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

### Basic CSS
[Main Tutorial from Code with me](http://codewithme.us/austin/main-curriculum/04-css-intro.html#/)

Concepts:
* What can CSS do
* How CSS rules are written
* Thought process when writing CSS

Exercise:
* Using your HTML from before, add CSS styles to it such you change the:
  * color
  * font-family
  * font-size
* On your own, look up how to do the following in CSS, and add it to your HTML file as well:
  * underline text
  * bold text
  * italicize text
* Going back to the Onion article [you formatted earlier](https://jsfiddle.net/kJHdt/86/), do the following using CSS:
  * Make the main headline dark green.
  * Use the font family "Georgia" for the main headline and the subheadline.
  * Center the text of the main headline and the subheadline.
  * Make the paragraphs have a line height of 19 pixels.
  * Remove the underline from the links.
  * Make the "You might also like" label all uppercase.
  * Bonus: Make an underline appear when you hover over a link.

### CSS Classes

Concepts:
* WTF do you do when you want to do more with your styles?
* CSS classes are easy. Just name HTML tags anything you want: `<p class="byline"></p>`
* Multiple classes can go on one tag: `<p class="byline muted"></p>`
* More specific CSS overwrites generic CSS

Exercise:
* Pick any past HTML page and add a CSS class and see if it works.
* Take a look at [this image](mars.png). Now, here's the [HTML code behind it](https://jsfiddle.net/wwc6n77p/1/). Can you use CSS classes to make it look the same as the image?

### File structure and getting HTML/CSS to work on your computer

Concepts:
* How to use `<style>` to link to your CSS in your HTML file

### Github

__How does Github work exactly?__

Four basic commands to sync the code on our computer to the repository hosted on Github

```
git status
git add .
git commit -m "Updated design"`
git push
```

Creating 'branches' and using a branch called 'gh-pages' to create our own website

```
git branch
git branch gh-pages
git checkout gh-pages
git push origin gh-pages
```

What else is possible? [Github's excellent cheatsheet](https://training.github.com/kit/downloads/github-git-cheat-sheet.pdf). They also have a [tutorial](https://try.github.io).
