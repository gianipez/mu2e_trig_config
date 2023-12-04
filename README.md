# mu2e_trig_config
This package houses the configuration files used to run the art executables in the TDAQ system. The package also includes a python script used to generate the configuration files for the TDAQ art jobs starting from a single JSON file.

## core
The main area houses a series of files used to configure the Online reconstruction and the trigger sequences:
- `trigProducers.fcl`: module instances of the producer modules used in the Online reconstruction
- `trigSequences.fcl`: sequences used in the trigger paths and Online reconstruction
- `trigFilters.fcl`  : module instances of the filter modules used in the Online reconstruction
- `trigServices.fcl` : place holder for teh services used in the Online reco 
- `trigDigiInputEpilog.fcl`: used only for Offline tests where the inout data are in a Digi format (not Fragments)

## data
This directory contains the `trigConf.json` file that organizes in a single JSON file the configuration of the several components needed to run the `art`-based steps of the TDAQ state machine: Online reconstruction, trigger selection, dataloggers, DQM

## python
This directory houses the following scripts:
- `generateMenuJSON.py`: it creates the set of `fcl` files necessary to configure using the `data/trigConf.json` as input:
    1. the trigger sequences that use the tracker+calorimeter data: `trigMenuPSConfig.fcl`, `trigMenu.fcl`
    2. the trigger sequences that use the CRV (+possibly the Trk+Cal) data: `aggMenuPSConfig.fcl`, `aggMenu.fcl`
    3. the datalogger: `trigLoggerConfig.fcl`, `trigLoggerMenu.fcl`
    4. the lumiLogger: `trigLumiLoggerConfig.fcl`, `trigLumiLoggerMenu.fcl`
 
