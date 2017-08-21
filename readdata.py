'''
Created on 14. des. 2016

@author: ELP
'''
from netCDF4 import Dataset
import main
def readdata_brom(self,fname): 

    fh = Dataset(fname)
    self.depth = fh.variables['z'][:] 
    self.depth2 = fh.variables['z2'][:] #middle points
    self.alk =  fh.variables['Alk'][:,:,:]
    self.temp =  fh.variables['T'][:,:]
    self.sal =  fh.variables['S'][:,:]
    self.kz =  fh.variables['Kz'][:,:]
    self.dic =  fh.variables['DIC'][:,:]
    self.phy =  fh.variables['Phy'][:,:]
    self.het =  fh.variables['Het'][:,:]
    self.no3 =  fh.variables['NO3'][:,:]
    self.po4 =  fh.variables['PO4'][:,:]
    self.nh4 =  fh.variables['NH4'][:,:]
    self.pon =  fh.variables['PON'][:,:]
    self.don =  fh.variables['DON'][:,:]
    self.o2  =  fh.variables['O2'][:,:]
    self.mn2 =  fh.variables['Mn2'][:,:]
    self.mn3 =  fh.variables['Mn3'][:,:]
    self.mn4 =  fh.variables['Mn4'][:,:]
    self.h2s =  fh.variables['H2S'][:,:]
    self.mns =  fh.variables['MnS'][:,:]
    self.mnco3 =  fh.variables['MnCO3'][:,:]
    self.fe2 =  fh.variables['Fe2'][:,:]
    self.fe3 =  fh.variables['Fe3'][:,:]
    self.fes =  fh.variables['FeS'][:,:]
    self.feco3 =  fh.variables['FeCO3'][:,:]
    self.no2 =  fh.variables['NO2'][:,:]
    self.s0 =  fh.variables['S0'][:,:]
    self.s2o3 =  fh.variables['S2O3'][:,:]
    self.so4 =  fh.variables['SO4'][:,:]
    self.si =  fh.variables['Si'][:,:]
    self.si_part =  fh.variables['Sipart'][:,:]
    self.baae =  fh.variables['Baae'][:,:]
    self.bhae =  fh.variables['Bhae'][:,:]
    self.baan =  fh.variables['Baan'][:,:]
    self.bhan =  fh.variables['Bhan'][:,:]
    self.caco3 =  fh.variables['CaCO3'][:,:]
    self.fes2 =  fh.variables['FeS2'][:,:]
    self.ch4 =  fh.variables['CH4'][:,:]
    self.ph =  fh.variables['pH'][:,:]
    self.pco2 =  fh.variables['pCO2'][:,:]
    self.om_ca =  fh.variables['Om_Ca'][:,:]
    self.om_ar =  fh.variables['Om_Ar'][:,:]
    self.co3 =  fh.variables['CO3'][:,:]
    self.ca =  fh.variables['Ca'][:,:]
    self.time =  fh.variables['time'][:]
    fh.close()
 
    
    