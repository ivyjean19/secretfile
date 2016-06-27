import pandas as pd
import numpy as np
from datetime import timedelta as td
from datetime import datetime as dt
import sqlalchemy
from sqlalchemy import create_engine
import sys
import requests
    

def getDF():

    rsite = sys.argv[1]
    fdate = sys.argv[2]
    tdate = sys.argv[3]
#    rsite = '1236'
    # set arbitrarily for now
#    fdate = "2015-04-25"
#    tdate = "2016-04-25"

    # url = "http://weather.asti.dost.gov.ph/home/index.php/api/data/%s/from/%s/to/%s" % (rsite,fdate,tdate)
    # r = requests.get(url)

    # df = pd.DataFrame(r.json()["data"])
    # df = df.set_index(['dateTimeRead'])
    # df.index = pd.to_datetime(df.index)

    engine = create_engine('mysql+mysqldb://root:senslope@127.0.0.1/senslopedb')

    #Changed date difference is 1 day or 24 hours
    query = "select * from senslopedb.rain_noah_%s where timestamp between '%s' and  '%s'" % (rsite , fdate, tdate)
    
    df = pd.io.sql.read_sql(query,engine)
    df.columns = ['ts','cumm','rval']
   

    df = df.set_index(['ts'])
    df = df["rval"].astype(float)
    df = df[df>= 0]
    df = df.resample('15Min', how = "sum").fillna(0.00)
    dfs = pd.rolling_sum(df,96)
    dfs1 = pd.rolling_sum(df,288)
    dfs = dfs[dfs>=0]
    dfs1 = dfs1[dfs1>=0]
    dfa = pd.DataFrame({"rval":df,"cumm":dfs,"72hrs":dfs1})
   
    dfa = dfa.fillna(0)
 
    
    dfajson = dfa.reset_index().to_json(orient="records",date_format='iso')
    #dfa = dfa.reset_index()
    dfajson = dfajson.replace("T"," ").replace("Z","").replace(".000","")
    print dfajson
    
getDF();