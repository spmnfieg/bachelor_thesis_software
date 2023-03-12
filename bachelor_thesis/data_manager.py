
from builtins import print

import time
import numpy as np

import feature_selector
import pandas as pd

"""
@author : Anonymous
"""

import glob, os
from Constants import *


def getBugCount( xDF):

    return len(xDF[xDF['Buggy'] > 0])

def getCleanCount( xDF):

    return len(xDF[xDF['Buggy'] == 0])



PROJECTS_155 = ['ActionBarSherlock','beets','Cachet','django-rest-framework','fat_free_crm','fresco','mopidy','proxygen','pyton','redisson','Signal-Android','SignalR','Twig','wp-cli','yii']




def getProjectNames():
    return PROJECTS_155


"""
Constants
"""


data_attribute = 'author_date_unix_timestamp'

class project(object):

    def __init__(self, name):
        self.name = name
        self.releases = getReleases(name)

        tempStartDate = math.inf
        tempEndDate = 0

        for r in self.releases:
            tempStartDate = min(tempStartDate, r.getStartDate())
            tempEndDate= max(tempEndDate, r.getReleaseDate())

        self.years = (tempEndDate - tempStartDate)/one_year


    def getYears(self):

        return self.years


    def getReleases(self):
        return self.releases

    def getName(self):
        return self.name

    def getAllChanges(self):

        changesDF = None
        changes = 0
        for r in self.releases:


            changes += len(r.getChanges())

            if changesDF is None:
                changesDF = r.getChanges()
            else:
                changesDF = changesDF.append(r.getChanges())



        return changesDF


class release(object):

    def __init__(self,release_date, changes, startDate):

        self.release_date = release_date
        self.changes = changes
        self.startDate = startDate


    def getReleaseDate(self):
        return self.release_date

    def getStartDate(self):
        return self.startDate

    def getChanges(self):
        return self.changes

    def __str__(self):
        return str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.release_date)) + " : "+str(
                len(self.changes)))



def getReleasesBefore(project, releaseDate):

    pastReleases = []

    for r in project.getReleases():

        if r.getReleaseDate() < releaseDate:
            pastReleases.append(r)


    return pastReleases

def getReleases(p):



    df = pd.read_csv('./data/'+p+'.csv')

    releaseObjects = []


    prevPeriod = None

    releaseDates = pd.read_csv('./data/releases/' + p + ".csv")['releases'].values.tolist()


    added = CONSIDER_FIRST_X_RELEASES

    for currentPeriod in releaseDates:

        if added <= 0:
            break

        if prevPeriod is None:
            prevPeriod = currentPeriod
            continue
        else:
            period = [prevPeriod, currentPeriod]


            tempDF = df[ (df[data_attribute] > prevPeriod) & (df[data_attribute] <= currentPeriod) ]


            rDF = formatDF(tempDF)

            if len(rDF) > 1:
                releaseObjects.append(release(currentPeriod, rDF, tempDF['author_date_unix_timestamp'].min()))
                added -= 1

            prevPeriod = currentPeriod


    return releaseObjects

def get_features(df):
    fs = feature_selector.featureSelector()
    df, _feature_nums, features = fs.cfs_bfs(df)
    return df, features


def formatDF(rdf):

    """
    Works for QT and OPEN-STACK
    releaseDF = rdf.copy(deep=True)
    releaseDF = releaseDF[['la','ld','nf','nd','ns','ent','revd','nrev','rtime','tcmt','hcmt','self',
                    'ndev','age','nuc','app','aexp','rexp','oexp','arexp','rrexp','orexp','asexp','rsexp','osexp','asawr','rsawr','osawr',
                    'commit_id','author_date','fixcount',
                    'bugcount']]
    releaseDF = releaseDF.drop(labels=['commit_id','author_date','fixcount'], axis=1)
    releaseDF = releaseDF.fillna(0)
    releaseDF.rename(columns={'bugcount': 'Buggy'}, inplace=True)
    """

    releaseDF = rdf.copy(deep=True)

    releaseDF = releaseDF[ [ 'author_date_unix_timestamp', 'ns','nd','nf','entropy', 'la','ld','lt','ndev','age','nuc','exp','rexp', 'sexp' , 'fix', 'contains_bug' ] ]


    dropList = ['author_date_unix_timestamp']

    releaseDF = releaseDF.drop(labels=dropList, axis=1)
    releaseDF = releaseDF.fillna(0)

    releaseDF = releaseDF[ (releaseDF['contains_bug'] == True) | (releaseDF['contains_bug'] == False) ]

    releaseDF.rename(columns={'contains_bug': 'Buggy'}, inplace=True)


    return releaseDF





def getProject(p):
    return project(p)

