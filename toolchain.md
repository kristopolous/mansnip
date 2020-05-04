These are my notes on the rather complex assortment of tools surrounding manpages and what they do.

groff will take man pages as input, but not in the gzip format that you find on modern unix systems ... it will ingest these files just fine, because the language syntax doesn't use a stack machine and unrecognized syntax is just interpreted as content. This means a bunch of binary crap will still be "processed". For instance, you can do `groff random_file.jpg` and get output. It never fails, take that Turing!

Now if instead we take this from man 7 roff

    cat file | ... | preproc | ... | troff options | postproc

and try to make a real example of it ... I'm going to use lsmod(8), one of my favorite man pages, 74 words including a copyright and a notice that it's maintained by more than one person. 

Isn't that hilarious? Yes, it's quite funny. Anyway,

Let's just do this to make our life easier for now.

    $ cp /usr/share/man/man8/lsmod.8.gz /tmp/
    $ cd /tmp
    $ gzip -cd lsmod.8.gz | groff -

Hey, stuff ... it looks like maybe that will be something.

And now we'll find out that this is actually a thing.

    $ gzip -cd lsmod.8.gz | groff -X -

Wow, that's hideous. Not even anti-aliasing. Did you know that all of
X used to look basically just like this? Look up xmail. 

Oh heck the internet is useless these days, all these results suck. 

Ok try xvidtune instead. There we go, that's the stuff. If X didn't come out of MIT nobody would have taken this thing seriously, it's crazy. 

Anyway, you may also notice that the `groff -X` formatting has all the white-space of 18th century literature, let's fix that. 

There's a tool that tries to make this sane called grog(1).






groffer
grog

troff ditroff 

groff is the GNU roff

man
