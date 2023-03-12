[![DOI](https://zenodo.org/badge/332297400.svg)](https://zenodo.org/badge/latestdoi/332297400)

# [Paper: Early Life Cycle Software Defect Prediction. Why? How?](https://arxiv.org/pdf/2011.13071.pdf) 

<img src="https://upload.wikimedia.org/wikipedia/commons/7/73/Alarm_Clock_Vector.svg" width="350">

Many researchers assume that, for software analytics,  "more data is better". We write to show that, at least for learning defect predictors, this may not be true. 

To demonstrate this,  we analyzed hundreds of popular GitHub projects. These projects ran for 84  months and contained   3,728  commits (median values).
Across these projects, most of the defects occur very early in their life cycle. Hence, defect predictors learned from the first 150 commits and four months  perform just as well as anything else. This means that, at least for the projects studied here,  after the first few months, we need not continually update our defect prediction models.

We hope these results inspire other researchers to adopt a "simplicity-first" approach to their work. Some domains require a complex and data-hungry analysis. But before   assuming complexity, it is prudent to check   the raw data looking for  "short cuts" that can simplify the   analysis. 


# Replication:

## Prerequisites

* Linux Terminal
* python 2.7.5 and python 3.6.7
* Git support

### On your Linux terminal

1. $ `git clone https://github.com/snaraya7/early-defect-prediction-icse21.git`
1. $ `cd early-defect-prediction-icse21`
1. $ `pip3 install -r requirements.txt`

## Follow the steps in the screenshot (below):

<img src="https://github.com/snaraya7/early-defect-prediction-icse21/blob/master/images/scratch.PNG" width="900">

## Dataset

#### Project csv's are available [here](https://github.com/snaraya7/early-defect-prediction-icse21/tree/master/data) and its associated release csv's are available [here](https://github.com/snaraya7/early-defect-prediction-icse21/tree/master/data/releases)

