# mu2e_trig_config
prototype for the mu2e_trig_config package

## Config
The main area houses a series of files used to configure the Online reconstruction and the trigger sequences:
- `trigProducers.fcl`:
- `trigSequences.fcl`:
- `trigProducers.fcl`:
- `trigFilters.fcl`:
- `trigServices.fcl`:
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
 - `upload_table.py`: it uploads the `data/trigConfig.json` JSON file to the MongoDb
 - `read_table.py`: it downloads the table specified at run time by the option `-v `
