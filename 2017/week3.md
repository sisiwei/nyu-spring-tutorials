# Week 3

* HTML/CSS: Page Layout & Basic Mobile Design
* HTML/CSS: Basic Data Visualization

### HTML/CSS: Page Layout and Basic Mobile Design

Box model
Block tags vs inline tags

CSS properties of boxes:
* width / height
* border
* padding
* margin
* float

Using the inspector, let's look at the layout of some websites
* https://www.propublica.org/
* https://www.propublica.org/article/the-demolition-of-workers-compensation
* http://www.nytimes.com/interactive/2012/07/20/us/drought-footprint.html

Layout exercise
https://codepen.io/sisiwei/pen/OMKZNE?editors=1000

---

Using the inspector, let's look at a few sites in normal view and in mobile view
* https://projects.propublica.org/nonprofits/organizations/135562308

CSS has a special feature called "[https://www.w3schools.com/cssref/css3_pr_mediaquery.asp](media queries)" that let you change the CSS based on the size of the screen and other traits.

```css
.my_box {
  width: 300px;
  padding: 10px;
}
@media screen and (max-width: 480px) {
  .my_box {
    width: 100%;
  }
}
```

In the above code, a `<div class="my_box"></div>` will have a width of 300px and a padding of 10px on a tablet or desktop view. What properties will it have on a mobile device?

(A: Width 100% and padding of 10px. Any CSS that isn't inside `@media` gets set for all screen types. But the order matters: CSS you set later in the file will override CSS set earlier.)

But first, you have to tell the web browser that it should

```html
<meta name="viewport" content="width=device-width" />
```

### HTML/CSS: Basic Data Visualization

* [Two numbers exercise](http://www.scribblelive.com/blog/2012/07/27/45-ways-to-communicate-two-quantities/)


### Resources & Reference

- ["block" tags vs "inline" tags in HTML](https://www.w3schools.com/htmL/html_blocks.asp)
- Slides: [Basic CSS](https://projects.propublica.org/graphics/images/data-institute/presentations/css.pdf)
- Slides: [CSS Layout](https://projects.propublica.org/graphics/images/data-institute/presentations/css-layout.pdf)

- [CSS Media Queries](https://www.w3schools.com/cssref/css3_pr_mediaquery.asp)
