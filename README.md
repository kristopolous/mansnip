# Just the snippets of man you want

Man pages are an impressive feat! 

Some of them however, are very unwieldy and hard to navigate.

Let's say I was looking for the syntax for the built-in `declare` command inside of `bash(1)`.

I would do

    $ man bash

Then just simply search for the string "declare" with the "/" command! Easy peasy!

Here's the problem:

    $ man bash | grep -c declare
    34

There's 34 of them. I'll have to go through all by using the 'n' keystroke, which here stands for 'nope, nope, nope'. 

If I were to look for the syntax to the bash built-in command named `command` I'd be faced with a daunting 615 matches. Oh dear.

"Oh wait", someone in the peanut gallery says "there's a faster way".

Ok, here's the fastest I know of. Let's roll

    $ man bash
      -N        turn line numbering on
      &declare  show all the results for "declare", scan them (remember the line number for which one you want)
      &[enter]  turn off the filtered view
      g(number) go to that line

And there you go. I remember navigating in the 1980s as well. 

This is insane. Why is this basic functionality not there?

## Wouldn't it be nice to just get the part you want?

Yes, why does this not exist? Why can't I just do something like this:

    $ man bash | mansnip declare
           declare [-aAfFgilnrtux] [-p] [name[=value] ...]
           typeset [-aAfFgilnrtux] [-p] [name[=value] ...]
                  Declare variables and/or give them attributes.  If no names are given then display the
                  values  of  variables.   The  -p option will display the attributes and values of each
                  name.  When -p is used with name arguments, additional options, other than -f and  -F,
                  are  ignored.   When  -p  is  supplied without name arguments, it will display the at‐
                  tributes and values of all variables having the attributes specified by the additional
                  options.   If  no  other  options  are  supplied with -p, declare will display the at‐
                  tributes and values of all shell variables.  The -f option will restrict  the  display
                  to  shell functions.  The -F option inhibits the display of function definitions; only
                  the function name and attributes are printed.  If the extdebug shell option is enabled
                  using  shopt, the source file name and line number where each name is defined are dis‐
           ...
    $

Well, now you can! (ok that was obvious, that's why I'm talking about it...)

## Why hasn't this existed forever?

man pages don't really encode a lot of semantic detail. The format is pretty old. There's been a number of replacements, such as GNU info and BSD mandoc but the ones you have on your system are probably boring old man files. Ah, inertia.

Being old, it's primarily concerned with formatting and not any kind of meta-information. And boy can it format! Try using the groffer(1) tool and do something like `groffer ffmpeg`. You'll hopefully get a very beautiful PDF popping up on your screen, excellent for printing out and keeping in a 3-ring binder next to your rolodex and fax machine. Did you know groff is in a lineage that goes back to the 1964 RUNOFF program on MIT's IBM 7094 CTSS? A mere year after Licklider's [Intergalactic Computer Network](https://en.wikipedia.org/wiki/Intergalactic_Computer_Network) memo leading to what you *probably* call "the internet" these days.

Anyway, so inside the document source that leads to the pretty man page, there is next to no indication that something is special. Let's go back to bash and specifically the lines that say "declare" and "typeset". Here's the actual source:

    .TP
    \fBdeclare\fP [\fB\-aAfFgilnrtux\fP] [\fB\-p\fP] [\fIname\fP[=\fIvalue\fP] ...]
    .PD 0
    .TP
    \fBtypeset\fP [\fB\-aAfFgilnrtux\fP] [\fB\-p\fP] [\fIname\fP[=\fIvalue\fP] ...]
    .PD

Alright, what do those things mean? You can see that in `man 7 man` or actually, 

    $  man 7 man | mansnip .TP .PD 
       .TP i    Begin paragraph with hanging tag.  The tag is given on the next line,  but  its  re‐
                sults are like those of the .IP command.
       .PD d    Set  inter-paragraph  vertical  distance to d (if omitted, d=0.4v); does not cause a
                break.

Hrmm, well that's a problem. It's effectively just a stylesheet. In fact, the format doesn't look fundamentally different than it did in [UNIX v0 in 1970](https://github.com/DoctorWkt/pdp7-unix/blob/master/man/stat.1). A mere 2 years after Engelbart demoed a prototype hyperlink system, this is well before the semantic web.

"But wait," you say. "If I do `man -html bash` and then wait for the glacially slow groff HTML post-processor I do indeed get links!"

Yes, the only two semantic concessions given in the modern man format is `.SH` which is for sections and `.TH` for the title (they also have stylistic definitions as well - the separation of concerns isn't there).  

"Well let's fix this!" you say. A third time? lol, ok, have fun. We're probably stuck with these for the rest of our lives.

"So there's no surefire easy way to find these snippets then, you can only guess?"

Uh, yep.


### It's not that terrible though!

Man pages are ridiculously consistent as far as non-semantically structured text goes.  It seems to work fine and if it doesn't, you can just go hunting and pecking like you usually do.

### This code looks really simple

Yeah, not everything that's useful is necessarily hard.

