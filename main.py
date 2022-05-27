"""
Created on May 2022

@author: Niko Suchowitz
"""
import aux_methods

def read_in_data():
    """

    :return:
    """
    # TODO: insert restliche daten
    # type of data to format
    # 1 = Net electricity generation by type of fuel - monthly data (nrg_cb_pem)
    # 2 = Gross production of electricity and derived heat from non-combustible fuels by type of plant and operator
    #     (nrg_ind_pehnf)
    # 3 = (nrg_cb_em)
    # 4 = (nrg_cb_e)
    # 5 = (nrg_ind_peh)
    # 6 = (nrg_ind_pehnf)
    # 7 = (nrg_ind_pehap)
    type_of_data = '2'

    # define output of 'SIEC'
    # True = only show the short code (e.g. 'CF')
    # False = show the whole label (e.g. 'Combustible fuels')
    siec_as_code = False

    if type_of_data == '1':
        aux_methods.nrg_cb_pem(siec_as_code)
    elif type_of_data == '2':
        aux_methods.nrg_ind_pehnf(siec_as_code)


if __name__ == '__main__':
    read_in_data()
