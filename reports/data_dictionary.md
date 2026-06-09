# Data Dictionary: Mutual Fund Analytics Platform

This data dictionary documents the exact columns, data types, and descriptions for all 10 tables in the `bluestock_mf.db` database.

---

### 1. dim_fund (Dimension Table)

| Column Name | Data Type | Key / Constraint | Description |
| :--- | :--- | :--- | :--- |
| `amfi_code` | TEXT | PRIMARY KEY | Unique identifier code for the mutual fund scheme. |
| `fund_house` | TEXT | NOT NULL | Name of the Asset Management Company (AMC). |
| `scheme_name` | TEXT | NOT NULL | Full official name of the mutual fund scheme. |
| `category` | TEXT | NOT NULL | Broad asset class category (e.g., Equity, Debt, Hybrid). |
| `sub_category` | TEXT | | Granular investment style classification (e.g., Large Cap, Liquid). |
| `plan` | TEXT | | Distribution channel option (Regular or Direct). |
| `launch_date` | DATE | | Official inception/launch date of the scheme. |
| `benchmark` | TEXT | | Target market index assigned to measure fund performance. |
| `expense_ratio_pct` | REAL | | Annual operating management fee charged to the fund, in %. |
| `exit_load_pct` | REAL | | Penalty fee percentage charged for early unit redemptions. |
| `min_sip_amount` | INTEGER | | Minimum allowable recurring installment amount in INR. |
| `min_lumpsum_amount`| INTEGER | | Minimum allowable one-time purchase amount in INR. |
| `fund_manager` | TEXT | | Name of the primary individual portfolio manager. |
| `risk_category` | TEXT | | SEBI mandated riskometer risk level label (e.g., Very High). |
| `sebi_category_code`| TEXT | | Standardized regulatory reporting classification code. |
| `created_at` | DATETIME | DEFAULT CURRENT_TIMESTAMP | Metadata recording row ingestion timestamp. |

---

### 2. fact_performance (Fact Table)

| Column Name | Data Type | Key / Constraint | Description |
| :--- | :--- | :--- | :--- |
| `amfi_code` | TEXT | PRIMARY KEY / FK | Primary reference link targeting `dim_fund(amfi_code)`. |
| `scheme_name` | TEXT | | Reference name of the fund scheme. |
| `fund_house` | TEXT | | Reference name of the fund house / AMC. |
| `category` | TEXT | | Reference broad asset classification type. |
| `plan` | TEXT | | Reference investment route plan. |
| `return_1yr_pct` | REAL | | 1-year trailing absolute percentage return performance. |
| `return_3yr_pct` | REAL | | 3-year annualized compound growth return profile (CAGR) %. |
| `return_5yr_pct` | REAL | | 5-year annualized compound growth return profile (CAGR) %. |
| `benchmark_3yr_pct` | REAL | | Assigned index benchmark 3-year annualized CAGR performance. |
| `alpha` | REAL | | Risk-adjusted manager outperformance margin vs tracking index. |
| `beta` | REAL | | Volatility market sensitivity risk coefficient factor. |
| `sharpe_ratio` | REAL | | Return efficiency score captured per unit of total risk volatility. |
| `sortino_ratio` | REAL | | Return efficiency score captured per unit of downside risk exposure. |
| `std_dev_ann_pct` | REAL | | Annualized standard deviation of daily rolling asset variations. |
| `max_drawdown_pct` | REAL | | Deepest historical peak-to-trough price percentage drop. |
| `aum_crore` | INTEGER | | Aggregated overall fund asset size measured in Crore INR. |
| `expense_ratio_pct` | REAL | | Annual operational expense tracking calculation ratio. |
| `morningstar_rating`| INTEGER | | Simulated 1 to 5 relative risk-adjusted rating ranking tier. |
| `risk_grade` | TEXT | | Qualitative categorical risk variance grouping level. |
| `created_at` | DATETIME | DEFAULT CURRENT_TIMESTAMP | Metadata recording row ingestion timestamp. |

---

### 3. fact_transactions (Fact Table)

| Column Name | Data Type | Key / Constraint | Description |
| :--- | :--- | :--- | :--- |
| `transaction_id` | INTEGER | PRIMARY KEY AUTOINCREMENT | System sequential ledger serial tracking index. |
| `investor_id` | TEXT | | Unique lookup identifier code assigned to the client. |
| `transaction_date` | DATE | | Operational execution and settlement day. |
| `amfi_code` | TEXT | FOREIGN KEY | Lookup validation link targeting `dim_fund(amfi_code)`. |
| `transaction_type` | TEXT | | Nature of individual account order (SIP / Lumpsum / Redemption). |
| `amount_inr` | INTEGER | | Absolute financial size of the order in Indian Rupees. |
| `state` | TEXT | | Resident province locale classification of the account holder. |
| `city` | TEXT | | Resident city location of the investor. |
| `city_tier` | TEXT | | AMFI regional classification tier (T30 = Top 30, B30 = Beyond 30). |
| `age_group` | TEXT | | Segmented demographic age profile range bucket. |
| `gender` | TEXT | | Declared gender identification profile of the user. |
| `annual_income_lakh`| REAL | | Documented client gross annual salary scale tier in Lakhs INR. |
| `payment_mode` | TEXT | | Banking settlement channel utilized (UPI, Mandate, Cheque, etc.). |
| `kyc_status` | TEXT | | Compliance verification condition (Verified or Pending). |
| `created_at` | DATETIME | DEFAULT CURRENT_TIMESTAMP | Metadata recording row ingestion timestamp. |

---

### 4. fact_nav (Fact Table)

| Column Name | Data Type | Key / Constraint | Description |
| :--- | :--- | :--- | :--- |
| `date` | DATE | COMPOSITE PK | Valuation operational business business day. |
| `amfi_code` | TEXT | COMPOSITE PK / FK | Target asset link referencing back to `dim_fund(amfi_code)`. |
| `nav` | REAL | | Per-unit closing Net Asset Value in Indian Rupees. |

---

### 5. fact_aum (Fact Table)

| Column Name | Data Type | Key / Constraint | Description |
| :--- | :--- | :--- | :--- |
| `date` | DATE | COMPOSITE PK | Quarterly reporting period accounting cutoff milestone date. |
| `fund_house` | TEXT | COMPOSITE PK | Matching key tracking back to the Asset Management Company. |
| `aum_lakh_crore` | REAL | | Cumulative asset scale calculated in Lakh Crore INR metric lines. |
| `aum_crore` | INTEGER | | Core nominal consolidated scale calculation in Crore INR units. |
| `num_schemes` | INTEGER | | Count of individual operational mutual fund lines run by the AMC. |

---

### 6. fact_sip (Fact Table)

| Column Name | Data Type | Key / Constraint | Description |
| :--- | :--- | :--- | :--- |
| `month` | DATE | PRIMARY KEY | Sequential chronological timeline indexing month milestone node. |
| `sip_inflow_crore` | INTEGER | | Sector aggregate cumulative monthly capital intakes via SIP in Crore INR. |
| `active_sip_accounts_crore`| REAL | | Global industry volume of active running systematic plans in Crores. |
| `new_sip_accounts_lakh`| REAL | | Count of fresh month-on-month customer mandate additions in Lakhs. |
| `sip_aum_lakh_crore` | REAL | | Aggregate underlying industry asset pool tied to SIP books in Lakh Crore. |
| `yoy_growth_pct` | REAL | | Calculated mathematical Year-over-Year change percentage margin. |

---

### 7. fact_category (Fact Table)

| Column Name | Data Type | Key / Constraint | Description |
| :--- | :--- | :--- | :--- |
| `month` | DATE | COMPOSITE PK | Temporal calendar sequence logging period. |
| `category` | TEXT | COMPOSITE PK | Target strategic grouping asset bucket framework (e.g., Small Cap). |
| `net_inflow_crore` | REAL | | Net periodic asset intake calculated after redemption actions in Crore INR. |

---

### 8. fact_industry (Fact Table)

| Column Name | Data Type | Key / Constraint | Description |
| :--- | :--- | :--- | :--- |
| `month` | DATE | PRIMARY KEY | Calendar temporal baseline sequence month tracking parameter. |
| `total_folios_crore` | REAL | | Aggregate sum total count of open individual mutual fund accounts in Crores. |
| `equity_folios_crore`| REAL | | Segment balance subtotal tracking operational active Equity folios. |
| `debt_folios_crore` | REAL | | Segment balance subtotal tracking operational active Debt folios. |
| `hybrid_folios_crore`| REAL | | Segment balance subtotal tracking operational active Hybrid folios. |
| `others_folios_crore`| REAL | | Remaining balance subtotal logging alternative product classifications. |

---

### 9. fact_portfolios (Fact Table)

| Column Name | Data Type | Key / Constraint | Description |
| :--- | :--- | :--- | :--- |
| `amfi_code` | TEXT | COMPOSITE PK / FK | Reference map key linking directly back to `dim_fund(amfi_code)`. |
| `stock_symbol` | TEXT | COMPOSITE PK | Unique exchange listing trading ticker symbol asset label (e.g., TCS). |
| `stock_name` | TEXT | | Full enterprise legal corporate identification title string. |
| `sector` | TEXT | | Financial industrial classification segment description block. |
| `weight_pct` | REAL | | Relative proportional weight allocation percentage slice inside the fund. |
| `market_value_cr` | REAL | | Nominal current value balance slice of security scaled in Crore INR. |
| `current_price_inr` | REAL | | Unit stock market price exchange value parameter recorded at cutoff. |
| `portfolio_date` | DATE | COMPOSITE PK | Effective period declaration logging day of holdings snapshot. |

---

### 10. fact_benchmarks (Fact Table)

| Column Name | Data Type | Key / Constraint | Description |
| :--- | :--- | :--- | :--- |
| `amfi_code` | TEXT | COMPOSITE PK / FK | Links index configurations back to respective master scheme structures. |
| `stock_symbol` | TEXT | COMPOSITE PK | Index constituent mapping identifier token ticker asset string. |
| `stock_name` | TEXT | | Full enterprise legal corporate title signature parameter. |
| `sector` | TEXT | | Target industrial classification class assigned inside index model rules. |
| `weight_pct` | REAL | | Constituent relative target baseline priority tracking model percentage. |
| `market_value_cr` | REAL | | Index weighting balance profile mapping factor tracking index equivalents. |
| `current_price_inr` | REAL | | Institutional market spot settlement execution pricing baseline value. |
| `portfolio_date` | DATE | COMPOSITE PK | Temporal validation record date of matching index structural logs. |
