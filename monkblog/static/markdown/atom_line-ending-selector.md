

# Atom line-ending-selector error

<a href='http://www.atom.io'><img class='img-responsive atom-logo' src='./posts/images/atomeditor.png' alt="Get Atom!"/></a>

Today I installed the beautiful [Atom editor](http://www.atom.io/) on my Ubuntu 14.10 system.

Immediately I received an error message:

```
Uncaught TypeError: object is not a function

At /usr/share/atom/resources/app.asar/node_modules/line-ending-selector/lib/main.js:74

TypeError: object is not a function
    at Object.consumeStatusBar (/usr/share/atom/resources/app.asar/node_modules/line-ending-selector/lib/main.js:74:23)
    at Provider.module.exports.Provider.provide (/usr/share/atom/resources/app.asar/node_modules/service-hub/lib/provider.js:30:52)
    at /usr/share/atom/resources/app.asar/node_modules/service-hub/lib/service-hub.js:55:26
    at doNTCallback0 (node.js:416:9)
    at process._tickCallback (node.js:345:13)
```

There's several pieces of info going on here, so what can I do to find out more?

(This post has lots of helpful info taken from the [issue I created on Atom's GitHub.](https://github.com/atom/line-ending-selector/issues/9))

In Atom you can open a developer console similar to one you'll find in your web browser.
This console will let you browse through the source files loaded by Atom, among a plethora of other info.

#### What's going on here?

To open the console, click: `View > Developer > Toggle Developer Tools`.

<br/>

<figure class="figure center-block">
    <a href="./images/atom_devconsole.png">
        <img class='img-responsive' src="./posts/images/atom_devconsole.png" />
    </a>
    <figcaption class="figure-caption">
        The Atom developer console - select the Sources tab.
    </figcaption>
</figure>

<br/>

If you check the Sources tab, you'll see that there's only 2 sources loaded from `[...]/node_modules/line-ending-selector/`.

#### What gives?

Why aren't all the sources showing as loaded?
Where is
I have no idea - probably because I don't know how Atom works under the hood.

#### So you don't know anything, do you at least know how to fix it?

Well... sort of.
I mean... technically, no.

But I found a workaround that is working perfectly for me: [build Atom from source](https://github.com/atom/atom/tree/master/docs/build-instructions).

<i>Build from source? What a hassle.</i>

Yes, I hear you saying this in the back of your head.
But believe me, it's a pretty painless process.

For more details, check out my post about [Building Atom from source](/markdown/build_atom).
