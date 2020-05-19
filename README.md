# FalconCMS

FalconCMS is a CMS for Habbo emulators. It currently targets Arcturus MorningStar emulator,
 but intends on supporting multiple emulators. This CMS is coded using the Django framework
 for Python. This CMS can be ran either by CPython through WSGI, directly or it can also be
 compiled as a WAR file and ran under a Java Servlet container.

# Project Directory Structure

Django is a Python web framework. There are many ways to deploy Python, each gets better than
the last, however, due to this CMS being in the early stages I will focus on the basics due to
there not being many (if any) Django projects in the scene.

The parent directory of this project contains this file and other important files such as
 the `manage.py` file which is used to do everything from starting up an HTTP server
 instance to database migrations. 
 
The sub-directories are `falcon` and `falconcms`.

* `./falconcms` houses what is considered the Django root this contains the settings.py file 
    which contains the configuration options for the database and other aspects of the project.

* `./falcon` houses what is known in Django as an 'app', essentially you install applications
    to be included in a Django project. The routes to the applications you wish to include will
    be defined in the Django root's `urls.py` module or other otherwise `./falconcms/urls.py`.
    This specifically defines the root at which that particular app will begin. You may define
    additional routes in each respective app's `urls.py` python module.

There are additional files that are special:

* `manage.py` - As mentioned above is used to maintain migrations as well as running an HTTP server.
    There are other use cases but those are best researched from the Django official docs.

* `requirements.txt` - If you've ever coded in another programming language this is basically a file
    full of Python dependencies to be installed via pip (e.g. `pip install -r requirements.txt`)
    which is Python's main package manager.
* `LICENSE` - The license to the project which is the MIT license, described at the bottom of this file.
* `CONTRIBUTING.md` - A file describing a process for contributing, I stole it from some repository somewhere
    so if it doesn't make sense just get in contact with a maintainer.

# Branching

There are two major branches in this project:
 * master
 * development

The development branch is always what developers are currently working on, and the master branch reflects the
last commit matching a release. You may not want to ever use code from development unless you know what you're
doing, being asked to do so by a developer or are developing FalconCMS.
 
 
# License
Licensed under the MIT License. Essentially meaning: Do anything, just keep the authors copyright in tact,
additionally there is no warranty that this project wont set your computer on fire.
