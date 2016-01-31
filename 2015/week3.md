# Week 3 - CSS Floats, Layout

### What You'll Learn
* How to use CSS floats and the mysterious clearfix.
* How to make your own layouts

## Today's Session

### CSS Floats

How any HTML element is able to be "floated" to the left or right of something else. What is a `float`? The ability to:

- Moving an element to the left or right of the main text:
- Moving elements side-by-side.

There are only two options: `float: left;` and `float:right;`.

In-class demos: [Just floats](http://codepen.io/anon/pen/Byxzzx) and [Cymbols](http://codepen.io/anon/pen/gbzMLv).

Javascript libraries that help do crazy positioning things: [Masonry](http://masonry.desandro.com/) and [Isotope](http://isotope.metafizzy.co/). [Superfluous interactivity example.](http://www.propublica.org/nerds/item/why-develop-in-the-newsroom)

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

Once you add this to your CSS, you can just add the class "cf" to any element that needs a clearfix, like so:

```
<div class="container cf">
    <img src="example.jpg" style="float:left;">
    <img src="example.jpg" style="float:left;">
</div>
```

### Example Portfolio Layouts
Try to re-create any of these layouts from scratch, using your own name and content. Feel free to pick your own fonts and colors, but the layouts must be the same.

- http://lenagroeger.com/
- http://shancarter.com/
- http://bost.ocks.org/mike/
