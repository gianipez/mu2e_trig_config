import json
import os

from argparse import ArgumentParser

from codecs import open

def capitalize(word):
    if not word:
        return word
    nLetters=1
    nn = word[0].upper()
    return nn + word[nLetters:]

def generateLogger(args, dictLog, logName):
    loggerFileName       = logName+'Menu.fcl'
    loggerConfigFileName = logName+'Config.fcl'
   
    os.system("chmod 755 {}".format(loggerConfigFileName))
    os.system("chmod 755 {}".format(loggerFileName))
    loggerMenu   = open(loggerFileName, 'w') 
    loggerConfig = open(loggerConfigFileName, 'w') 
    
    tagName = capitalize(logName)
    
    loggerMenu.write(tagName+"Menu: {\n")
    loggerConfig.write(tagName+"Config: {\n")
 
    
    list_of_logger_streams = []
    for k in dictLog:
        if dictLog[k]['enabled'] == 0: continue
        vv = k.split("_")
        streamName = vv[0]
        for i in range(1,len(vv)): streamName = streamName + capitalize(vv[i])
        streamName = streamName+"Output"
        list_of_logger_streams.append(streamName)
        #
        loggerConfig.write("   {}:".format(streamName)+" { \n")
        loggerConfig.write("      module_type: RootDAQOutput \n")
        loggerConfig.write("      SelectEvents : {}\n".format(dictLog[k]['paths']))
        loggerConfig.write("   }\n\n")

    loggerMenu.write("  outputs: [")
    for i in range(len(list_of_logger_streams)):
        k = list_of_logger_streams[i]
        if i!= len(list_of_logger_streams)-1: 
            loggerMenu.write("{},".format(k))
        else:
            loggerMenu.write("{}".format(k))
    loggerMenu.write("]\n")
    loggerMenu.write("  end_paths: [ outputs ] \n")

    loggerConfig.write("}\n")
    loggerConfig.close()
    loggerMenu.write("}\n")
    loggerMenu.close()
  
################################################################################
##
##
##
################################################################################
def generateMenu(args,  dictMenu, menuName):
    trigMenuFileName = menuName+'.fcl'
    psConfigFileName = menuName+'PSConfig.fcl'
    
    os.system("chmod 755 {}".format(trigMenuFileName))
    os.system("chmod 755 {}".format(psConfigFileName))

    trigMenu = open(trigMenuFileName, 'w')
    psConfig = open(psConfigFileName, 'w')
    
    tag = capitalize(menuName)
    trigMenu.write(tag+": {\n")
    trigMenu.write("  trigger_paths: [\n")
    psConfig.write(tag+"PSConfig: {\n")
  
    list_of_calo_trk_paths = []
    for k in dictMenu:
        if dictMenu[k]['enabled'] == 0: continue
        list_of_calo_trk_paths.append(k)
        trigMenu.write('     "{}:{},"\n'.format(dictMenu[k]['bit'], k))
        #
        vv=k.split("_")
        streamName = vv[0]
        for i in range(1,len(vv)): streamName = streamName + capitalize(vv[i])
        psConfig.write("   {}PS:".format(streamName)+" { \n")
        psConfig.write("      module_type: PrescaleEvent \n")
        psConfig.write("      eventModeConfig : {}\n".format(dictMenu[k]['eventModeConfig']))
        psConfig.write("}\n\n")
    #
    print("[generateMenuJSON] TRK+CALO TRIGGER PATHS FOUND (): {}".format(len(list_of_calo_trk_paths), list_of_calo_trk_paths)) 
    #
    psConfig.write("}\n")
    psConfig.close()
    trigMenu.write("  ]\n")
    trigMenu.write("}\n")
    trigMenu.close()
    
    os.system("chmod 444 {}".format(trigMenuFileName))
    os.system("chmod 444 {}".format(psConfigFileName))



def generate(args):
    # trigMenuFileName = 'trigMenuTest.fcl'
    # psConfigFileName = 'trigPSConfigTest.fcl'
    
    # os.system("chmod 755 {}".format(trigMenuFileName))
    # os.system("chmod 755 {}".format(psConfigFileName))

    # trigMenu = open(trigMenuFileName, 'w')
    # psConfig = open(psConfigFileName, 'w')
    
    # trigMenu.write("TrigMenu: {\n")
    # trigMenu.write("  trigger_paths: [\n")
    # psConfig.write("TrigPSConfig: {\n")
    
    with open('data/dictMenu.json') as f:
        conf = json.load(f)
        keys = conf.keys()
        print("[generateMenuJSON] KEYS FOUND: {}".format(keys))
    
        dict_trkcal_triggers = conf['trigger_paths']
        generateMenu(args, dict_trkcal_triggers, 'trigMenu')
        
        # list_of_calo_trk_paths = []
        # for k in dict_trkcal_triggers:
        #     if dict_trkcal_triggers[k]['enabled'] == 0: continue
        #     list_of_calo_trk_paths.append(k)
        #     trigMenu.write('     "{}:{},"\n'.format(dict_trkcal_triggers[k]['bit'], k))
        #     #
        #     psConfig.write("   {}Prescale:".format(k.replace("_",""))+" { \n")
        #     psConfig.write("      module_type: PrescaleEvent \n")
        #     psConfig.write("      eventModeConfig : {}\n".format(dict_trkcal_triggers[k]['eventModeConfig']))
        #     psConfig.write("}\n\n")
            

        #now produce the logger menus
        dict_logger = conf['dataLogger_streams']
        generateLogger(args, dict_logger, 'trigLogger')
        #
        dict_logger = conf['lumiLogger_streams']
        generateLogger(args, dict_logger, 'trigLumiLogger')
        
   
    # psConfig.write("}\n")
    # psConfig.close()
    # trigMenu.write("  ]\n")
    # trigMenu.write("}\n")
    # trigMenu.close()
    
    # os.system("chmod 444 {}".format(trigMenuFileName))
    # os.system("chmod 444 {}".format(psConfigFileName))


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-q", "--quiet",
                        action="store_false", dest="verbose", default=True,
                        help="don't print status messages to stdout")

    args = parser.parse_args()

    generate(args)
