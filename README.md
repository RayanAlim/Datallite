# AI4Good Lab - Project

In this project, we seek to expand the existing work that has been conducted by [Jean et al](http://sustain.stanford.edu/predicting-poverty) predicting poverty. We use the [pytorch replication](https://github.com/jmather625/predicting-poverty-replication) done by Jatin Mathur. We explore new countries in West Africa and approach the problem from the angle of education, a topic which is intricately linked with global poverty. 

## Motivation

The stark lack of reliable data in developing countries is a major obstacle to sustainable development. This data drought should be addressed if we hope to inform policy decisions and help direct humanitarian efforts. The use of satellite data may be a way to do this, as remote satellite imagery is becoming increasingly available and inexpensive.

## Data

We use the same data sources as the original projects: The World Bank, Google Maps, and Night time lights. 

sect3_plantingw3.csv contains education related indicators (ie. dropout rate, high education level obtained, etc.)

cons_agg_wave3_visit2.csv contains the average education consumption aggregate; the variable is ‘edtexp’

nga_householdgeovars_y3.csv contains the geovariables of households

All three files contain a column ‘hhid’ that is the household identification number so you can cross-reference data across different files. 



