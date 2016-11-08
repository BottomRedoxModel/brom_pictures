# BROM_pictures

## About
BROM_pictures - is a GUI application written on Python 2.7  to visualise results of running Bottom RedOx Model (NetCDF output) - 
fully coupled benthic-pelagic model for simulation of seasonal anoxia and its impact to environment.
(http://www.geosci-model-dev-discuss.net/gmd-2015-239/gmd-2015-239.pdf)

## How to use
1. For running this application you should have Python 2.7 installed.
2. BROM_Pictures uses third-party Python modules: NumPy and MatPlotLib, and PyQt4. These also need to be installed to run script.
3. Clone this repository into your computer.  
4. When you run main.py, dialog will be opened. Choose BROM output file (Usually it is called BROM_out.nc).
5. You can view annual distributions for model data. 
   Push the buttons 'PO4,SO4,O2 annual', 'T,S,Kz annual', 'NO2,NO3,NH4 annual', 'Si,pH annual', 'Mn,Fe,H2S annual',
   
##### Example of figures   
[![image.png](https://s17.postimg.org/gpqvxp1z3/image.png)](https://postimg.org/image/3llbl09x7/)

6. Also you can view all distributions for choosen day. 
   Choose at spin box the number of day you are interested in and press button 'All(1) chosen day' or 'All(2) chosen day'
   
##### Example of figures 
![Figure example](http://i.imgur.com/hU84LUU.png)

