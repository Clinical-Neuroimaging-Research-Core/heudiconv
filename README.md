# heudiconv

heudiconv is a DICOM converter used to organize brain imaging data into BIDS and convert data into NiFti files.

heudiconv is easiest used in a container - such as Docker or Singularity.

Check out our powerpoint on heudiconv here: https://sites.brown.edu/cnrc-core/resources-and-help/

Look through the heudiconv [website](https://heudiconv.readthedocs.io/en/latest/) and [github](https://github.com/nipy/heudiconv) for more help!

## heudiconv basic steps

### 1. Generate the initial heuristic file
   - This first step will generate a .tsv file of all the dicom files that you will then use to create a heuristic file
   - Essentially, run the heudiconv command with out the "convert" flag activated

### 2. Look at the dicominfo.tsv file
  - Running heudiconv creates a hidden folder in your output directory
  - Reveal the hidden files by using ``` cmd + . ``` (mac) or using ``` ls -a ``` through the terminal
  - Look for the dicominfo_.tsv file and open it

### 3. Create a heuristic script
  - The heuristic script is a python script that provides the heudiconv program information about your study's dicoms

### 4. Run heudiconv with the new heuristic script added to command
  - Add the heuristic script to the heudiconv command
  - Make sure to update the converter flag       

## heudiconv on CCV

- heudiconv is run through a singularity container on CCV
- You need to download the singularity container to your CCV through the terminal using: 
``` 
singularity pull docker://nipy/heudiconv
```
- This will create the heudiconv_latest.sif container in your home directory

## heudiconv with docker

- Install docker on your local computer and make sure to increase memory and CPUs utilization
- Add heudiconv image to docker by typing in terminal:
```
docker pull nipy/heudiconv
```
- This will create the heudiconv image in the docker container 

For step by step guide, please look our powerpoint on heudiconv here: https://sites.brown.edu/cnrc-core/resources-and-help/
