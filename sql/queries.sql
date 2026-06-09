--top 5 funds
select * from fact_aum order by aum_crore desc limit 5;

--average NAV permonth
select strftime('%Y-%m', date) AS nav_month, avg(nav) from fact_nav group by nav_month;

-- sip yoy growth
select month, yoy_growth_pct from fact_sip;

--transactions by state
SELECT state, COUNT(*) AS total_transactions, SUM(amount_inr) AS total_amount_crore FROM fact_transactions GROUP BY state;

--funds ith expense ratio < 1%
select * from dim_fund where expense_ratio_pct < 1;

-- dectors with highest benchmark
select sector, sum(market_value_cr) as Market_Value from fact_benchmarks group by sector;

-- sum category wise
select category, sum(net_inflow_crore) as 'inflow sum' from fact_category group by category;

--equity as percent of total 
select month, equity_folios_crore/total_folios_crore*100 as equity_ratio from fact_industry;

--plan's avg rating
select plan, avg(morningstar_rating) from fact_performance group by plan

--sector market value
select sector, sum(market_value_cr) as value from fact_portfolios group by sector;

