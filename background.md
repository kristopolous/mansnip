## Pre-history

Here were my two methods of searching before I made this tool:

 * Search with a leading space, sometimes "  -t" with two spaces, sometimes with one, etc... Very imprecise

And when using less as the pager

  * `man bash `
  * `-N       ` turn line numbering on
  * `&declare ` filter and show all the results for "declare", scan them (remember the line number for which one you want)
  * `&[enter] ` turn off the filtered view
  * `g(number)` go to that line

I've been using these older workflows for 20+ years really without questioning it. It always felt a little primitive so I went looking for the more sophisticated way.

I thought "surely there's like an xpath system here where I can do some * queries or display a tree hierarchy... I'm clearly just doing this in a bonehead manner"

I looked for these and they didn't exist. The regex and cycle method was the best way there was.

Shocking. 

So I built something better.

## Why hasn't something like mansnip existed forever?

It is pretty obvious and I was surprised myself to find nothing.

One of the reasons is man pages don't really encode a lot of semantic detail. The format is pretty old. There's been a number of attempted replacements, such as [GNU info](https://www.gnu.org/software/texinfo/manual/info-stnd/) and [BSD mdoc](https://mandoc.bsd.lv/) (`man 7 mandoc_mdoc`) but the ones you use on your system are probably just the traditional boring old man files. Ah, inertia.


Being old, it's primarily concerned with formatting and not any kind of meta-information. And boy can it format! Try using the `groffer(1)` tool and do something like `groffer git-config`. You'll hopefully get a very beautiful PDF popping up on your screen, excellent for printing out and keeping in a 3-ring binder next to your Rolodex and FAX machine. Did you know groff is in a lineage that goes back to the [1964 RUNOFF](https://en.wikipedia.org/wiki/TYPSET_and_RUNOFF) program on MIT's IBM 7094 CTSS? A mere year after Licklider's [Intergalactic Computer Network](https://en.wikipedia.org/wiki/Intergalactic_Computer_Network) memo leading to what *you* probably call "the internet" these days.

Anyway, so inside the document source that leads to the pretty man page, there is next to no indication whether something has any special meaning. Let's go back to `bash(1)` and specifically the source lines for "declare" and "typeset":

    .TP
    \fBdeclare\fP [\fB\-aAfFgilnrtux\fP] [\fB\-p\fP] [\fIname\fP[=\fIvalue\fP] ...]
    .PD 0
    .TP
    \fBtypeset\fP [\fB\-aAfFgilnrtux\fP] [\fB\-p\fP] [\fIname\fP[=\fIvalue\fP] ...]
    .PD

Alright, what do those things mean? You can see that in `man 7 man` or actually, 

    $ mansnip 7 man .TP .PD .B .P .I
    55   DESCRIPTION
         Fonts
           .B  Bold

    61     .I  Italics

    97   Normal paragraphs
           .P       Same as .PP (begin a new paragraph).

    124  Indented paragraph macros
           .TP i    Begin paragraph with hanging tag.  The tag is given on the next line,  but  its  re‐
                    sults are like those of the .IP command.

    147  Miscellaneous macros
           .PD d    Set  inter-paragraph  vertical  distance to d (if omitted, d=0.4v); does not cause a
                    break.



Hrmm, well that's a problem. It's effectively just a stylesheet. In fact, the format doesn't look fundamentally different than it did in [UNIX v0 in 1970](https://github.com/DoctorWkt/pdp7-unix/blob/master/man/stat.1). A mere 2 years after [Engelbart demoed a prototype hypertext](https://en.wikipedia.org/wiki/The_Mother_of_All_Demos) system, this is well before the [semantic web](https://en.wikipedia.org/wiki/Semantic_Web).

"But wait," you say. "If I do `man --html bash` and then wait for the glacially slow [groff HTML post-processor](http://git.savannah.gnu.org/cgit/groff.git/tree/src/devices/grohtml) I do indeed get links!"

Yes, the only two semantic concessions given in the modern man format is `.SH` which is for sections and `.TH` for the title and ... that's ... it.

"Well let's fix this!" you say! 

A third time? lol, ok, have fun. Might work. For now we're stuck with these.

"So there's no surefire easy way to find these snippets then, you can only guess?"

Uh, yep.


### It's not that terrible though!

Man pages are ridiculously consistent as far as non-semantically structured text goes.  This tool usually works fine and if it doesn't, file a bug and go hunting and pecking like you usually do. I'll fix it eventually.

Want even more background? Try `mansnip roff HISTORY`.


---

**Still** not satisfied? The [source is commented](mansnip) but seriously, that's the last stop.

