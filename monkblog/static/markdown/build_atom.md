

# Building Atom From Source

<a href='http://www.atom.io'><img class='img-responsive atom-logo' src='posts/images/atomeditor.png' alt="Get Atom!"/></a>


In [my previous post](/markdown/atom) I came to the conclusion that I needed some kind of workaround to fix my Atom installation on Ubuntu.
That workaround was to build Atom from source.

I'll be reviewing the instructions for Ubuntu/Debian, you may need to [refer to the documentation](https://github.com/atom/atom/tree/master/docs/build-instructions) for your system.

### Workarounds 101

Here's a list of tools you'll be needing:

* C++ toolchain
* Git
* node.js (currently v0.10.x or 0.12.x, or io.js v1.x or v2.x)
* npm (required version listed as v1.4.x in the Atom docs)
* some dev packages

And I would suggest adding:

* [nvm](https://github.com/creationix/nvm) - to make sure you're running the correct version of node.js.

I was using node.js v4.1.0 and needed to quickly switch to v0.12.x, nvm made that a trivial task.

#### Prerequisites

Before you can even start to build anything you'll need to make sure you have a few packages installed already.
For Ubuntu / Debian, you'll need to run:

```bash
sudo apt-get install git build-essential libgnome-keyring-dev fakeroot
```

You'll also need to check if the command `node` does anything on your machine.
You can do this a few ways, try `node -v` to check both availability and version on your machine.
If you get `node: command not found`, see [It didn't work!](#it-didnt-work).

You can also use `which node` to see if node is available.
If the output of this command is entirely blank, see [It didn't work!](#it-didnt-work).

<a name='it-didnt-work'></a>

#### It didn't work!
If neither of these work, you may have `node` installed as `nodejs` - it's not your fault, you didn't do anything wrong, I promise.

If you have `nodejs` available, you can update your system to refer to it as `node` with the following command:

```bash
sudo update-alternatives --install /usr/bin/node node /usr/bin/nodejs 10
```

### Obtaining the source code

Once you have the prerequisites installed and the command `node -v` reports that you have v0.10.x or v0.12.x, you can start the build process.

I preferred to put my source in `/opt/atom/`, however you may perform these commands from any directory.
To make things simple and avoid using `sudo`, make sure you `chown` the directory you want to build from and give yourself permissions.

#### Optional step: creating a folder in `/opt`

```bash
[monkpit@monkbox]~$ sudo mkdir /opt/atom
[monkpit@monkbox]~$ sudo chown `whoami` /opt/atom
[monkpit@monkbox]~$ cd /opt
```

#### Cloning the Atom repo

Now that we are in the parent directory, let's clone the git repo into the `atom` subfolder.
The subfolder will be created if it does not exist, and if you have valid permissions to create it.

```
[monkpit@monkbox]~$ git clone https://github.com/atom/atom atom
Initialized empty Git repository in /opt/atom/.git/
remote: Counting objects: 142979, done.
remote: Compressing objects: 100% (267/267), done.
remote: Total 142979 (delta 190), reused 6 (delta 6), pack-reused 142705
Receiving objects: 100% (142979/142979), 268.44 MiB | 569 KiB/s, done.
Resolving deltas: 100% (101045/101045), done.

[monkpit@monkbox]~$ cd atom && ls
apm           coffeelint.json  dot-atom    menus         script  vendor
atom.sh       CONTRIBUTING.md  exports     package.json  spec
build         Dockerfile       keymaps     README.md     src
CHANGELOG.md  docs             LICENSE.md  resources     static
```

So, we've cloned the repo and we can see there are files in the directory.
What's next?

#### Checkout the latest release

We need to make sure we will be building the latest version when we run the build scripts.
We will use a `git checkout` command to get everything we need.

```bash
[monkpit@monkbox]~$ git fetch -p
[monkpit@monkbox]~$ git checkout $(git describe --tags `git rev-list --tags --max-count=1`)
```

[<i>What on earth does that mean??? Click here to jump to the explanation below.</i>](#explanation)


#### Build the application

This is the hard part, right?

```bash
[monkpit@monkbox]~$ script/build
Node: v0.12.7
npm: v2.11.3
Installing build modules...
Installing apm...
[Yada, yada...]

[monkpit@monkbox]~$ sudo script/grunt install
[Yak yak yak...]

[monkpit@monkbox]~$ atom
```

### aww yiss it's done

Enjoy the awesome Atom editor!

<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>


<a name="explanation"></a>

#### The numbers, Mason!

```bash
[monkpit@monkbox]~$ git checkout $(git describe --tags `git rev-list --tags --max-count=1`)
```

That command might look a little cryptic - let's break it down!
In a shell environment, anything inside the parentheses of `$()` is evaluated and passed to the current command as a string.
Backticks (` `` `) have the same effect.

For example:

```bash
[monkpit@monkbox]~$ echo Hello!
Hello!
[monkpit@monkbox]~$ whoami
monkpit
[monkpit@monkbox]~$ echo Hello, $(whoami)!
Hello, monkpit!
[monkpit@monkbox]~$ echo Goodbye, `whoami`!
Goodbye, monkpit!
```

Armed with that knowledge, let's break this down from the inside-out.

```bash
[monkpit@monkbox]~$ git rev-list --tags --max-count=1
abe924f23185e51f86774e65fb82c638e8777307
```

`git rev-list --tags --max-count=1` lists the latest commit to the repository.

```bash
[monkpit@monkbox]~$ git describe --tags abe924f23185e51f86774e65fb82c638e8777307
v1.0.16
```

`git describe --tags [commit]` describes a commit using the most recent tag from the time of the given commit.
The `--tags` option will use any tag it finds, not just fully annotated tags.

This results in a version number, `v1.0.16`.
I hear you asking, <i>why couldn't we have taken this from the top of the list of tags?</i>
Well, astute reader, we probably could have done that too.
I will leave it as an exercise for the reader.

Lastly, we pull the whole thing together.

```bash
[monkpit@monkbox]~$ git checkout $(git describe --tags `git rev-list --tags --max-count=1`)
```

It really just evaluates to `git checkout v1.0.16`, but it's a way to write it without hard-coding the version number, so the user will always checkout the latest version.

Neat.
