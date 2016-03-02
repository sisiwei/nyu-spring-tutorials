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

Similar to CSS, you can also write Javascript within your HTML page, but using the tags:

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