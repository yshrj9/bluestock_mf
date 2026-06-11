import json
import requests
import pandas as pd
from pathlib import Path
wd = Path(__file__).parent.resolve().parent/'data'/'raw'
#request

r = requests.get("https://api.mfapi.in/mf/125497")
data = json.loads(r.content)
df = pd.DataFrame(data['data'])
name=data['meta']['scheme_name']+'.csv'
path = wd/name 
df.to_csv(path,index=False)


r = requests.get("https://api.mfapi.in/mf/119551")
data = json.loads(r.content)
df = pd.DataFrame(data['data'])
name=data['meta']['scheme_name']+'.csv'
path = wd/name 
df.to_csv(path,index=False)

r = requests.get("https://api.mfapi.in/mf/120503")
data = json.loads(r.content)
df = pd.DataFrame(data['data'])
name=data['meta']['scheme_name']+'.csv'
path = wd/name 
df.to_csv(path,index=False)

r = requests.get("https://api.mfapi.in/mf/118632")
data = json.loads(r.content)
df = pd.DataFrame(data['data'])
name=data['meta']['scheme_name']+'.csv'
path = wd/name 
df.to_csv(path,index=False)

r = requests.get("https://api.mfapi.in/mf/120841")
data = json.loads(r.content)
df = pd.DataFrame(data['data'])
name=data['meta']['scheme_name']+'.csv'
path = wd/name 
df.to_csv(path,index=False)


r = requests.get("https://api.mfapi.in/mf/119092")
data = json.loads(r.content)
df = pd.DataFrame(data['data'])
name=data['meta']['scheme_name']+'.csv'
path = wd/name 
df.to_csv(path,index=False)
