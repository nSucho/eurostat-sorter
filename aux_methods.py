"""
Created on May 2022

@author: Niko Suchowitz
"""
import pandas as pd
import os
import numpy as np


def sort_col(dataframe, column_list, needs_split):
    """
    needs_split = True: split the first column into its individual parts and then move them to the front of the dataframe
    needs_split = false: just sort in order of 'column_list'
    : sort the df in the order of 'column_list'
    :param dataframe:
    :type dataframe: dataframe
    :param column_list:
    :type column_list: list
    :param needs_split:
    :type needs_split: boolean
    :return:
    :rtype: dataframe
    """
    i = 0
    if needs_split:
        dataframe[column_list] = dataframe.iloc[:, 0].str.split(',', expand=True)
        for el in column_list:
            pop_column = dataframe.pop(el)
            dataframe.insert(i, el, pop_column)
            i += 1
    if not needs_split:
        for el in column_list:
            pop_column = dataframe.pop(el)
            dataframe.insert(i, el, pop_column)
            i += 1
    return dataframe


def siec_to_label(dataframe):
    """

    :param dataframe:
    :type dataframe:
    :return:
    :rtype:
    """
    # TODO: can happen that code is not in list, just add here if missing
    # dict
    # read in the file
    siec_df = pd.read_csv('data/siec.csv', sep='\t', names=['Key', 'Value'])
    # set first column to index, then transpose and convert to dict
    siec_df = siec_df.set_index('Key').T
    siec_dict = siec_df.to_dict('list')

    # replace the key with the value
    for key, value in siec_dict.items():
        dataframe['SIEC'] = dataframe['SIEC'].replace(key, value[0], regex=True)
    return dataframe


def save_data(dataframe, file_name, header):
    """
    method to save the files
    :param dataframe:
    :type dataframe: dataframe
    :param file_name:
    :type file_name: string
    :param header:
    :type header: list
    :return:
    :rtype:
    """
    # check if folder exists
    isExist = os.path.exists('data/sorted')
    if not isExist:
        os.makedirs('data/sorted')
    # save as csv
    dataframe.to_csv(
        'data/sorted/'+file_name+'_sorted.csv', sep='\t', encoding='utf-8',
        header=header)
