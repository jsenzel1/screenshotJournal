# screenshotJournal
## A visual journal through screenshots
### takes a screenshot every day (I have mine set at 4 o' clock)
### made with github pages, p5, python, and uh what else, that's it I think, does cron count as a framework?


# make your own

Note: this will work natively on mac and I believe linux, and not on windows (sorry)

if you want to make your own but don't know anything about programming, let me know! If you're on mac I'll be happy to make up a little version for you, I'd love to see other people doing this alongside me.

either way though do yourself a favor and google what crontab is, then visit [this site](crontab.guru) to understand how it works better. it's really awesome you won't regret it

making your own should be pretty simple, but it does involve a tiny bit of programming knowledge. 


# step 1
 the first step is simply to fork this repo (or if you just want a local version for your own viewing, clone or download it) 

# step 2

delete my existing screenshots, and run reset.py, also delete all the text in dates.txt

# step 3

you need to replace some names of things. In taker.py, anywhere you see

`/Users/Jonah/githubProjects/screenshotJournal/caps/`

change it to whatever folder your repo is in, ie:

`/Users/billySmith/Desktop/screenshotJournal/caps`

(use find and replace to do this quickly)

# step 4

add these lines to crontab (using crontab -e)

`* 16 * * * python3 /Users/Jonah/githubProjects/screenshotJournal/taker.py`

`* 16 * * * osascript -e 'tell app "System Events" to display dialog "Screenshot Taken"'`

thes are also included in the "cronJobs.txt" file

(the second line is just an applescript pop up, so its really not important just nice to have a little notification maybe, maybe not?)

# That should be it!
am I forgetting something? I'm probably forgetting something. If you have any issues, email me at jsenzel1@gmail.com and I'll be happy to help you out with anything and everything

Best,

Jonah
