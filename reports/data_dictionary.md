
### 1. dim_fund (Dimension Table)

| Column Name | Data Type | Key / Constraint | Description |
| :--- | :--- | :--- | :--- |
| `amfi_code` | TEXT | PRIMARY KEY | Unique asset code identifying the mutual fund scheme. |
| `fund_house` | TEXT | NOT NULL | Name of the managing Asset Management Company (AMC). |
| `scheme_name` | TEXT | NOT NULL | Full official commercial name of the mutual fund product. |
| `category` | TEXT | NOT NULL | Asset classification class (e.g., Equity, Debt, Hybrid). |
| `sub_category` | TEXT | | Granular investment sub-classification (e.g., Large Cap, Flexi Cap). |
| `plan` | TEXT | | Distribution route channel option (Regular or Direct). |
| `launch_date` | DATE | | Official inception/launch date of the scheme. |
| `benchmark` | TEXT | | Baseline target market index assigned to measure return efficiency. |
| `expense_ratio_pct` | REAL | | Annual management operating fee charged to assets under management. |
| `exit_load_pct` | REAL | | Conditional redemption penalty fee percentage for early withdrawal. |
| `min_sip_amount` | INTEGER | | Minimum allowable recurring installment investment threshold in INR. |
| `min_lumpsum_amount`| INTEGER | | Minimum initialization one-time purchase capital required in INR. |
| `fund_manager` | TEXT | | Stated name of the primary execution portfolio manager. |
| `risk_category` | TEXT | | Regulatory SEBI riskometer ranking tier (e.g., Very High). |
| `sebi_category_code`| TEXT | | Standardized regulatory reporting categorization code sequence. |
| `created_at` | DATETIME | DEFAULT CURRENT_TIMESTAMP | System metadata recording row ingestion timestamp. |

---

### 2. fact_performance (Fact Table)

| Column Name | Data Type | Key / Constraint | Description |
| :--- | :--- | :--- | :--- |
| `amfi_code` | TEXT | PRIMARY KEY / FK | Primary identifier matching directly against `dim_fund(amfi_code)`. |
| `scheme_name` | TEXT | | Denormalized reference title of the fund scheme. |
| `fund_house` | TEXT | | Denormalized descriptive reference of the fund house. |
| `category` | TEXT | | Denormalized descriptive broad asset classification type. |
| `plan` | TEXT | | Denormalized reference of the route plan. |
| `return_1yr_pct` | REAL | | 1-year trailing absolute return calculation profile in %. |
| `return_3yr_pct` | REAL | | 3-year annualized compound growth return profile (CAGR) %. |
| `return_5yr_pct` | REAL | | 5-year annualized compound growth return profile (CAGR) %. |
| `benchmark_3yr_pct` | REAL | | Concurrent index benchmark performance milestone track over 3 years. |
| `alpha` | REAL | | Value-add manager outperformance return margin vs tracking index. |
| `beta` | REAL | | Volatility market systemic risk sensitivity coefficient. |
| `sharpe_ratio` | REAL | | Return efficiency score captured per unit of total tracking risk. |
| `sortino_ratio` | REAL | | Return efficiency score captured per unit of specific downside risk. |
| `std_dev_ann_pct` | REAL | | Annualized standard deviation of historical rolling asset variations. |
| `max_drawdown_pct` | REAL | | Deepest historic peak-to-trough price retrenchment percentage drop. |
| `aum_crore` | INTEGER | | Aggregated fund scale asset size metrics evaluated in Crore INR. |
| `expense_ratio_pct` | REAL | | Stated annual operational expense tracking calculation ratio. |
| `morningstar_rating`| INTEGER | | Simulated 1 to 5 relative performance scoring tier ranking. |
| `risk_grade` | TEXT | | Qualitative categorical risk variance grouping level. |
| `created_at` | DATETIME | DEFAULT CURRENT_TIMESTAMP | System metadata recording row ingestion timestamp. |

---

### 3. fact_transactions (Fact Table)

| Column Name | Data Type | Key / Constraint | Description |
| :--- | :--- | :--- | :--- |
| `transaction_id` | INTEGER | PRIMARY KEY AUTOINCREMENT | System sequential tracking index assigned to the row ledger item. |
| `investor_id` | TEXT | | Unique lookup hash identifier indexing a unique retail client. |
| `transaction_date` | DATE | | Operational fulfillment settlement day. |
| `amfi_code` | TEXT | FOREIGN KEY | Lookup validation link targeting `dim_fund(amfi_code)`. |
| `transaction_type` | TEXT | | Operational nature of individual order (SIP / Lumpsum / Redemption). |
| `amount_inr` | INTEGER | | Absolute financial size of order captured in Indian Rupees. |
| `state` | TEXT | | Resident province locale categorization of the executing consumer account. |
| `city` | TEXT | | Primary resident population center base location. |
| `city_tier` | TEXT | | Location scale filter classification (T30 = Top 30, B30 = Beyond 30). |
| `age_group` | TEXT | | Segmented demographic age profile bracket. |
| `gender` | TEXT | | Stated structural biological identity of user account. |
| `annual_income_lakh`| REAL | | Documented client gross salary tier scaled in Lakhs INR. |
| `payment_mode` | TEXT | | Settlement mechanism path tracking node (UPI, Mandate, Cheque). |
| `kyc_status` | TEXT | | Compliance verification tracking classification (Verified / Pending). |
| `created_at` | DATETIME | DEFAULT CURRENT_TIMESTAMP | System metadata recording row ingestion timestamp. |

---

### 4. fact_nav (Fact Table)

| Column Name | Data Type | Key / Constraint | Description |
| :--- | :--- | :--- | :--- |
| `date` | DATE | COMPOSITE PK | Market evaluation financial day constraint index. |
| `amfi_code` | TEXT | COMPOSITE PK / FK | Target asset link referencing back to `dim_fund(amfi_code)`. |
| `nav` | REAL | | Per-unit closing Net Asset Value calculated in Indian Rupees. |

---

### 5. fact_portfolios (Fact Table)

| Column Name | Data Type | Key / Constraint | Description |
| :--- | :--- | :--- | :--- |
| `amfi_code` | TEXT | COMPOSITE PK / FK | Reference map key linking to master asset logs `dim_fund(amfi_code)`. |
| `stock_symbol` | TEXT | COMPOSITE PK | Exchange ticker security identifier (e.g., TCS). |
| `stock_name` | TEXT | | Full enterprise legal identification identity string. |
| `sector` | TEXT | | Standard financial industrial classification segment description block. |
| `weight_pct` | REAL | | Relative proportional weight distribution slice inside the fund. |
| `market_value_cr` | REAL | | Nominal current value balance slice of security scaled in Crore INR. |
| `current_price_inr` | REAL | | Unit asset market spot exchange value parameter recorded at cutoff. |
| `portfolio_date` | DATE | COMPOSITE PK | Effective period logging day of declaration snapshot. |

---

### 6. fact_benchmarks (Fact Table) — *REVISED*

| Column Name | Data Type | Key / Constraint | Description |
| :--- | :--- | :--- | :--- |
| `date` | DATE | COMPOSITE PK | Valuation baseline market business day. |
| `index_name` | TEXT | COMPOSITE PK | Broad target index tracker name (e.g., NIFTY50, NIFTY100). |
| `close_value`| REAL | | Financial closing valuation price recorded in index points. |

---

### 7. fact_aum (Fact Table)

| Column Name | Data Type | Key / Constraint | Description |
| :--- | :--- | :--- | :--- |
| `date` | DATE | COMPOSITE PK | Quarterly tracking cutoff snapshot day indicator. |
| `fund_house` | TEXT | COMPOSITE PK | String name tracking back to corporate entity identities. |
| `aum_lakh_crore` | REAL | | Cumulative asset scale calculated in Lakh Crore INR metric lines. |
| `aum_crore` | INTEGER | | Core nominal consolidated scale calculation in Crore INR units. |
| `num_schemes` | INTEGER | | Count of individual operational mutual fund lines run by the AMC. |

---

### 8. fact_sip (Fact Table)

| Column Name | Data Type | Key / Constraint | Description |
| :--- | :--- | :--- | :--- |
| `month` | DATE | PRIMARY KEY | Sequential tracking timeline key milestone entry node (YYYY-MM-DD). |
| `sip_inflow_crore` | INTEGER | | Sector total cumulative capital volume inputs via SIP in Crore INR. |
| `active_sip_accounts_crore`| REAL | | Aggregate national trace volume of live contracts, scaled in Crores. |
| `new_sip_accounts_lakh`| REAL | | Count of new incoming monthly plan additions, scaled in Lakhs. |
| `sip_aum_lakh_crore` | REAL | | Valuation total pool of underlying assets managed via SIP in Lakh Crore. |
| `yoy_growth_pct` | REAL | | Computed mathematical Year-over-Year change margin percentage. |

---

### 9. fact_category (Fact Table)

| Column Name | Data Type | Key / Constraint | Description |
| :--- | :--- | :--- | :--- |
| `month` | DATE | COMPOSITE PK | Temporal calendar sequence logging period. |
| `category` | TEXT | COMPOSITE PK | Target strategic grouping asset bucket (e.g., Small Cap, Debt). |
| `net_inflow_crore` | REAL | | Net periodic asset intake calculated after redemption actions. |

---

### 10. fact_industry (Fact Table)

| Column Name | Data Type | Key / Constraint | Description |
| :--- | :--- | :--- | :--- |
| `month` | DATE | PRIMARY KEY | Calendar temporal baseline sequence parameter. |
| `total_folios_crore` | REAL | | Nominal sum total count of active operational accounts inside India. |
| `equity_folios_crore`| REAL | | Segment balance subtotal tracking operational Equity folios. |
| `debt_folios_crore` | REAL | | Segment balance subtotal tracking operational Debt folios. |
| `hybrid_folios_crore`| REAL | | Segment balance subtotal tracking operational Hybrid folios. |
| `others_folios_crore`| REAL | | Remaining balance subtotal logging alternative product classifications. |
