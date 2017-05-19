## The ingredients for an install

Getting to the point where you can do this at work or home can be half the battle. The good news is that it can pretty much all be had for free. Let's talk for a second about what this will require:

- **A text editor**
- **Python**
- **Access to a command line interface**
- **pip**
- **virtualenv**
- **virtualenvwrapper**
- **A connection to the internet**

Here's what the various parts do, as well as why you need them:

**The text editor** allows you to write scripts for the Python interpreter in a plain text format. Something along the lines of a full word processor (think Microsoft Word or Apple's Pages) won't cut it; those are designed for presentation and resulting files will be cluttered with a bunch of elements that control text styling. Having one at your disposal is a must for writing code and great for examining data. The default text editor is fine, but [Sublime](https://www.sublimetext.com/) or [Atom](https://atom.io/) are nice, fully featured alternatives.

**Python** is the engine of the entire affair; it's a code interpreter that's going to look at the commands you write and then faithfully execute them. The 2016 session uses version 2.7; the 2017 session uses version 3.6. This install guide will focus on installing the latest version of Python 3.

**Access to a command line interface** in the form of the OS X terminal or Windows command prompt. It will be used to run Python scripts and access the Python interpreter.

**pip** is a Python library that helps you manage the download and installation of packages that don't come with standard Python. There's a lot there already, sure, but people have written new modules to assist with tasks like web scraping and dealing with PDF files. It makes adding new functionality as easy as typing `pip install <some-new-package>`. **pip** will fetch it from the internet and install it for you -- and do the same for any other packages required to make it all work correctly. **pip** comes bundled with Python 3.4 and later.

**virtualenv** is an external Python library that allows you to create virtual sandboxes where your scripts can live and have their own packages, completely compartmentalized from one another. It solves a problem in development where you may have conflicting package needs among different pieces of code. It also insulates you from mucking around with the core Python. When a new virtual environment is created, it springs up with its own copy of Python and **pip**. The packages in the environment can be modified, removed and reset at will, but it will never screw with the underlying Python and **pip** on the system, even if the environment is deleted.

**virtualenvwrapper** is another external Python library that just makes it easier to deal with the various virtual environments; it keeps them organized in one place, and you can easily jump in and out of environments with a few brief commands. Windows has its own version, [**virtualenvwrapper-win**](https://pypi.python.org/pypi/virtualenvwrapper-win).

**A connection to the internet** is necessary because **pip** will be fetching packages from the web.

## On Windows
	
This guide is for Windows 8.1. For other versions of Windows, the process should be similar.

1\. **Download Python 3**

You'll want to download the [most current release of Python 3 for Windows](https://www.python.org/downloads/windows); you'll likely have the best luck with the *Windows x86 MSI installer*.

---

2\. **Install Python 3**

When you open the installer, you'll have the option to add python.exe to your `PATH`. All that means is that typing `python` at the command prompt will get you to the interpreter or give you the ability to execute a Python script, regardless of where you've navigated on your system. You want to select this option; it may not be selected by default.

**Make sure this option is selected before completing the install.**

---

3\. **Verify installation of Python and pip**

Open the Windows command prompt. If you're unable to locate it in the "Start" menu, search for an application called **cmd**.

To check that Python was installed successfully, write the following command and hit _enter_:

```bash
python --version
```

If everything went as planned, this should spit out the version number of Python you just installed. 

**Caution**: If you get an error message that says Python isn't recognized as a legitimate command, something's gone awry. Python may not have been added to your command prompt `PATH`, which you can resolve by following step 3 in [this guide](http://www.anthonydebarros.com/2014/02/16/setting-up-python-in-windows-8-1/). If the main Python directory, its Scripts folder and site-packages are already on the `PATH`, you might need to reinstall.

Once we've verified that all is well with Python, let's turn our attention to **pip**:

```bash
pip list
```

If **pip** was installed correctly along with Python, you should get a quick recap of any nonstandard packages it can find. The output probably looks something like:

```bash
pip (7.0.1)
setuptools (16.0)
```
It may also have a message griping about an outdated version of **pip**, but let's not worry about that right now.

**Caution**: If the command prompt threw some kind of error at you, **pip** may not be installed and there are a couple of things you can try. You can reinstall Python from the MSI file and make sure the option to install **pip** is selected. It can also be installed manually by following [the instructions here](https://pip.pypa.io/en/stable/installing.html).

---

4\. **Install virtualenv**

With **pip**, adding the **virtualenv** package is as easy as typing:

```bash
pip install virtualenv
```

It should appear among pip and setuptools when you type ```pip list``` and you should be able to verify the version with:

```bash
virtualenv --version
```

---

5\. **Install virtualenvwrapper-win**

You may start to be seeing a pattern here with installation using **pip**:

```bash
pip install virtualenvwrapper-win
```
**Caution**: If you prefer to use a more robust command line interface like Windows PowerShell, note that the package **virtualenvwrapper-win** won't work; try something like **[`virtualenvwrapper-powershell`](https://pypi.python.org/pypi/virtualenvwrapper-powershell)** instead (note, though, that it's only tested on Python 2.7).
	
This wrapper just adds commands for easier interaction with **virtualenv**. For example: Instead of having to navigate to an environment's "Scripts" folder and ```activate``` it, typing ```workon <your-virtual-environment>``` achieves the same effect regardless of what directory you're in.

---

**Other ways into Python on Windows**

In recent years IRE has been teaching Python in PC labs, and the easiest way to get everyone set up quickly has been to use the [Anaconda distribution of Python](http://continuum.io/downloads), which comes with many popular nonstandard libraries already installed alongside the core program.

This remains an option available to you; it comes with **pip** and has its own method of segregating projects into virtual environments.

## On OS X

Python comes pre-installed on OS X, which actually makes the process of getting set up properly more difficult.

Yes, more difficult.

The version accompanying OS X has been tinkered with by Apple, and it's responsible for other functionality on your computer. It's also likely out of date.

The accepted way to get around this problem is to install an OS X program called [Homebrew](http://brew.sh/), which is essentially a package manager for your system, similar to what pip does for Python. It will allow you to download an independent and updateable version of Python that you can use going forward. A side benefit is that `pip` comes with the Python you install with Homebrew.

Not to evangelize about Homebrew too much, but if you decide to travel down the path leading to some of the more complex data journalism techniques on the command line, you'll find other uses for Homebrew and its many packages beyond just providing a clean copy of Python.

It has downsides; Homebrew requires a current version of Apple's Xcode's command line tools to be installed on your computer first. A full guide is [available here](https://github.com/Homebrew/brew/blob/master/docs/Installation.md#installation) to get you up and running.


0\. **Install Homebrew** 
Here are the steps to install Homebrew and Python 3 (borrowed from [this excellent guide to getting up and running on Python](https://python-guide-pt-br.readthedocs.io/en/latest/starting/install3/osx/)):

First, install Xcode:

```bash
xcode-select --install
```

Then install Homebrew:

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Now you need to add a line to the bottom of your `~/.profile`:

In the terminal, type:

```bash
open -e ~/.profile
```

If you get an error message, you may need to create it first:

```bash
touch ~/.profile
open -e ~/.profile
```

Add this line to bottom of the file and hit save:

```bash
export PATH=/usr/local/bin:/usr/local/sbin:$PATH
```

Now it's time to use Homebrew to install Python:

```bash
brew install python3
```

Once that finishes, you will have two versions of Python on your machine:

- Running `python` from the terminal will launch the Apple version of Python 2.7
- Running `python3` will launch the latest version of Python 3 that you just installed



_Running El Capitan?_ Changes in OS X 10.11 El Capitan can make this process even trickier. Apple instituted extra system protections that have the capability of adding a few steps to the Homebrew install process. If you're running into these issues, [read this](https://github.com/Homebrew/homebrew/blob/master/share/doc/homebrew/El_Capitan_and_Homebrew.md) for more information.

	
1\. **Check for pip**
Homebrew's Python comes with pip in tow -- which, for Python 3, is used by calling `pip3`. If you're using the OS X system version, it may not be installed -- check first. Open the Terminal and type the following:
```bash
pip3 -V
```
If pip is installed, this will return a version number.

----
	
2\. **If it's not there: Get pip**
Download [`get-pip.py`](https://bootstrap.pypa.io/get-pip.py), navigate to wherever you downloaded it and type the following:
```bash
python get-pip.py
```

See [this walkthrough](http://pip.readthedocs.org/en/stable/installing/) for more information on installing pip.

----

3\. **Verify the presence of Python and pip**
Let's see what we're working with here and check to make sure all is well:

```bash
python3 -V
pip3 -V
```
----

4\. **Get and install virtualenv**

With **pip**, adding the **virtualenv** package is as easy as typing:

```bash
pip install virtualenv
```

It should appear among pip and setuptools when you type ```pip list``` and you should be able to verify the version with:

```bash
virtualenv --version
```

----

5\. **Get and install virtualenvwrapper**

We can install virtualenvwrapper with **pip** as well:

```bash
pip install virtualenvwrapper
```
	
This wrapper just adds commands for easier interaction with **virtualenv**. You can make new virtual environments easily, using the `mkvirtualenv` command. And instead of having to navigate to an environment's "Scripts" folder and `activate` it, typing `workon <your-virtual-environment>` wherever you're at in the system achieves the same effect.

Remember: You now have two versions of Python on your machine. You can specify which version of Python to use in a virtual environment by passing an argument to the `mkvirtualenv` command.

If you want to use Python 3:

```bash
mkvirtualenv test-env -p 3
```

If you want to use Python 2:

```bash
mkvirtualenv test-env -p 2
```
----

6\. **Modify your .bash_profile so you can use virtualenvwrapper commands and give your virtualenvs a home**

This can be accomplished by opening your .bash_profile, which is typically in your main user directory. Typing:
```bash
open -e ~/.bash_profile
```
Opens the file in your system's default text editor -— probably TextEdit.

If you get an error saying that the file doesn't exist, create one and then try opening it again.
```bash
touch ~/.bash_profile
open -e ~/.bash_profile
```

The following lines need to be added once it's been opened:

```bash
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
```
The first line just sets up a directory for your virtual environments; if you don't want them in your Home directory in a folder called "Envs," you can change the path accordingly.

The second line is a hook for **virtualenvwrapper** so that its commands will work when you type them in the Terminal. 

_Optional_: If you want to use Python 3 by default with `virtualenvwrapper` instead of Python 2, you can also add these two lines:

```bash
export VIRTUALENV_PYTHON=/usr/local/bin/python3
export VIRTUALENVWRAPPER_PYTHON=$VIRTUALENV_PYTHON
```

----

7\. **Reload your .bash_profile**

So that these new changes take effect, type:
```bash
source ~/.bash_profile
```

You should see several new thing run in the Terminal after the reload as it makes a place for your environments.

----

## Test run

```bash
mkvirtualenv mytest
deactivate
workon
workon mytest
pip list mytest
```

These lines do the following:

- Create a new virtual environment called "mytest"
- Exit the "mytest" environment
- List the virtual environments that presently exist
- Move into the "mytest" environment again
- List all libraries presently installed in "mytest"
