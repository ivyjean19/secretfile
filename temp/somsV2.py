
import sys
import ConvertSomsRaw as CSR
import pandas as pd
import numpy as np
from datetime import timedelta as td
from datetime import datetime as dt
import sqlalchemy
from sqlalchemy import create_engine
import sys
import requests
    
def getDF():

        site = sys.argv[1]
        fdate = sys.argv[2]
        tdate = sys.argv[3]
        nid = sys.argv[4]
#        site = 'agbsb'
#        fdate = '2016-04-10'
#        tdate = '2016-04-11'
#        nid = '2'
        df= CSR.getsomsrawdata(site+'m',nid,fdate,tdate)
        
        
        df = pd.DataFrame(df,columns=['raw'])
        #df.index = df.ts
        #print df
        dfajson = df.reset_index().to_json(orient="records",date_format='iso')
        dfajson = dfajson.replace("T"," ").replace("Z","").replace(".000","")
        print dfajson
    
getDF();