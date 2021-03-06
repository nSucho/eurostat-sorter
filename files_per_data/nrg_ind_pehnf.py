"""
Created on May 2022

@author: Niko Suchowitz
"""
import aux_methods
import pandas as pd
import numpy as np


def nrg_ind_pehnf_main(siec):
    """
    Gross production of electricity and derived heat from non-combustible fuels by type of plant and operator
    (nrg_ind_pehnf)
    :param siec: if SIEC is displayed as code(True) or label(False)
    :type siec: bool
    :return:
    :rtype:
    """
    # read in the file
    tsv_data = pd.read_csv('data/nrg_ind_pehnf.tsv', sep='\t')

    # split the first column
    column_list = ['Plants', 'Operator', 'nrg_bal', 'SIEC', 'Unit', 'Geo']
    tsv_data = aux_methods.sort_col(tsv_data, column_list, True)
    # afterwards delete the column which got split to prevent duplicates
    tsv_data.drop(['plants,operator,nrg_bal,siec,unit,geo\\time'], axis=1, inplace=True)

    # create list from the head of the columns then delete 'Plants', 'Operator', 'nrg_bal', 'SIEC', 'Unit' and 'Geo'
    data_head = list(tsv_data.columns)
    del data_head[0:6]

    # turn the years from columns to rows
    tsv_data = pd.lreshape(tsv_data, {"NetGeneration": tsv_data.filter(regex=r'(19|20)').columns})
    # sort the columns
    tsv_data = aux_methods.sort_col(tsv_data, column_list, False)
    tsv_data = tsv_data.sort_values(by=column_list).reset_index(drop=True)

    # cut emtpy place in elements ending
    for i in range(len(data_head)):
        data_head[i] = data_head[i].strip()
    # add the list to the df, first needs to be same length
    mult = len(tsv_data) / len(data_head)
    i = 1.0
    data_head_copy = data_head.copy()
    while i < mult:
        data_head.extend(data_head_copy)
        i += 1
    tsv_data['DateTime'] = data_head
    tsv_data['DateTime'] = pd.to_datetime(tsv_data['DateTime'], format="%Y").dt.strftime('%Y')
    # set DateTime as index
    tsv_data.set_index('DateTime', inplace=True)

    # replace all ':' with nan
    tsv_data['NetGeneration'] = tsv_data['NetGeneration'].replace(':', np.nan, regex=True)

    # change the code into the whole label
    if not siec:
        tsv_data = aux_methods.siec_to_label(tsv_data)

    # save df
    header = ['Plants', 'Operator', 'nrg_bal', 'SIEC', 'Unit', 'Geo', 'NetGeneration']
    aux_methods.save_data(tsv_data,'nrg_ind_pehnf', header)
