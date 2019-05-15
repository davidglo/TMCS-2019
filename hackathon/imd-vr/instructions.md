# Code-your-own iMD-VR molecular simulations
This course in focused on creating a virtual reality simulation of the protein-ligand system **neuraminidase and oseltamivir**. The group will be split into 3, where each person will start at a different section in the workflow. You will have ~3 hours to complete each section, before moving on to the next section. If you encounter problems, don't hesitate to ask Becca or Alex for guidance. 

## Useful Terminology 
* NarupaXR - Software produced by the Glowacki Group at the University of Bristol, for running molecular simulations and interacting with them using Virtual Reality
* Amber/AmberTools - The collective name for a suite of programmes that allow users to carry out molecular dynamics simulations, particularly on biomolecules
* OpenMM - A high performance toolkit for molecular simulation
* VMD - Common visualiser for viewing molecular trajectories in a variety of formats
* pdb file - File format for storing protein structures, containing atom positions, bonds and information about which amino acids are present
* prmtop file - The topology file for the system of interest which includes the following kind of information: connectivity, atom names, atom types, residue names, and charges
* inpcrd file - The coordinate file for the system
* xml file - Standard file format for storing information - HMTL (language used to write web pages) is an example of XML


## Set-up
For this course, you will need the following packages installed:
* AmberTools19 (installed through Conda)
* OpenMM (installed through Conda)
* VMD

## Instructions
### Part 1: Parameterising your molecule  

1. The first step in being able to visualise a system in VR is making sure your system is parameterised correctly. The protein-ligand system we will be looking at is neuraminidase and oseltamivir (commonly known as Tamiflu). [Download the pdb here](https://github.com/davidglo/TMCS-2019/tree/master/hackathon/imd-vr) titled 3NSS.pdb. Note that this pdb contains the protein, ligand, ions, and a water box.

2. Now that you have your system, you must clean it up and make sure it is parameterised correctly! To do this, we will use AmberTools 19. Make sure you have installed AmberTools19, which can be done through [cuda](http://ambermd.org/GetAmber.php).

3. Once AmberTools has been installed, this should give you access to a programme called tLEaP. This is the primary programme to create a new system in Amber, or to modify existing systems. The tutorial that goes through the steps you need to complete to paramterise your protein and ligand is given [here](http://ambermd.org/tutorials/pengfei/index.htm), where you should **start at step 3** in the example at the bottom of the page. The [Amber documentation](http://ambermd.org/doc12/Amber18.pdf) is also very helpful in understanding what tLEaP is used for, should you be curious. **Note that you should NOT solvate the system in a perdiodic box of water, as the VR uses implicit solvent, so any comments relating to water can be skipped**

4. Once you have successfully created new Amber topology (.prmtop) and coordinate (.inpcrd) files for your system, you should check that the system looks sensible by loading it into VMD (for example, by highlighting certain parts of the system separately, such as the protein and the ligand). A useful introductory guide to VMD is given [here](https://chryswoods.com/dynamics/visualisation/mouse.html).


### Part 2: Writing OpenMM Scripts 

1. In this section, you will take .prmtop and .inpcrd files generated in Amber for the neuraminidase-oseltamivir system and convert them into files that NarupaRX can understand. The Amber files you will need (3NSS.prmtop and 3NSS.inpcrd) are [here](https://github.com/davidglo/TMCS-2019/tree/master/hackathon/imd-vr) if you are beginning at this part of the course, OR the files you have generated in the previous step. For this section, you will need to write your own python script which calls OpenMM, high performance toolkit for molecular simulation. You can [download OpenMM through anaconda here](https://anaconda.org/omnia/openmm).

2. Once you have installed OpenMM, you can now start writing your python script that creates the neccessary files to put your system into NarupaXR. This is done by running a *very small* amount of molecular dynamics (MD) through OpenMM to create a new coordinate (.pdb) file and topology (.xml). The OpenMM documentation provides a introduction on how to write a script to run MD [using Amber files](http://docs.openmm.org/latest/userguide/application.html#using-amber-files). 

You should use their example script as a guide, but you are encourgaed to investigate each of the parameters and change them around - the documentation does a good job of explaining what each part of the script does. For example, as the system has no explicit solvent molecules, you should add something that adds some implicit solvent to the system. 

**Note that the OpenMM example script in the documentation only gives an output pdb file. To generate an output .xml file, the following lines of code will have to be added to the end of your script**
```
outputFile = 'systemname.xml'
system_xml = mm.XmlSerializer.serialize(system)
with open(outputFile, 'w') as f:
    f.write(system_xml)
```

3. Once your script runs and you get an output .xml and .pdb file, you are ready to put your system into VR. The VR is split into two parts: the *frontend* and the *server*. The frontend is the part which visualises the system you have sent to the VR. The server is the part which actually reads in the files you want to visualise. To be able to see your molecule in VR you must send all of the information about it to the server in a file which wraps everything together - an example of a very basic version is [here](https://github.com/davidglo/TMCS-2019/blob/master/hackathon/imd-vr/vr_openmm_template.xml). To this example script, add the path to your files and then look at the [documentation](https://intangiblerealities.gitlab.io/narupa/index.html) to see if you can add/modify any parts of this script that could be useful.


### Part 3: Manipulation in NarupaXR 

**The VR is launched from the Alienware laptops, but you should save your files to the TMCS git repo so you can add them to the folder TMCS-2019 on the Alienwares**

1. This section is focused on i) editing the script which contains all of the information that NarupaXR needs to be able to visualise your system and ii) making selections and getting to grips with molecular manipulation in VR. First, on the VR alienware computers, navigate to the the programme itch, NarupaXR, and then click on show local files. Then navigate to server/Assets/Simulations/TMCS-2019 and copy a version a version of [this server file](https://github.com/davidglo/TMCS-2019/tree/master/hackathon/imd-vr) to this folder, OR copy your own generated 3NSS xml file from the previous section. 

This is a very basic version of the server script for neuraminidase, which you will have to add the path to your own files, or the xml and pdb files for vr located [here](https://github.com/davidglo/TMCS-2019/tree/master/hackathon/imd-vr) - there are many things which can be added to change your experience in VR. 

Check out the [VR documentation](https://intangiblerealities.gitlab.io/narupa/index.html) to see what else can be added to this file or edited! *hint: how can you record what pathways you are going to generate in VR?* **Once you have finished learning about this file and editing it, make sure you save it back in the itch TMCS-2019 folder under the name 3NSS_yourname.xml**

2. Now that you have your server file you are ready to launch your VR simulation! This can be done by navigating to the programme itch, then clicking on NarupaXR, then Launch -> Server and VR. Once in VR, you are free to play around with your simulation! You will notice that there are two types of mode: Interaction Mode and Selection Mode. Interaction Mode allows you to (you guessed it) interact with your simulation, whereas Selection mode allows you to select and change various parts of your system. Whilst in Interaction mode, try undocking and redocking your drug, or unfolding the protein. Whilst in Selection Mode have a go at the following things:

* Select oseltamivir and group all the atoms together
* Colour in residues 70 and 71 a different colour
* Make the remaining protein backbone rigid and a different color
* Choose different renderers (i.e. ball and stick etc.) for each of the selections mentioned above

Have fun! See what selections and trajectories you can generate. 

### If you have any questions, please do not hesitate to ask Becca or Alex! 

