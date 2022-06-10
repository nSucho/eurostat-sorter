"""
Created on May 2022

@author: Niko Suchowitz
"""
import aux_methods
import pandas as pd
import numpy as np


def nrg_cb_pem_main(siec):
    """
    Net electricity generation by type of fuel - monthly data (nrg_cb_pem)
    :param siec: if SIEC is displayed as code(True) or label(False)
    :type siec: bool
    :return:
    :rtype:
    """
    # read in the file
    tsv_data = pd.read_csv('data/nrg_cb_pem.tsv', sep='\t')

    # split the first column
    column_list = ['SIEC', 'Unit', 'Geo']
    tsv_data = aux_methods.sort_col(tsv_data, column_list, True)
    # afterwards delete the column which got split to prevent duplicates
    tsv_data.drop(['siec,unit,geo\\time'], axis=1, inplace=True)

    # create list from the head of the columns and delete 'SIEC', 'Unit' and 'Geo'
    data_head = list(tsv_data.columns)
    del data_head[0:3]

    # turn the years from columns to rows with filtering the name of the column
    tsv_data = pd.lreshape(tsv_data, {"NetGeneration": tsv_data.filter(regex=r'20').columns})
    # sort the columns
    tsv_data = aux_methods.sort_col(tsv_data, column_list, False)
    # sort the data and drop old index
    tsv_data = tsv_data.sort_values(by=column_list).reset_index(drop=True)

    # cut redundant space from the end of each element(else the following command will create error)
    for i in range(len(data_head)):
        data_head[i] = data_head[i].strip()
    # now add the list to the df
    # mult = variable how often list fits to the dataframe
    mult = len(tsv_data) / len(data_head)
    i = 1.0
    # copy so we don't change original
    data_head_copy = data_head.copy()
    # insert the list into the df
    while i < mult:
        data_head.extend(data_head_copy)
        i += 1
    # make 'DateTime' as the index-column
    tsv_data['DateTime'] = data_head
    tsv_data['DateTime'] = pd.to_datetime(tsv_data['DateTime'], format="%YM%m").dt.strftime('%Y-%m')
    # set DateTime as index
    tsv_data.set_index('DateTime', inplace=True)

    # replace all ':' with nan
    tsv_data['NetGeneration'] = tsv_data['NetGeneration'].replace(':', np.nan, regex=True)

    # change the code into the whole label
    if not siec:
        tsv_data = aux_methods.siec_to_label(tsv_data)

    # save the data
    header = ['SIEC', 'Unit', 'Geo', 'NetGeneration']
    aux_methods.save_data(tsv_data, 'nrg_cb_pem', header)