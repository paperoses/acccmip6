# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 01:58:23 2019

@author: Taufiq
"""

from acccmip6.utilities.c6db import SearchDB
from acccmip6.utilities.CMIP6_database import CMIP6DB
from acccmip6.utilities.util import color

def SearchCmip6(**kwargs):
        _var = kwargs.get('variable', None)
        _mod = kwargs.get('model', None)
        _exp = kwargs.get('experiment', None)
        _freq = kwargs.get('frequency', None)
        _realm = kwargs.get('realm', None)
        _check = kwargs.get('check', None)
        _desc = kwargs.get('desc', None)
        
        print('\n'+color.UNDERLINE+color.BOLD+'TIPS:'+color.END+" If you are not sure about what you are looking for use CMIP6DB module \n      to look for currently avalable models/experiments/variables and so on . . ."+color.END)
        
        search=SearchDB()
        if (_check == 'Yes') or (_check == 'yes'):
            search._set_check('Yes')
        else:
            search._set_check('No')
        if (_mod != None):
            try:
                search.model=_mod
            except ValueError as ve:
                print(color.LRED+"\n<<No options available.>>\n\nPlease make sure "+str(_mod)+" exists."+color.END)
                print(ve)
            except Exception as ee:
                print('\nDid you mean any of the above?')
                print(ee)
        if (_exp != None):
            try:
                search.experiment=_exp
            except ValueError as ve:
                print(color.LRED+"\n<<No options available.>>\n\nPlease make sure "+str(_exp)+" exists."+color.END)
                print(ve)
            except Exception as ee:
                print('\nDid you mean any of the above?')
                print(ee)
        if (_var != None):
            try:
                search.variable=_var
            except ValueError as ve:
                print(color.LRED+"\n<<No options available.>>\n\nPlease make sure "+str(_var)+" exists."+color.END)
                print(ve)
            except Exception as ee:
                print('\nDid you mean any of the above?')
                print(ee)
        if (_freq != None):
            try:
                search.frequency=_freq
            except ValueError as ve:
                print(color.LRED+"\n<<No options available.>>\n\nPlease make sure "+str(_freq)+" exists."+color.END)
                print(ve)
            except Exception as ee:
                print('\nDid you mean any of the above?')
                print(ee)
        if (_realm != None):
            try:
                search.realm=_realm
            except ValueError as ve:
                print(color.LRED+"\n<<No options available.>>\n\nPlease make sure "+str(_realm)+" exists."+color.END)
                print(ve)
            except Exception as ee:
                print('\nDid you mean any of the above?')
                print(ee)
        
        info = search.get_info()
        
        print(color.LGREEN+"\n\n Currently available models based on your search: \n\n"+color.END,info.mod)
        print(color.LGREEN+"\nCurrently available variables based on your search: \n\n"+color.END,info.var)
        print(color.LGREEN+"\nCurrently available experiments based on your search: \n\n"+color.END,info.exp,"\n\n")
        print(color.LGREEN+"\nNumber of files:"+color.END, len(search.get_links()),"\n\n")
        if (_desc != None):
            print(color.YELLOW+"< < < Here are the experiment descriptions > > >\033[0m")
            for item in info.exp:
                print("\n\n"+color.CYAN+str(item)+":\033[0m \n"+CMIP6DB._get_definition(item))
        print(color.RED+"\n\n       <===============Exiting now!================>\033[0m\n\n")
        raise SystemExit