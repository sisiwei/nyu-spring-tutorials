# Week 1 - Github and the Command Line
We might not get through everything, but we'll get as far as we can.

### What You'll Learn
* How to use the command line to execute some basic commands on your computer
* How to publish up a website you made from scratch using Github pages
* How to follow the same workflow as professional developers when coding (and why they do things this way)

## Today's Session

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

__Who uses it?__
- [NYTimes](https://github.com/nytimes/)
- [Washington Post](https://github.com/washingtonpost)
- [Propublica](https://github.com/propublica)
- [Quartz](https://github.com/quartz)
- [WNYC](https://github.com/wnyc)

### Installs and Account Creation

1. Create a new account on [Github](https://github.com).
2. Install and setup Git and SSH Keys.
    * Mac:
       * Git: https://help.github.com/articles/set-up-git/
       * SSH: https://help.github.com/articles/generating-ssh-keys/
    * Windows:
       * https://windows.github.com/

__How does Github work exactly?__

Four basic commands to sync the code on our computer to the repository hosted on Github

```
git status
git add .
git commit -m "Updated design"`
git push
```

Creating 'branches' and using a branch called 'gh-pages' to create our own website

```
git branch
git branch gh-pages
git checkout gh-pages
git push origin gh-pages
```

What else is possible? [Github's excellent cheatsheet](https://training.github.com/kit/downloads/github-git-cheat-sheet.pdf). They also have a [tutorial](https://try.github.io).

### Command Line Basics

But before we try any of these commands themselves, we need to know some [Command line basics](tutorials/command-line-basics.md).

<table>
    <tr>
        <th>Command</th>
        <th>Example</th>
        <th>What it does</th>
        <th>Notes</th>
    </tr>
    <tr>
        <td>pwd</td>
        <td>pwd</td>
        <td>Shows your present working directory</td>
        <td>Useful for keeping track of where you are</td>
    </tr>
    <tr>
        <td>ls</td>
        <td>ls</td>
        <td>Shows the contents of the current directory</td>
        <td>Can also use ls -a or ls -l to show more information about files</td>
    </tr>
    <tr>
        <td>cd</td>
        <td>cd Desktop</td>
        <td>Changes directories</td>
        <td>Use cd ..``` to move backwards</td>
    </tr>
    <tr>
        <td>mkdir</td>
        <td>mkdir new-directory</td>
        <td>Creates a new directory</td>
        <td></td>
    </tr>
    <tr>
        <td>touch</td>
        <td>touch test.py</td>
        <td>Creates a new file</td>
        <td></td>
    </tr>
    <tr>
        <td>mv</td>
        <td>mv test.py ./Desktop</td>
        <td>This isn't covered above, but mv moves or renames a file.</td>
        <td></td>
    </tr>
    <tr>
        <td>rm</td>
        <td>rm test.py</td>
        <td>Deletes a file</td>
        <td>Use with extreme caution. Once a file is deleted this way, you can't get it back.</td>
    </tr>
</table>
