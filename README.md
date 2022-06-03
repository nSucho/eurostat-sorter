# eurostat-sorter

This project reads in the downloaded data from 'https://ec.europa.eu/eurostat/web/main/data/database', changes the
data-type from 'tsv' into 'csv' while converting it into processable form.
Therefore, the .tsv-data has to be copied into the **'data'**-folder and has to have the same name as the corresponding 
.py-file. Choose in the **'main.py'** the data to convert and the type of 'SIEC' (code/label).

**Example:** For **'Net electricity generation by type of fuel - monthly data'** the file need to be named **'nrg_cb_pem.tsv'**. 
In the **'main.py'** choose **type_of_data = '1'** and to have only the code of SIEC **siec_as_code = True**.


## Right now working for:
* Net electricity generation by type of fuel - monthly data (nrg_cb_pem)
* Gross production of electricity and derived heat from non-combustible fuels by type of plant and operator
      (nrg_ind_pehnf)
* Supply, transformation and consumption of electricity - monthly data (nrg_cb_em)
* Supply, transformation and consumption of electricity (nrg_cb_e)
* Gross and net production of electricity and derived heat by type of plant and operator (nrg_ind_peh)
* Production of electricity and heat by autoproducers, by type of plant (nrg_ind_pehap)


## SIEC-list downloaded at:
* https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?sort=1&dir=dic%2Fen
* **Name:** siec.dic
