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
    # dict
    replace_dict = {'TOTAL': 'Total', 'CF': 'Combustible fuels', 'CF_R': 'Combustible fuels- renewable',
                    'CF_NR': 'Combustible fuels- non-renewable', 'C0000': 'Coal and manufactured gases',
                    'G3000': 'Natural gas', 'O4000XBIO': 'Oil and petroleum products(excluding biofuel portion)',
                    'RA100': 'Hydro', 'RA110': 'Pure hydro power', 'RA120': 'Mixed hydro power',
                    'RA130': 'Pumped hydro power', 'RA200': 'Geothermal', 'RA300': 'Wind', 'RA310': 'Wind on shore',
                    'RA320': 'Wind off shore', 'RA400': 'Solar', 'RA410': 'Solar thermal',
                    'RA420': 'Solar photovoltaic', 'RA500_5160': 'Other renewable energies',
                    'N9000': 'Nuclear fuels and other fuels n.e.c.', 'X9900': 'Other fuels n.e.c.'}
    # replace the key with the value
    for key, value in replace_dict.items():
        dataframe['SIEC'] = dataframe['SIEC'].replace(key, value, regex=True)
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
