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

[github-shield]: https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white
[github-url]: https://github.com/Nara-On
