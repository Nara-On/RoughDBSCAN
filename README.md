[![GitHub][github-shield]][github-url]
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

<br />
<div align="center">
  <h3 align="center">Rough DBSCAN Implementation</h3>
  <p align="center">
    An implementation of the paper <br />
    <b> Rough-DBSCAN: A fast hybrid density based clustering method for large data sets </b> <br />
    by  P. Viswanath and V. Suresh Babub
    <br />
    <br />
</div>

<br >

## Author
Marina Bermúdez Granados - <a href="https://github.com/nara-on">nara-on</a> <br />

<br >

## Project Structure

      .
      ├── datasets                       # Directory containing the different datsets
      ├── experiments                    # Directory containing all the main experiments
      ├── models                         # Directory containing the models: Counted-Leaders, DBSCAN, and Rough-DBSCAN
      ├── tests                          # Directory containing all the tests, single runs of DBSCAN and Rough-DBSCAN
      ├── utils                          # Directory containing different functionalities 
      └── visuals
          ├── experiments                # Directory for the results of the experiments
          └── tests                      # Directory for the results of the tests

<br >

## Images 
<br />
<div align="center">
   <h4>Classification of Data Points in Rough-DBSCAN</h4>
   <img src="https://github.com/Nara-On/RoughDBSCAN/blob/main/visuals/dense_points.png" width="800">
   <br />
   <br />
   <br />
   
   <h4>Some Rough-DBSCAN Results in Blobs Dataset with Different Parameters</h4>
   <img src="https://github.com/Nara-On/RoughDBSCAN/blob/main/visuals/tests/blobs/1000_E0.5_T30_R0.2/rdbscan_all_1000_E0.5_T30_R0.2.jpg" width="800">
   <img src="https://github.com/Nara-On/RoughDBSCAN/blob/main/visuals/tests/blobs/1000_E0.5_T30_R0.5/rdbscan_all_1000_E0.5_T30_R0.5.jpg" width="800">
   <br />
   <br />
   <br />
   
   <h4>Some Rough-DBSCAN Results in Banana Dataset with Different Parameters</h4>
   <img src="https://github.com/Nara-On/RoughDBSCAN/blob/main/visuals/tests/banana/4000_E0.5_T8_R0.25/rdbscan_all_E0.5_T8_R0.25.jpg" width="800">
   <img src="https://github.com/Nara-On/RoughDBSCAN/blob/main/visuals/tests/banana/4000_E0.2_T8_R0.5/rdbscan_all_E0.2_T8_R0.5.jpg" width="800">
</div>

<br />
<br />

## Version History
* Updates to README.md
    * Improvements for GitHub 
* Requirements
    * Update to requirements.txt 
* Correction
    * Fixed typo
* More details
    * Extra experiments for PenDigits dataset 
* Details
    * Minor optimizations 

<br />

* Scratch Experiments
    * Uploaded scratch results datasets for Banana, Blobs, Letter, PendDigits, and Shuttle datasets

<br />

* Sklearn Experiments + Fixing issues
    * Added sklearn code to experiment files
    * Uploaded sklearn results datasets for Banana, Blobs, Letter, and Shuttle datasets
    *  Minor corrections to timelimits in DBSCAN
* Experiments PenDigits + Optimizations
    * Developed experiment code for Banana dataset
    * Renamed DBSCAN class to DBSCAN_scratch
    * Updated testing code
    * Uploaded results dataset for leaders
    * Uploaded sklearn results dataset for PenDigits dataset
* Experiment Leaders vs Patterns
    * Updated hyperparameters in experiments
    * Added default parameters to synthetic dataset
    * Developed plotting functions for synthetic datasets
    * Uploaded visuals for Banana and Blobs dataset
    * Uploaded visuals for Leaders experiment

<br />

* Checkpoint Experiments
    * Tests folder created
    * Moved testing code to tests folder
    * Developed experiment code for blobs dataset
    * Developed experiments code to test the Leaders
    * Added timelimit to DBSCAN
    * Moved plotting resources to separate file in utils
    * Moved previous results to a separate tests folder in visuals
    * Uploaded PenDigits results in a separate experiments folder in visuals
    * Uploaded dense points documentation to visuals

<br />

* Testing Done
    * Updated PenDigits dataset
    * Developed experiment code for PenDigits
    * Updating hyperparameters for rest of experiments
    * Reorganized fit and predict of DBSCAN
    * Optimized find_N function
    * Reorganization of visuals folder with new content

<br />

* Checkpoint: Real datasets tests
    * Updates to Shuttle dataset
    * Developed experiment code for Letter and SHuttle datasets
    * Minor printing modifications to DBSCAN and Rough_DBSCAN
    * Minor updates to plot generation and dataset loading util functions
    * Upload first Letter and Shuttle experiments
* Fixed N, RDBSCAN Synthetic Tests
    * Developed find_rough_N utils function
    * Updated find_N utils funtcion
    * Updated Counted_Leaders class
    * Updates to DBSCAN for dual implementation of DBSCAN and Rough_DBSCAN
    * Updates to Rough_DBSCAN
    * Updates to plotting util functions
    * Renamed experiment codes to tests
    * Uploaded first set of visual results with different parameters
* Refactor Experiments
    * Developed code for the experiments of the remianing dataset
    * Developed dataset generation utils function for each dataset
    * Developed experiments utils function
    * Developed plotting utils function
    * Updated old results

<br />

* Mini Refactor Experiments
    * Datasets folder created
    * Upload PenDigits, Letter, and Shuttle datasets to datasets folder
    * Update DBSCAN for fit_predict function
    * Update Rough_DBSCAN for fit_predict function
    * Developed generate_results utils function
    * Uploaded and refactored visuals of banana and blobs datasets

<br />

* Initial fit Rough DBSCAN
    * Experiments folder created
    * Visuals folder created
    * Updates to Counted_Leaders class
    * Updates to Rough_DBSCAN class
    * Developed separate DBSCAN class
    * Developed find_N utils function
    * Developed code to experiments in banana and blobs dataset
    * Uploaded first results of experiments in banana and blob dataset

<br />

* Counted Leaders
    * Updates to Counted_Leaders class
    * Updates in coincidence function
* Developing Counted Leaders
    * First version of Counted Leaders
    * Developed coincidence utils function
    * Update README.md
* Basic structure
    * Models folder created
    * Utils folder created
    * Base code for Counted_Leaders and Rough_DBSCAN classes
    * First version of README.md
    * First version of requirements.txt
    * Added gitignore file
* Initial Commit
    * Initial Release


[github-shield]: https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white
[github-url]: https://github.com/Nara-On
