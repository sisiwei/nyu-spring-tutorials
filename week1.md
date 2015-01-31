# Week 1 - Github and the Command Line
We might not get through everything, but we'll get as far as we can.

## Meta

### What You'll Learn
* How to use the command line to execute some basic commands on your computer
* How to publish up a website you made from scratch using Github pages
* How to follow the same workflow as professional developers when coding (and why they do things this way)

### External Resources
Missed the session or want a quick refresher? Here are some tutorials that cover most of what we'll be talking about in class:

* [https://try.github.io](https://try.github.io)
* [Command line basics](tutorials/command-line-basics.md)

## Today's Session

### Installs and Account Creation

1. Create a new account on [Github](https://github.com).
2. Install and setup Git and SSH Keys.
    * Git: https://help.github.com/articles/set-up-git/
    * SSH: https://help.github.com/articles/generating-ssh-keys/

### Git vs. Github

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

__How does Github work exactly?__

Four basic commands to sync the code on our computer to the repository hosted on Github:

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






Want more? [Github's excellent cheatsheet](https://training.github.com/kit/downloads/github-git-cheat-sheet.pdf).
