# Week 1 - Introduction, Github, Command Line
We might not get through everything, but we'll get as far as we can.

### What You'll Learn
* What different programming languages are for and how they work together
* How to use the command line to execute some basic commands on your computer
* How to publish up a website you made from scratch using Github pages
* How to follow the same workflow as professional developers when coding (and why they do things this way)

## Today's Session

### Intro to Code

### Git and GitHub

https://projects.propublica.org/graphics/images/data-institute/presentations/git-and-github.pdf

__What is Git?__
  * Version control for coders
    * Why do coders need version control?
      * Sometimes your code just breaks and you need to go back
      * Collaboration
      * Think of it like "track changes" or "revision history"

__What is Github?__
  * Graphical web service that helps people use git, plus some other nice features
  * Why would anyone use it?
    * Creators:
      * Version control
      * Collaboration
      * Sharing with the world
      * Free web hosting
      * Project management extras (issues, milestones, etc.)
    * Users:
      * Access open-source projects and libraries
      * Contribute to projects online (pull request)

__Who uses it?__
- [NYTimes](https://github.com/nytimes/)
- [Washington Post](https://github.com/washingtonpost)
- [ProPublica](https://github.com/propublica)
- [Quartz](https://github.com/quartz)
- [WNYC](https://github.com/wnyc)

__How does Github work exactly?__

Four basic commands to sync the code on our computer to the repository hosted on Github; in the command line, you'd do it like this:

```
git status
git add .
git commit -m "Updated design"`
git push
```

Creating 'branches' and using a branch called 'gh-pages' to create our own website.

```
git branch
git branch gh-pages
git checkout gh-pages
git push origin gh-pages
```

(Don't fret! We'll get to the command line shortly.)

What else is possible? [Github's excellent cheatsheet](https://training.github.com/kit/downloads/github-git-cheat-sheet.pdf). They also have a [tutorial](https://try.github.io).

We'll also go over how commits, push, pull, and branches work in the GitHub app.

#### Hands-on with GitHub

1. Create a new account on [Github](https://github.com).
2. Install and setup Git and SSH Keys.
    * Mac:
       * Git: https://help.github.com/articles/set-up-git/
       * SSH: https://help.github.com/articles/generating-ssh-keys/
    * Windows:
       * https://windows.github.com/

### Command Line Basics

[Command line cheatsheet](https://github.com/propublica/institute-files/blob/master/commandline.md)

[Command line basics](https://github.com/sisiwei/nyu-spring-tutorials/blob/master/2015/tutorials/command-line-basics.md).
