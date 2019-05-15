# TMCS CDT Software Course - TMCS 2019

Tues 14th - Fri 17th, May 2019

designed by David R Glowacki (DRG)

with assistance from:
Stephanie Hare (SH)
Jonathan Barnoud (JB)
Dasha Shchepanovska (DS) 
Becca Walters (BW)
Alexander Jamieson-Binnie (AJB)

## Timetable

Tuesday 14th May (DRG)

* 10:00 Introduction and Overview
* 10:15 Getting Started with Python
    * [A simple Python Program](outlines/gettingStarted.md)
* 10:45 A simple live demo for debugging in PyCharm (DRG)
    * [This video also provides a nice outline of how to debug in PyCharm](https://www.youtube.com/watch?v=BBPoInSOiOY)
    
* 11:00 Learning more about Python
    * [A Python Framework for Simple Game Mechanics](outlines/I-pyGlet-GameMechanics.md)
    * Basic Python features
      * [containers, lists, and dictionaries](python/1_lists_and_dictionaries.md)
      * [functions & modules](python/2_functions_and_modules.md)
      * [documenting Code](python/3_documenting_code.md)
    * [Basic Principles of Object-Oriented Programming](python/4_object_orientation.md)

* 11:30 coffee
* 13:00 Lunch
* 14:00 [Scipy and NumPy](python/5_numpy.md)
* 15:15 Coffee 
* 15:30 [Experiment & Play: Use what you've learned to hack-your-own game mechanics](outlines/II-pyGlet-GameMechanics.md)
* 17:30 Finish 

Wednesday 15th May (DRG, JB, SH, AJB, DS, BW)

* 10:00 [Experiment & Play: Use what you've learned to hack-your-own game mechanics](outlines/II-pyGlet-GameMechanics.md)
* 11:00 coffee
* 12:15 show and tell
* 12:30 Lunch
* 13:30 Version Control 
    * [Part 1: Basic git - structure & commands](outlines/git-outline.md#git-and-version-control) - JB
* 14:30 Version Control
    * [Part 2: Remote repos & GIT GUIs](outlines/git-outline.md#part-2) - JB
    * [Part 3: upload your game projects onto the TMCS-2019 github](version-control/git-exercise.md) - DRG
* 16:00 coffee
* 16:15 [Testing software and catching errors](testing/README.md) ([slides](testing/slides.pdf)) - JB/DRG
* 17:00 Overview of the four hackathon projects
    * JB - Brownian motion on a 2d graph with pyGlet graphics ([slides](hackathon/drunk-simulator/drunk-simulator.pdf))
    * DS - Aesthetic style transfer using neural nets ([description](hackathon/style-transfer/style-transfer.md))
    * SH/RW/AJB - Interactive molecular dynamics in VR (iMD-VR) 
      * RW/AJB - Code-your-own iMD-VR molecular simulations ([slides](https://github.com/davidglo/TMCS-2019/blob/master/hackathon/imd-vr/Code-your-own%20iMD-VR%20molecular%20simulations-converted.pdf))
      * SH/AJB - Dimensionality reduction of iMD-VR data ([description](hackathon/dimensionality-reduction/dimensionality-reduction.md))
* 17:45 Pub. Students should take this opportunity to organize themselves into their project groups

Thursday 16th May (DRG, JB, SH, AJB, DS, BW)

* 10:00 - 18:00 hackathon
    * group 1 led by JB - [description](hackathon/drunk-simulator/drunk-simulator.md) 
    * group 2 led by DS 
    * group 3 led by RW/AJB - [description](https://github.com/davidglo/TMCS-2019/blob/master/hackathon/imd-vr/instructions.md)
    * group 4 led by SH/AJB - [description](hackathon/dimensionality-reduction/dimensionality-reduction.md)
* 18:00 - 19:00 pizza/wine party!

Friday 17th May (DRG, JB, SH, AJB, DS, BW)
 
* 10:00 - 15:00 hackathon
* 15:00 - 16:00 show and tell


## Hints and tips

[Hints and tips](outlines/hints_and_tips.md) on common Bash and editor commands.

Beginners guide to using the [shell](shell/README.md)
## Before you arrive...

We recommend that you bring your own laptop to work on (so 
that you can easily continue to use the same tools for the hackathon!).

You should test your installation using our testing scripts. To access these start a shell and run the 
commands:

    git clone https://github.com/larsbratholm/boot-camps.git
    cd boot-camps/setup

before following [these instructions](setup/README.md).

You also need to create a free individual account on 
[GitHub](https://github.com/join). Make sure 
you know your username and password when you arrive

We recommend that you to work through this short tutorial on 
[Beginning Python](http://chryswoods.com/beginning_python) to refresh yourself on Python. 

## Acknowledgements 

Much of this workshop borrows from the great resource that is [Software Carpentry](https://software-carpentry.org/).
