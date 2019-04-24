# # Data Acquisition
#
# 0. Planning
# 1. **Data Acquisition** <- You are here
# 2. Data Preparation
# 3. Data Exploration
# 4. Data Modeling
#
# This script provides functions for downloading the data from the server and
# processing it.
#
# ## Overview
#
# We get the data as a [gzipped](https://en.wikipedia.org/wiki/Gzip) [tar
# archive](https://en.wikipedia.org/wiki/Tar_(computing)), which means that
# while the data consists of multiple files, we download it as a single file.
# This script will uncompress the data and split it into multiple files.
#
# The resulting files are data from fitbit, and each file represents about 30
# days worth of data. Each file has activity and nutrition data in it.
#
# While the files have the `csv` file extension, they are not yet ready to work
# with. Each file consists of multiple sections (which should ideally be
# separate csv files), separated by blank lines. Each section consists of:
#
# - a title, a single line describing the section. These are consistent between
#   the different files, e.g. each csv file has a "Foods" section
# - a header row
# - the data itself
#
# The sections present in each file are:
#
# - Foods
# - Activites
# - Multiple sections indicating nutrition data for individual days
#
# This script will combine all of the various sections together into two
# resulting csv files: `Foods.csv` and `Activities.csv`, which will be loaded
# as data frames when the `get_fitbit_data` function is called.
#
# We are ignoring the indiviual day food logs, which might be a place for
# further future exploration.
import os
import shutil

import pandas as pd

from datetime import datetime
from collections import defaultdict
from typing import NamedTuple, List, Tuple
from urllib.request import urlretrieve
from os import path

#
# ## Implementation
#

# `log` is a simple little function to help us with out logging output. It will
# prepend a timestamp and the name of the file to any passed messages.
def log(msg):
    print(f'[{datetime.now()} acquire.py] {msg}')

# `Section` is a type to represent the sections of the "csv" files that we get
# from fitbit.
Section = NamedTuple('Section', [('title', str),
                                 ('columns', List[str]),
                                 ('data', List[List[str]])])

DATA_URL = 'https://ds.codeup.com/fitbit-data.tar.gz'
TGZ_FILE_PATH = './fitbit-data.tar.gz'
DATA_DIR = './fitbit'

def process_section(section) -> Section:
    '''
    Given a section as a big string, will extract the pieces and return a
    Section object.
    '''
    title, columns, *data = section.split('\n')
    return Section(title=title, columns=columns, data=data)

def get_sections(fp: str) -> List[Section]:
    '''
    Given a filepath, will return a list of the sections in that file.
    '''
    with open(fp) as f:
        contents = f.read().strip()
    # Sections are separated by empty lines, or `\n\n`
    return [process_section(section) for section in contents.split('\n\n')]

def download_data():
    'Download the compressed data from the server'
    log('Downloading data file')
    filepath, _ = urlretrieve(DATA_URL)
    shutil.move(filepath, TGZ_FILE_PATH)

def extract_data():
    'Untar and uncompress the data'
    log('Extracting files')
    shutil.unpack_archive(TGZ_FILE_PATH)

def process_data_and_save_csvs():
    '''
    Run through all the extracted data and put it into a more reasonable format,
    two output csvs.
    '''
    log('Processing data')

    # We'll start by getting a list of the sections in each file
    csvfiles = [f'{DATA_DIR}/{file}' for file in os.listdir(DATA_DIR)]
    processed_files = [get_sections(file) for file in csvfiles]

    # We want to put all the same sections together from each file, e.g. all the
    # food sections should go together. We will use this dictionary to do so.
    output = {'Foods': [], 'Activities': []}

    # After a quick look at the data, we'll just take a look at the `Foods` and
    # `Activites` sections. We can always come back later and look at the other
    # sections.

    # Loop through all of the processed sections and put the sections into the
    # appropriate place in the output dictionary.
    for file in processed_files:
        for section in file:
            if section.title not in output.keys():
                continue
            output[section.title].append(section)

    # Combine all the sections into one big csv file for each group.
    for group in output:
        sections = output[group]
        # The first line of the output csv should be the columns, and the rest
        # of the lines will be the data.
        csv_contents = [sections[0].columns]
        for section in sections:
            csv_contents += section.data
        with open(group + '.csv', 'w') as f:
            f.write('\n'.join(csv_contents))

def get_fitbit_data(cache=True) -> Tuple[pd.DataFrame, pd.DataFrame]:
    '''
    Returns the foods and activites data as data frames.

    By default this will use local csv files if they exist.

    To force a re-download and re-processing of the data, use cache=False
    '''
    if not path.exists('Foods.csv') or not path.exists('Activities.csv') or not cache:
        download_data()
        extract_data()
        process_data_and_save_csvs()
    else:
        log('Reading data from local csvs')
    return pd.read_csv('Foods.csv'), pd.read_csv('Activities.csv')
