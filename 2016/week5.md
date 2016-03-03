# Week 5 - Practice Making Websites, A Little Javascript

### What You'll Learn
* How to make your own layouts
* What Javascript is capable of and how to get started

## Today's Session

### Make Your Own Portfolios
Remember these layouts from last week? We'll spend an hour in class having you actually create your own version of one of these or something similar.

- http://lenagroeger.com/
- http://shancarter.com/
- http://bost.ocks.org/mike/

### A Little Javascript
First, we'll talk about what types of actions Javascript is capable of, including:
* Creating, removing or changing HTML & CSS
	* Creating: Tooltips
	* Removing: Fadeouts
	* Changing: Slideshows, animations
* Controlling the user's browser
	* Scrolling
	* Clicking

In order to include Javascript on your HTML pages, you need to link to them, just like you need to link to CSS files. To link to an external javascript file:

```html
<html>
	<head>
		<script src="script-file-name-here.js"></script>
	</head>
	<body></body>
</html>
```

Similar to CSS, you can also write Javascript within your HTML page:

```html
<html>
	<head>
		<script type="text/javascript">
			alert('Hello!');
		</script>
	</head>
	<body></body>
</html>
```

You can write Javascript on your own, but more often than not, you'll be also using Javascript libraries. Think of them as pre-written javascript that other programmers have created and are letting you use for free. They'll usually be one single javascript file that you can include in your code. The most commmong Javascript library you'll use is probably `jQuery`, which you can [read more about on their site](https://jquery.com/).

In order to use Javascript libraries, you can download them into your project and link to it like you would your own Javascript external files. Or, companies like Google have started hosting common Javascript libraries on their site, that anyone can use. For example, you can link to Google's version of jQuery by using the code below. Here are [all the Javascript libraries Google hosts](https://developers.google.com/speed/libraries/#jquery).

```html
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>
```

Now let's get down to actually writing some Javascript ourselves. Make a new Codepen. We'll go through:
* How to add Javascript libraries to CodePen specifically
* How to use jQuery to create, change, and remove HTML and CSS

[Our puppies Codepen.](http://codepen.io/sisiwei/pen/XdbzwE)