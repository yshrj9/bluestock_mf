import pandas as pd
from pathlib import Path
rd=Path(__file__).parent.resolve().parent/'data'/'processed'

perf = pd.read_csv(rd/'clean_performance.csv')

i = int(input("Enter Risk \n1. Low\n2. Moderate\n3.High\n:"))

if i==1:
    c="Low"
elif i==2:
    c="Moderate"
elif i==3:
    c="High"
else:
    print("wrong input")

shred_perf = perf[perf['risk_grade']==c]

rec=shred_perf.sort_values('sharpe_ratio',ascending=False)
print("Recommened funds = \n",rec.iloc[:3,[0,1,11]])
