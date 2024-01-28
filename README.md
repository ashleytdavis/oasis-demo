# Git Version Control Tutorial

## Basic Version Control using Github Desktop

Check out the slides [here](https://docs.google.com/presentation/d/10KpKDJYZdpAfZhK_YtrPJZJqOGL0hqMvNc5FFcaS0Rk/edit?usp=sharing) for the tutorial

## Advanced Version Control using Terminal

1. Creating a new repository on the command line:

```
$ echo "# repo-name" >> README.md
$ git init
$ git add README.md
$ git commit -m "init repo"
$ git branch -M main
$ git remote add origin https://github.com/username/repo-name.git
$ git push -u origin main
```

2. Cloning a repository from GitHub:

```
$ git clone https://github.com/username/repo-name.git
```

3. Initializing a new project (e.g. using create-react-app):

```
$ npx create-react-app my-app
```

4. Creating a new branch and switching to it:

```
$ git branch new-feature
$ git checkout new-feature
```

5. Making changes to the code and committing:

```
$ git add .
$ git commit -m "Added new feature"
```

6. Pushing changes to the remote repository:

```
$ git push origin new-feature
```

7. Creating a pull request on GitHub:

   1. On GitHub, navigate to the main branch of your repository
   2. Click on "Pull requests" tab
   3. Click on "New pull request" button
   4. Select the branch you just pushed
   5. Click on "Create pull request"

8. Merging the pull request:
   1. On GitHub, navigate to the pull request
   2. Click on "Merge pull request"
   3. Confirm the merge
