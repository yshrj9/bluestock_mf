from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine
rd = Path(__file__).parent.resolve().parent/'data'/'processed'
target = Path(__file__).parent.resolve().parent/'data'/'db'/'bluestock_mf.db'

mapped = {
    "clean_fund.csv": "dim_fund",
    "clean_performance.csv": "fact_performance",
    "clean_transactions.csv": "fact_transactions",
    "clean_nav.csv": "fact_nav",
    "clean_aum.csv": "fact_aum",
    "clean_sip.csv": "fact_sip",
    "clean_category.csv": "fact_category",
    "clean_industry.csv": "fact_industry",
    "clean_portfoilio.csv": "fact_portfolios",
    "clean_benchmark.csv": "fact_benchmarks"
}

engine = create_engine(f"sqlite:///{target}")

for name,table in mapped.items():
    path = rd/name
    print(path,'-->',name)
    df = pd.read_csv(path)
    df.to_sql(table, engine,if_exists='append', index=False)
