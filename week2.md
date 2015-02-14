# Week 2 - Inspector, CSS and Layouts
After Zoe's HTML/CSS workshop, let's dig deeper into what you can do with CSS and make a few layouts.

Quick announcement: I'm planning on splitting our time together in half. 2 hours of demos/new information, 2 hours of help on any interactive work you want to do in your studio classes.

### What You'll Learn
* How to use the Inspector
* How to use CSS floats and the mysterious clearfix.
* How to make your own layouts

## Today's Session

### Web Inspector

The web inspector is avaiable in Chrome, Safari, or Firefox, but we'll be focusing on the Chrome version.

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
- Look at resources
- Inspect cookies
- Investigate load times

For more information on the inspector:
- [Video tutorial](http://discover-devtools.codeschool.com/)
- [Text tutorial](http://code.tutsplus.com/tutorials/chrome-dev-tools-markup-and-style--net-27149)
- [Official Chrome page](https://developer.chrome.com/devtools)

### Review
- On the CSS Box Model: [Box Model Ninja](http://codewithme.us/exercises/box-model-ninja.html)


### Clearfix

When we start using the `float` attribute in CSS, we'll run into some problems. Essentially, `float` allows elements to stick out of their parent elements, and if we don't want that behavoir, we have to institute a "clearfix."
- Read more about [how float actually works](http://complexspiral.com/publications/containing-floats/)


There are many, many ways to institute clearfix. My current favorite is [by Nicolas Gallagher](http://nicolasgallagher.com/micro-clearfix-hack/).

```
.cf:before,
.cf:after {
    content: " ";
    display: table;
}

.cf:after {
    clear: both;
}
```

### Great Portfolio Layouts

http://charlottetang.com/
http://bjoernmeier.com/
http://lenagroeger.com/
http://shancarter.com/
http://bost.ocks.org/mike/






