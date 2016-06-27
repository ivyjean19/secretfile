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
    ms1 = sys.argv[4]
    ms2 = sys.argv[5]
#   site = 'barscm'
#   fdate = "2016-04-20"
 #   tdate = "2016-04-25"
  #  ms1 = '111'
   # ms2 = '110'
    # m ="m"
    engine = create_engine('mysql+mysqldb://root:senslope@127.0.0.1/senslopedb')
    # query = "select timestamp, mval1 from senslopedb.%s%s where timestamp between '%s' and '%s'" % (site,m ,fdate ,tdate)
    query ="select timestamp,mval1,mval2 from senslopedb.%s where msgid = '%s' or msgid = '%s' and timestamp between '%s' and '%s'"% (site,ms1,ms2,fdate ,tdate)
    df = pd.io.sql.read_sql(query,engine)
    
    df.columns = ['ts','mval1','mval2']
    df = df.set_index(['ts'])
    #
    #dfa= df.pivot('ts','crack_id','meas')
#    print df
#    dfa = df.fillna(method='ffill')
    dfajson = df.reset_index().to_json(orient='records',date_format='iso')
    dfajson = dfajson.replace("T"," ").replace("Z","").replace(".000","")
     
    print dfajson



getDF();
