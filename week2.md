# Week 2 - Inspector, CSS and Layouts
After Zoe's HTML/CSS workshop, let's dig deeper into what you can do with CSS and make a few layouts.

Quick announcement: I'm planning on splitting our time together in half. 2 hours of demos/new information, 2 hours of help on any interactive work you want to do in your studio classes.

### What You'll Learn
* How to use the Web Inspector
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

### HTML/CSS Review

- Simple HTML review: 
    + Create a new HTML file and copy: http://jsfiddle.net/kJHdt/86/light/
    + Use HTML to markup the article

- CSS review:
    + Setup an external CSS stylesheet
    + Style your HTML with the rules below:
        + Make the main headline dark green.
        + Use the font family "Georgia" for the main headline and the subheadline.
        + Center the text of the main headline and the subheadline.
        + Make the paragraphs have a line height of 19 pixels.
        + Remove the underline from the links.
        + Make the "You might also like" label all uppercase.
        + Make an underline appear when you hover over a link. 

- CSS Box Model
    + Demo: http://sports.espn.go.com/espn/grantland/story/_/id/9175394/out-great-alone
    + Exercise: Let's draw some boxes
        * Pick any news website you'd like
        * Print it out
        * Physically draw the boxes on top
    + On the CSS Box Model: [Box Model Ninja](http://codewithme.us/exercises/box-model-ninja.html)

### CSS Floats


<img src="http://codewithme.us/austin/main-curriculum/images/presentations/combined-layout/7_webfloat.png">

<img src="http://codewithme.us/images/exercises/drought-maps/drought-final.png">
Exercise: http://jsfiddle.net/qt77z/2/light/

#### Clearfix

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

### Example Portfolio Layouts

http://lenagroeger.com/
http://shancarter.com/
http://bost.ocks.org/mike/






