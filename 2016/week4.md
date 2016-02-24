# Week 4 - CSS Floats, Layout

### What You'll Learn
* How to use CSS floats and the mysterious clearfix.
* How to make your own layouts

## Today's Session

### Using Divs

Last week's exercise drawing boxes is exactly how designers think about making websites. When you need a box, you can use one of the HTML tags you've already learned (p for paragraphs, img for images). But if you need a box to contain other elements, use `<div></div>`.

`div` just stands for divider or division. It's a tool to help you contain your HTML.

### CSS Floats

How any HTML element is able to be "floated" to the left or right of something else. What is a `float`? The ability to:

- Moving an element to the left or right of the main text:
- Moving elements side-by-side.

There are only two options: `float: left;` and `float:right;`.

Let's start with a demo using our [CIA example from two weeks ago](http://codepen.io/sisiwei/pen/Veoxjz?editors=1100). I'm going to:

- Float the image to the right.
- Float the image, with a new caption, to the right.
- What if I want the image and caption to have a nice border, padding, and margin?

Exercise: Here's a [clean copy of the CIA example](http://codepen.io/sisiwei/pen/YwmLQY?editors=1100). Try doing the same thing without looking at my code.

<!-- In-class demos: [Just floats](http://codepen.io/anon/pen/Byxzzx) and [Cymbols](http://codepen.io/anon/pen/gbzMLv). -->

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

### Layout

When we want to get more complicated with layouts, we are able to really get in the weeds.

For example, let's say we want to label [different parts of an image](http://codepen.io/sisiwei/pen/yemjMB?editors=1100). How can we tell the labels to be in the right place?

We'll cover: `position: absolute` and `position: relative` and how they relate to each other.

Exercise: http://codepen.io/sisiwei/pen/OMKZNE?editors=1000

#### Extra things

Javascript libraries that help do crazy positioning things: [Masonry](http://masonry.desandro.com/) and [Isotope](http://isotope.metafizzy.co/). [Superfluous interactivity example.](http://www.propublica.org/nerds/item/why-develop-in-the-newsroom)

### Example Portfolio Layouts
Try to re-create any of these layouts from scratch, using your own name and content. Feel free to pick your own fonts and colors, but the layouts must be the same.

- http://lenagroeger.com/
- http://shancarter.com/
- http://bost.ocks.org/mike/
