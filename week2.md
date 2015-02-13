# Week 2 - CSS and Layouts
After Zoe's HTML/CSS workshop, let's dig deeper into what you can do with CSS and make a few layouts.

### What You'll Learn
* How to use the Inspector
* How to use CSS floats and the mysterious clearfix.
* How to make your own layouts

## Today's Session


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







