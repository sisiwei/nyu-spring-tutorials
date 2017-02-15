# Week 3

* HTML/CSS: Page Layout & Mobile Layout
* HTML/CSS: Basic Data Visualization

---

### HTML/CSS: Page Layout

**Block tags vs inline tags in HTML**

Tags like `<div>` `<p>` `<h1>` `<h2>` are "blocks", which always start a new line and fill up the width of whatever container they're in (unless you give it a width).

* Example: https://jsfiddle.net/mtigas/018xp9hn/2/  
  * _Instead of filling the width of the page, the `<div>` is 300px wide, and the `<p>` tags become 300px wide._

Tags like `<span>` `<em>` `<strong>` `<i>` `<b>` `<a>` `<img>` are "inline" tags, which don't start a new line and don't fill the width of the space they're in.

* Example: https://jsfiddle.net/mtigas/gg9a0dp7/1/

---

**The Box Model**

Block tags are just boxes! In CSS, they've got the following properties:
* `width` / `height`
* `border`
* `margin`
* `padding`
* `float`

Some examples:

https://jsfiddle.net/mtigas/1199n2kc/1/
* `width` and `height` are basically "how much space does the content inside get?"
* `margin`: "I need to leave some space in the room that I'm given"
* `padding`: "the content inside here needs some space"

https://jsfiddle.net/mtigas/22tm3Lok/1/
* Remember that block tags always flow down to a new line!

This is where `float` comes in  
https://jsfiddle.net/mtigas/22tm3Lok/2/


One last thing: "clearing" floats.  
https://jsfiddle.net/mtigas/22tm3Lok/3/

You can use the `clear: left;` property to say "ignore the most recent left float, I want this block tag to go down to a new line".  
https://jsfiddle.net/mtigas/22tm3Lok/4/


Real uses for floats:
* "Inset" content in articles
  * https://jsfiddle.net/mtigas/0r220L8b/
  * https://jsfiddle.net/mtigas/0r220L8b/1/
*

---

Using the inspector, let's look at the layout of some web pages and see how the box model comes together:
* https://www.propublica.org/
* https://www.propublica.org/article/the-demolition-of-workers-compensation
* http://www.nytimes.com/interactive/2012/07/20/us/drought-footprint.html

Layout exercise
* Copy all the HTML from [here](https://codepen.io/sisiwei/pen/OMKZNE?editors=1000). Open your code editor, paste this into a new blank file, and save it as an HTML file on your computer (like `week3.html`).
* Write some CSS that makes it look like this:  
  https://projects.propublica.org/graphics/images/data-institute/presentations/drought.png
* Alternatively, you can work in here https://jsfiddle.net/mtigas/ca2hh4s9/ and make changes and press "Run" to see your changes.

---

### HTML/CSS: Mobile CSS

Using the inspector, let's look at a few sites in normal view and in mobile view
* https://projects.propublica.org/nonprofits/organizations/135562308

CSS has a special feature called "[https://www.w3schools.com/cssref/css3_pr_mediaquery.asp](media queries)" that let you change the CSS based on the size of the screen and other traits.

```css
.my_box {
  width: 450px;
  padding: 10px;
}
@media screen and (max-width: 480px) {
  .my_box {
    width: 100%;
  }
}
```

In the above code, a `<div class="my_box"></div>` will behave like this:

On the desktop (or a tablet, or any screen bigger than 480px):
* Width will be 450px.
* Padding will be 10px.

On screen sizes smaller than 480px:
* Width will be the full width of the screen or window
* Padding will _still be_ 10px.

(Why does the padding stay at 10px? Any CSS that isn't inside `@media` happens to _all screen sizes_. But the order matters: CSS you set later in the file will override CSS set earlier. If you go to the inspector, inspect the div, and look at the "Styles" tab, you'll see what rules get overridden by other CSS — they show up as crossed-out.)



To use this, you first have to add the following within the `<head></head>` section of your HTML file — it tells mobile browsers not to show a "zoomed out" version of the desktop view.

```html
<meta name="viewport" content="width=device-width" />
```

---

### HTML/CSS: Basic Data Visualization

* [Two numbers exercise](http://www.scribblelive.com/blog/2012/07/27/45-ways-to-communicate-two-quantities/)

Some web data visualization is possible without anything more than plain HTML/CSS
* https://projects.propublica.org/nonprofits/organizations/135562308
  * Using percent-width (`width: 50%;`) to draw bars
  * Using opacity `opacity: 50%;`
  * Using font sizes
* https://jsfiddle.net/mtigas/bmf8oLtt/

---

### Google Charts and a peek at JavaScript

This might be a little overwhelming, but let's

https://developers.google.com/chart/

---

### Resources & Reference

- ["block" tags vs "inline" tags in HTML](https://www.w3schools.com/htmL/html_blocks.asp)
- Slides: [Basic CSS](https://projects.propublica.org/graphics/images/data-institute/presentations/css.pdf)
- Slides: [CSS Layout](https://projects.propublica.org/graphics/images/data-institute/presentations/css-layout.pdf)

- [CSS Media Queries](https://www.w3schools.com/cssref/css3_pr_mediaquery.asp)
