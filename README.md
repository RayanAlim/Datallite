# Datallite - AI4Good

In this project, we seek to expand the existing work that has been conducted by [Jean et al](http://sustain.stanford.edu/predicting-poverty) predicting poverty. We use the [pytorch replication](https://github.com/jmather625/predicting-poverty-replication) done by Jatin Mathur. We explore new countries in West Africa and approach the problem from the angle of education, a topic which is intricately linked with global poverty. 

# Motivation

The stark lack of reliable data in developing countries is a major obstacle to sustainable development. This data drought should be addressed if we hope to inform policy decisions and help direct humanitarian efforts. The use of satellite data may be a way to do this, as remote satellite imagery is becoming increasingly available and inexpensive.

# Data
## World Bank 
We use the same data sources as the original projects: The World Bank, Google Maps, and Night time lights. 

sect3_plantingw3.csv contains education related indicators (ie. dropout rate, high education level obtained, etc.)

cons_agg_wave3_visit2.csv contains the average education consumption aggregate; the variable is ‘edtexp’

nga_householdgeovars_y3.csv contains the geovariables of households as variables 'LAT_DD_MOD' and 'LON_DD_MOD'.

All three files contain a column ‘hhid’ that is the household identification number so you can cross-reference data across different files. The state data dictionary can be found here (https://microdata.worldbank.org/index.php/catalog/2734/data-dictionary/F41?file_name=sect2_harvestw3) under STATE CODE. 

## Schools In Nigeria 
https://grid3.gov.ng/datasets

Complete clean dataset: Schools-with-lat-long.csv

# Contact

Check out our other repo https://github.com/raphaelletseng/datallite-site, and [site in progress](https://raphaelletseng.github.io/datallite-site/).

## Reach out to learn more
Contact our team with any inquiries through our email, datallite.ai@gmail.com.

Follow us on Linkedin at https://www.linkedin.com/company/datallite/about/
