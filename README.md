# bluestock_mf
capstone project for bluestock fintech internship. Creating full stack Mutual fund analytic platform

# useage

1. install requirements.txt
pip install -r requirements.txt

2. create and move db
in sql/
sqlite3 bluestock_mf.db
> .read schema.sql
>.exit

copy to data/sb/

3. run master scipt 

 python etl_pipeline.py

4. view analysis

jupyter notebook

 and open, use various notebooks in notebook/ directory

 # files 

data/          -> datasets
scripts/       -> python scripts
sql/           -> database scripts
notebooks/     -> analytics notebooks
dashboard/     -> power bi files
reports/       -> final documentation

