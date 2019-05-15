# Pushing your games to the Github repository

You've spent the last day or so hacking around with PyGlet, making games. Now you are going to use Git to push your games onto the main Github project page so that the TMCS-2019 Github repository contains a record of what you have done.

To do this you are each going to need a Github username, which [you can set up here](https://github.com/). 

There is a [10-part series of videos from the always entertaining Daniel Schiffman](https://www.youtube.com/playlist?list=PLRqwX-V7Uu6ZF9C0YMKuns9sLDzK6zoiV) which I highly recommend because they provide a superb intro to Git and Github, which you should watch later.

I usually like to keep all of my GIT projects in a single directory called GIT-repos, because this enables me to easily keep track of the various projects to which I'm contributing. Make a GIT-repos directory on your machine, and then we can get started.

The steps which you are going to follow are essentially these:
1. you will want to go the TMCS-2019 Github repository and fork the repo, which creates a separate version that you can now work on.
2. then you are going to clone your fork onto your own machine, which will let you inspect its contents. You will see that it contains a folder called studentProjects.
3. Navigate to the studentProjects directory a folder whose title is firstnameSurname (so for example, I would name this folder davidGlowacki). Place within the firstnameSurname folder all of the files required to run your game from pyCHARM. Be sure to include a README.md file which includes instructions that people unfamiliar with your game need in order to run it. 
4. Once you've placed the files in the directory, you need to tell Git that it should consider these new files to be part of the repository. From within the firstnameSurname directory, you can do this with the command

    $ git add --all

5. git commit your changes to your local TMCS-2019 repository
6. do a git push, so that your (merged) local repository shows up in the remote TMCS-2019 Github fork. You can determine whether you have managed to successfully push your changes to your own TMCS-2019 Github fork by inspecting your fork, and checking whether you see your firstnameSurname folder, which should contain the appropriate files required to run your game.
7. then go to Github and do a pull request, which is essentially a request that the owner of the repository (davidglo) "pull" your changes into the master Github repository from which you forked.

You can determine whether davidglo has accepted your pull request into the TMCS-2019 Github master repository by inspecting [the TMCS-2019/studentProjects folder](https://github.com/davidglo/TMCS-2019/tree/master/studentProjects). Once davidglo accepts, you should see that your firstnameSurname folder, which contains the appropriate files required to run your game.

If you'd like to make any more changes to your files, you can do so by following steps (4) - (7) above.
