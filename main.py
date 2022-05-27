"""
Created on May 2022

@author: Niko Suchowitz
"""
import nrg_cb_pem
import nrg_ind_pehnf
import nrg_cb_em
import nrg_cb_e
import nrg_ind_peh
import nrg_ind_pehap


def read_in_data():
    """

    :return:
    """
    # TODO: insert the other data
    # type of data to format
    # 1 = Net electricity generation by type of fuel - monthly data (nrg_cb_pem)
    # 2 = Gross production of electricity and derived heat from non-combustible fuels by type of plant and operator
    #     (nrg_ind_pehnf)
    # 3 = (nrg_cb_em)
    # 4 = (nrg_cb_e)
    # 5 = (nrg_ind_peh)
    # 6 = (nrg_ind_pehnf) # TODO: doppelt
    # 7 = (nrg_ind_pehap)
    type_of_data = '1'

    # define output of 'SIEC'
    # True = only show the short code (e.g. 'CF')
    # False = show the whole label (e.g. 'Combustible fuels')
    siec_as_code = True

    if type_of_data == '1':
        nrg_cb_pem.nrg_cb_pem_main(siec_as_code)
    elif type_of_data == '2':
        nrg_ind_pehnf.nrg_ind_pehnf_main(siec_as_code)
    if type_of_data == '3':
        nrg_cb_em.nrg_cb_em_main(siec_as_code)
    elif type_of_data == '4':
        nrg_cb_e.nrg_cb_e_main(siec_as_code)
    if type_of_data == '5':
        nrg_ind_peh.nrg_ind_peh_main(siec_as_code)
    # TODO: 6 doppelt
    elif type_of_data == '7':
        nrg_ind_pehap.nrg_ind_pehab_main(siec_as_code)


if __name__ == '__main__':
    read_in_data()
