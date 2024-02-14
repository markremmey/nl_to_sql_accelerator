golden_records = [ 

  { 

    "question": "What was the value of the consumer price index in May 2023?", 

    "sql_query": "SELECT value FROM bls_consumer_price_index WHERE area_name = 'U.S. city average' AND item_name = 'All items' AND seasonal = 'Seasonally Adjusted' AND year = 2023 AND period_name = 'May'", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "How much did food prices go up between 2019 and 2022?", 

    "sql_query": "SELECT (cpi_2022.value - cpi_2019.value)/cpi_2019.value as rate_of_inflation  FROM bls_consumer_price_index as cpi_2019, bls_consumer_price_index as cpi_2022  WHERE cpi_2019.area_name = 'U.S. city average'  AND cpi_2019.item_name = 'Food'  AND cpi_2019.seasonal = 'Seasonally Adjusted'  AND cpi_2019.year = 2019 AND cpi_2019.period_name = 'January' AND cpi_2022.area_name = 'U.S. city average'  AND cpi_2022.item_name = 'Food'  AND cpi_2022.seasonal = 'Seasonally Adjusted'  AND cpi_2022.year = 2022 AND cpi_2022.period_name = 'December'", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What was the unemployment rate in 2018?", 

    "sql_query": "SELECT value as unemployment_rate FROM bls_labor_force_statistics WHERE period_name = 'Annual' AND year = 2018 AND age_group = '16 years and over' AND labor_force_status = 'Unemployment rate' AND foreign_native_born = 'N/A' AND certification_license_status = 'N/A' AND children = 'N/A' AND class_of_worker = 'N/A' AND disabled_status = 'N/A' AND length_of_unemployment = 'N/A' AND level_of_education = 'All educational levels' AND labor_force_entrant_status = 'N/A' AND experience_level = 'N/A' AND head_of_family = 'N/A' AND hours_worked_bucket = 'N/A' AND industry_name = 'All Industries' AND wants_job = 'N/A' AND reason_looking = 'N/A' AND marriage_status = 'N/A' AND multiple_job_holder_status = 'N/A' AND occupation = 'All Occupations' AND hispanic_origin = 'All Origins' AND race = 'All Races' AND sex = 'Both Sexes' AND veteran_status = 'N/A'", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What was the unemployment rate for men and women in 2018?", 

    "sql_query": "SELECT sex, value as unemployment_rate FROM bls_labor_force_statistics WHERE period_name = 'Annual' AND year = 2018 AND age_group = '16 years and over' AND labor_force_status = 'Unemployment rate' AND foreign_native_born = 'N/A' AND certification_license_status = 'N/A' AND children = 'N/A' AND class_of_worker = 'N/A' AND disabled_status = 'N/A' AND length_of_unemployment = 'N/A' AND level_of_education = 'All educational levels' AND labor_force_entrant_status = 'N/A' AND experience_level = 'N/A' AND head_of_family = 'N/A' AND hours_worked_bucket = 'N/A' AND industry_name = 'All Industries' AND wants_job = 'N/A' AND reason_looking = 'N/A' AND marriage_status = 'N/A' AND multiple_job_holder_status = 'N/A' AND occupation = 'All Occupations' AND hispanic_origin = 'All Origins' AND race = 'All Races' AND veteran_status = 'N/A'", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What was the unemployment rate for immigrants and native born Americans in 2018?", 

    "sql_query": "SELECT foreign_native_born, AVG(value) as unemployment_rate FROM bls_labor_force_statistics WHERE period_name = 'Annual' AND year = 2018 AND age_group = '16 years and over' AND labor_force_status = 'Unemployment rate' AND certification_license_status = 'N/A' AND children = 'N/A' AND class_of_worker = 'N/A' AND disabled_status = 'N/A' AND length_of_unemployment = 'N/A' AND level_of_education = 'All educational levels' AND labor_force_entrant_status = 'N/A' AND experience_level = 'N/A' AND head_of_family = 'N/A' AND hours_worked_bucket = 'N/A' AND industry_name = 'All Industries' AND wants_job = 'N/A' AND reason_looking = 'N/A' AND marriage_status = 'N/A' AND multiple_job_holder_status = 'N/A' AND occupation = 'All Occupations' AND hispanic_origin = 'All Origins' AND race = 'All Races' AND sex = 'Both Sexes' AND veteran_status = 'N/A' GROUP BY foreign_native_born", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What is the unemployment rate in Denver CO?", 

    "sql_query": "SELECT value as unemployment_rate FROM bls_local_area_unemployment_statistics WHERE area_type = 'cities and towns above 25,000 population' AND area_name = 'Denver County/city, CO' AND year = 2022 AND period_name = 'Annual' AND measure = 'unemployment rate'", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "Is the economy growing?", 

    "sql_query": "SELECT (1 + (gdp_q4_2022.value - gdp_q3_2022.value)/gdp_q3_2022.value)^4 -1 as gdp_growth_rate FROM bea_gross_domestic_product_by_quarter gdp_q4_2022, bea_gross_domestic_product_by_quarter gdp_q3_2022 WHERE gdp_q4_2022.measurement_name = 'Real GDP by state' AND gdp_q4_2022.area_type = 'Nationwide' AND gdp_q4_2022.industry_type = 'Total' AND gdp_q4_2022.year = 2022 AND gdp_q4_2022.quarter = 'Q4' AND gdp_q3_2022.measurement_name = 'Real GDP by state' AND gdp_q3_2022.area_type = 'Nationwide' AND gdp_q3_2022.industry_type = 'Total' AND gdp_q3_2022.year = 2022 AND gdp_q3_2022.quarter = 'Q3'", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "Is the cost of living rising?", 

    "sql_query": "SELECT (cpi_july_2023.value - cpi_july_2022.value)/cpi_july_2022.value as rate_of_inflation FROM bls_consumer_price_index cpi_july_2023, bls_consumer_price_index cpi_july_2022 WHERE cpi_july_2023.area_name = 'U.S. city average' AND cpi_july_2023.item_name = 'All items' AND cpi_july_2023.year = 2023 AND cpi_july_2023.period_name = 'July' AND cpi_july_2023.seasonal = 'Not Seasonally Adjusted' AND cpi_july_2022.area_name = 'U.S. city average' AND cpi_july_2022.item_name = 'All items' AND cpi_july_2022.year = 2022 AND cpi_july_2022.period_name = 'July' AND cpi_july_2022.seasonal = 'Not Seasonally Adjusted' -- this query calculates the overall rate of inflation in the US for the most recently-available month (July 2023) compared to the same month in the prior year (July 2022)", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "How is the US job market?", 

    "sql_query": "SELECT (real_earnings_2023.value - real_earnings_2022.value)/real_earnings_2022.value as real_wage_change, (nominal_earnings_2023.value - nominal_earnings_2022.value)/nominal_earnings_2022.value as nominal_wage_change FROM bls_current_employment real_earnings_2023, bls_current_employment real_earnings_2022, bls_current_employment nominal_earnings_2023, bls_current_employment nominal_earnings_2022 WHERE real_earnings_2023.data_type = 'AVERAGE HOURLY EARNINGS OF ALL EMPLOYEES, 1982-1984 DOLLARS' AND real_earnings_2023.supersector_name = 'Total private' AND real_earnings_2023.seasonal = 'Seasonally Adjusted' AND real_earnings_2023.year = 2023 AND real_earnings_2023.period_name = 'July' AND real_earnings_2022.data_type = 'AVERAGE HOURLY EARNINGS OF ALL EMPLOYEES, 1982-1984 DOLLARS' AND real_earnings_2022.supersector_name = 'Total private' AND real_earnings_2022.seasonal = 'Seasonally Adjusted' AND real_earnings_2022.year = 2022 AND real_earnings_2022.period_name = 'July' AND nominal_earnings_2023.data_type = 'AVERAGE HOURLY EARNINGS OF ALL EMPLOYEES' AND nominal_earnings_2023.supersector_name = 'Total private' AND nominal_earnings_2023.seasonal = 'Seasonally Adjusted' AND nominal_earnings_2023.year = 2023 AND nominal_earnings_2023.period_name = 'July' AND nominal_earnings_2022.data_type = 'AVERAGE HOURLY EARNINGS OF ALL EMPLOYEES' AND nominal_earnings_2022.supersector_name = 'Total private' AND nominal_earnings_2022.seasonal = 'Seasonally Adjusted' AND nominal_earnings_2022.year = 2022 AND nominal_earnings_2022.period_name = 'July' -- this query calculates the percent change in real (inflation-adjusted) and nominal wages over the last year, using the most recently-available month and year (July 2023)", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What is the inflation rate?", 

    "sql_query": "SELECT (cpi_july_2023.value - cpi_july_2022.value)/cpi_july_2022.value as rate_of_inflation FROM bls_consumer_price_index cpi_july_2023, bls_consumer_price_index cpi_july_2022 WHERE cpi_july_2023.area_name = 'U.S. city average' AND cpi_july_2023.item_name = 'All items' AND cpi_july_2023.year = 2023 AND cpi_july_2023.period_name = 'July' AND cpi_july_2023.seasonal = 'Not Seasonally Adjusted' AND cpi_july_2022.area_name = 'U.S. city average' AND cpi_july_2022.item_name = 'All items' AND cpi_july_2022.year = 2022 AND cpi_july_2022.period_name = 'July' AND cpi_july_2022.seasonal = 'Not Seasonally Adjusted' -- this query calculates the overall rate of inflation in the US for the most recently-available month (July 2023) compared to the same month in the prior year (July 2022)", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "Where have prices increased the most? The least?", 

    "sql_query": "(SELECT t.item_name, (t.current_value - t.prev_value)/t.prev_value as inflation_rate, 'Top 5' as top_bottom FROM ( select item_name, period_name as month, year, value as current_value, LAG(value) OVER (PARTITION BY item_name ORDER BY year ASC) as prev_value from bls_consumer_price_index where area_name = 'U.S. city average' and year in (2022, 2023) and period_name = 'July' and seasonal = 'Not Seasonally Adjusted' ) as t WHERE t.year = 2023 ORDER BY (t.current_value - t.prev_value)/t.prev_value DESC NULLS LAST LIMIT 5) UNION (SELECT t.item_name, (t.current_value - t.prev_value)/t.prev_value as inflation_rate, 'Bottom 5' as top_bottom FROM ( select item_name, period_name as month, year, value as current_value, LAG(value) OVER (PARTITION BY item_name ORDER BY year ASC) as prev_value from bls_consumer_price_index where area_name = 'U.S. city average' and year in (2022, 2023) and period_name = 'July' and seasonal = 'Not Seasonally Adjusted' ) as t WHERE t.year = 2023 ORDER BY (t.current_value - t.prev_value)/t.prev_value ASC LIMIT 5) -- this query calculates the rate of inflation for each product category over the last year using the most recently-available month and year (July 2023) and shows the 5 product categories with the highest and lowest increases", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "How does the inflation rate of the U.S. city average compare to specific cities within the last 5 years?", 

    "sql_query": "SELECT cpi_2022.area_name, ((cpi_2022.value - cpi_2017.value)/cpi_2017.value) as inflation_rate FROM bls_consumer_price_index cpi_2022, bls_consumer_price_index cpi_2017 WHERE cpi_2022.item_name = 'All items' AND cpi_2022.year = 2022 AND cpi_2022.period_name = 'Annual' AND cpi_2022.seasonal = 'Not Seasonally Adjusted' AND cpi_2022.area_type IN ('Metro', 'Total') AND cpi_2017.item_name = 'All items' AND cpi_2017.year = 2017 AND cpi_2017.period_name = 'Annual' AND cpi_2017.seasonal = 'Not Seasonally Adjusted' AND cpi_2017.area_type IN ('Metro', 'Total') AND cpi_2022.area_name = cpi_2017.area_name ORDER BY inflation_rate DESC LIMIT 10 -- this query calculates the overall rate of inflation for the 25 metro areas with the highest inflation rate along with the US average inflation rate over the last 5 years", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "How has the cost of living increased in different areas of the country over the last 5 years?", 

    "sql_query": "SELECT cpi_2022.area_name, ((cpi_2022.value - cpi_2017.value) / cpi_2017.value) AS inflation_rate FROM bls_consumer_price_index cpi_2022, bls_consumer_price_index cpi_2017 WHERE cpi_2022.item_name = 'All items' AND cpi_2022.year = 2022 AND cpi_2022.period_name = 'Annual' AND cpi_2022.seasonal = 'Not Seasonally Adjusted' AND cpi_2022.area_type = 'Region' AND cpi_2017.item_name = 'All items' AND cpi_2017.year = 2017 AND cpi_2017.period_name = 'Annual' AND cpi_2017.seasonal = 'Not Seasonally Adjusted' AND cpi_2017.area_type = 'Region' AND cpi_2022.area_name = cpi_2017.area_name ORDER BY INFLATION_RATE DESC LIMIT 10 -- retrieves the overall inflation rate from 2017 to 2022 (the most recent 5 years) by US area/region", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What was the inflation rate in each metro area from June 2022 through June 2023?", 

    "sql_query": "SELECT cpi_2023.area_name, ((cpi_2023.value - cpi_2022.value)/cpi_2022.value) as inflation_rate FROM bls_consumer_price_index cpi_2023, bls_consumer_price_index cpi_2022 WHERE cpi_2023.item_name = 'All items' AND cpi_2023.year = 2023 AND cpi_2023.period_name = 'June' AND cpi_2023.seasonal = 'Not Seasonally Adjusted' AND cpi_2023.area_type = 'Metro' AND cpi_2022.item_name = 'All items' AND cpi_2022.year = 2022 AND cpi_2022.period_name = 'June' AND cpi_2022.seasonal = 'Not Seasonally Adjusted' AND cpi_2022.area_type = 'Metro' AND cpi_2023.area_name = cpi_2022.area_name ORDER BY inflation_rate DESC LIMIT 10 -- this query calculates the overall rate of inflation for each metro area from June 2022 to June 2023", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "How does inflation in the Miami area compare to the rest of the United States?", 

    "sql_query": "SELECT cpi_2022.area_name, (cpi_2023.value - cpi_2022.value)/cpi_2022.value as rate_of_inflation FROM bls_consumer_price_index cpi_2023, bls_consumer_price_index cpi_2022 WHERE cpi_2023.area_name IN ('Miami-Fort Lauderdale-West Palm Beach, FL', 'U.S. city average') AND cpi_2023.item_name = 'All items' AND cpi_2023.seasonal = 'Not Seasonally Adjusted' AND cpi_2023.period_name = 'June' AND cpi_2023.year = '2023' AND cpi_2022.area_name IN ('Miami-Fort Lauderdale-West Palm Beach, FL', 'U.S. city average') AND cpi_2022.item_name = 'All items' AND cpi_2022.seasonal = 'Not Seasonally Adjusted' AND cpi_2022.period_name = 'June' AND cpi_2022.year = '2022' AND cpi_2023.area_name = cpi_2022.area_name -- calculates the rate of inflation for the Miami area compared to the entire US from June 2022 to June 2023", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What jobs have grown the most since 2020?", 

    "sql_query": "SELECT ce_2023.industry_name, (ce_2023.value - ce_2020.value)/ce_2020.value as rate_of_increase FROM bls_current_employment ce_2023, bls_current_employment ce_2020 WHERE ce_2023.data_type = 'ALL EMPLOYEES, THOUSANDS' AND ce_2023.period_name = 'July' AND ce_2023.year = 2023 AND ce_2023.seasonal = 'Seasonally Adjusted' AND ce_2020.data_type = 'ALL EMPLOYEES, THOUSANDS' AND ce_2020.period_name = 'January' AND ce_2020.year = 2020 AND ce_2020.seasonal = 'Seasonally Adjusted' AND ce_2023.industry_name = ce_2020.industry_name ORDER BY rate_of_increase DESC LIMIT 10 -- calculates the rate of increase in the number of employees in each industry since January 2020 and selects the top 25", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What industries and sectors contribute the most to GDP?", 

    "sql_query": "SELECT industry_name, value FROM bea_gross_domestic_product_by_year WHERE measurement_name = 'Real GDP by state' AND area_name = 'United States' AND industry_type = 'Sector' AND year = 2022 ORDER BY value DESC LIMIT 10;", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What are the GDP trends for different regions and geographic areas in the United States?", 

    "sql_query": "SELECT gdp_q4_2022.area_name, gdp_q4_2022.area_type, (1 + (gdp_q4_2022.value - gdp_q3_2022.value)/gdp_q3_2022.value)^4 -1 as gdp_growth_rate FROM bea_gross_domestic_product_by_quarter as gdp_q4_2022 INNER JOIN bea_gross_domestic_product_by_quarter as gdp_q3_2022 ON gdp_q4_2022.area_name = gdp_q3_2022.area_name WHERE gdp_q4_2022.measurement_name = 'Real GDP by state' AND gdp_q4_2022.industry_type = 'Total' AND gdp_q4_2022.year = 2022 AND gdp_q4_2022.quarter = 'Q4' AND gdp_q4_2022.area_type != 'Nationwide' AND gdp_q3_2022.measurement_name = 'Real GDP by state' AND gdp_q3_2022.industry_type = 'Total' AND gdp_q3_2022.year = 2022 AND gdp_q3_2022.quarter = 'Q3' AND gdp_q3_2022.area_type != 'Nationwide' GROUP BY gdp_q4_2022.area_name, gdp_q4_2022.area_type, gdp_q4_2022.value, gdp_q3_2022.value ORDER BY gdp_q4_2022.area_type, gdp_growth_rate DESC LIMIT 10", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "How much does government spending impact GDP?", 

    "sql_query": "SELECT gov.value AS government_value, gov.value/total.value AS government_proportion FROM bea_gross_domestic_product_by_quarter AS gov, bea_gross_domestic_product_by_quarter AS total WHERE gov.measurement_name = 'Real GDP by state' AND gov.industry_name = 'Government and government enterprises' AND gov.year = 2022 AND gov.quarter = 'Q4' AND gov.area_type = 'Nationwide' AND total.measurement_name = 'Real GDP by state' AND total.industry_name = 'All industry total' AND total.year = 2022 AND total.quarter = 'Q4' AND total.area_type = 'Nationwide' LIMIT 10", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What is the total amount of consumer spending in the United States, and how has it changed over time?", 

    "sql_query": "SELECT value as total_spending FROM bea_personal_consumption_expenditures_aggregate WHERE product_category_name = 'Total personal consumption expenditures' AND area_type = 'Nationwide' AND year = 2021;", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What percentage of consumer spending is allocated to different categories such as housing, food, transportation, healthcare, and entertainment?", 

    "sql_query": "SELECT product_category_name, value as total_spending, value/(SELECT value FROM bea_personal_consumption_expenditures_aggregate WHERE area_type = 'Nationwide' AND product_category_name = 'Total personal consumption expenditures' AND year = 2021) as proportion_of_total FROM bea_personal_consumption_expenditures_aggregate WHERE area_type = 'Nationwide' AND product_category_type = 'Product Type' AND year = 2021 ORDER BY proportion_of_total DESC NULLS LAST LIMIT 10;", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What percentage of the population is working or actively seeking work?", 

    "sql_query": "SELECT value as labor_force_participation_rate FROM bls_labor_force_statistics WHERE year = 2023 AND period_name = 'July' AND seasonal = 'Seasonally Adjusted' AND age_group = '16 years and over' AND labor_force_status = 'Civilian labor force participation rate' AND foreign_native_born = 'N/A' AND certification_license_status = 'N/A' AND children = 'N/A' AND class_of_worker = 'N/A' AND disabled_status = 'N/A' AND length_of_unemployment = 'N/A' AND level_of_education = 'All educational levels' AND labor_force_entrant_status = 'N/A' AND experience_level = 'N/A' AND head_of_family = 'N/A' AND hours_worked_bucket = 'N/A' AND industry_name = 'All Industries' AND wants_job = 'N/A' AND reason_looking = 'N/A' AND marriage_status = 'N/A' AND multiple_job_holder_status = 'N/A' AND occupation = 'All Occupations' AND hispanic_origin = 'All Origins' AND race = 'All Races' AND sex = 'Both Sexes' AND veteran_status = 'N/A' LIMIT 10", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "Has the unemployment rate risen since 2020 in California?", 

    "sql_query": "SELECT year, value FROM bls_local_area_unemployment_statistics WHERE area_name = 'California' AND measure = 'unemployment rate' AND area_type = 'statewide' AND period_type = 'yearly (calendar year)' AND year >= 2020 LIMIT 10", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "How did the unemployment rate differ by education level in 2018", 

    "sql_query": "SELECT unemployed_2018.level_of_education, unemployed_2018.value as unemployed, total_2018.value as labor_force, unemployed_2018.value/total_2018.value AS unemployment_rate FROM bls_labor_force_statistics unemployed_2018, bls_labor_force_statistics total_2018 WHERE unemployed_2018.period_name = 'Annual' AND unemployed_2018.year = 2018 AND unemployed_2018.age_group = '25 years and over' AND unemployed_2018.labor_force_status = 'Unemployed' AND unemployed_2018.foreign_native_born = 'N/A' AND unemployed_2018.industry_name = 'All Industries' AND unemployed_2018.hispanic_origin = 'All Origins' AND unemployed_2018.RACE = 'All Races' AND unemployed_2018.SEX = 'Both Sexes' AND unemployed_2018.veteran_status = 'N/A' AND unemployed_2018.level_of_education != 'All educational levels' AND total_2018.period_name = 'Annual' AND total_2018.year = 2018 AND total_2018.age_group = '25 years and over' AND total_2018.labor_force_status = 'Civilian labor force' AND total_2018.foreign_native_born = 'N/A' AND total_2018.industry_name = 'All Industries' AND total_2018.hispanic_origin = 'All Origins' AND total_2018.RACE = 'All Races' AND total_2018.SEX = 'Both Sexes' AND total_2018.veteran_status = 'N/A' AND total_2018.level_of_education != 'All educational levels' AND total_2018.level_of_education = unemployed_2018.level_of_education AND total_2018.year = unemployed_2018.year", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "How many people were employed in the construction industry in 2020?", 

    "sql_query": "SELECT value as construction_employment FROM bls_labor_force_statistics WHERE YEAR = 2020 AND industry_name = 'Construction' AND PERIOD_NAME = 'Annual' AND labor_force_status = 'Employed' AND occupation = 'All Occupations' AND age_group = '16 years and over' AND race = 'All Races' AND foreign_native_born = 'N/A' AND hispanic_origin = 'All Origins' AND sex = 'Both Sexes' AND working_status = 'N/A';", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What are the salaries of the states with the highest salaries in 2022?", 

    "sql_query": "SELECT location_name, value * 52 AS median_weekly_earnings FROM bls_earnings WHERE year = 2022 AND location_name != 'U.S. Total' AND measure = 'Median usual weekly earnings - in current dollars (second quartile)' AND union_status = 'N/A' AND industry_name = 'All Industries' AND occupation_name = 'All Occupations' AND education = 'All educational levels' AND age = '16 years and over' AND race = 'All Races' AND national_origin = 'All Origins' AND sex = 'Both Sexes' AND native_foreign_born = 'N/A' ORDER BY value DESC LIMIT 10;", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What was GDP in Washington in 2019?", 

    "sql_query": "SELECT value as gdp_2019 FROM bea_gross_domestic_product_by_year WHERE area_name = 'Washington' AND measurement_name = 'Real GDP by state' AND year = 2019 AND industry_type = 'Total';", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "Where is the unemployment rate the highest?", 

    "sql_query": "SELECT area_name, value AS unemployment_rate FROM bls_local_area_unemployment_statistics WHERE measure = 'unemployment rate' AND year = 2023 AND period_name = 'July' AND seasonal = 'Seasonally Adjusted' AND area_type = 'statewide' ORDER BY unemployment_rate DESC;", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What was the GDP of Michigan in 2013?", 

    "sql_query": "SELECT value FROM bea_gross_domestic_product_by_year WHERE area_name = 'Michigan' AND measurement_name = 'Real GDP by state' AND industry_type = 'Total' AND year = 2013", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What was the GDP of Utah in 2013?", 

    "sql_query": "SELECT value FROM bea_gross_domestic_product_by_year WHERE area_name = 'Utah' AND measurement_name = 'Real GDP by state' AND industry_type = 'Total' AND year = 2013", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What was the GDP of Oregon in 1999?", 

    "sql_query": "SELECT value FROM bea_gross_domestic_product_by_year WHERE area_name = 'Oregon' AND measurement_name = 'Real GDP by state' AND industry_type = 'Total' AND year = 1999", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What was the GDP of Maryland in 2019?", 

    "sql_query": "SELECT value FROM bea_gross_domestic_product_by_year WHERE area_name = 'Maryland' AND measurement_name = 'Real GDP by state' AND industry_type = 'Total' AND year = 2019", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What was the GDP of Connecticut in 1977?", 

    "sql_query": "SELECT value FROM bea_gross_domestic_product_by_year WHERE area_name = 'Connecticut' AND measurement_name = 'Real GDP by state' AND industry_type = 'Total' AND year = 1977", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "Which states have the largest Mining (except oil and gas) industry?", 

    "sql_query": "SELECT year, area_name, industry_name, value FROM bea_gross_domestic_product_by_year WHERE industry_name = 'Mining (except oil and gas)' AND year = ( SELECT MAX(year) FROM bea_gross_domestic_product_by_year WHERE industry_name = 'Mining (except oil and gas)' GROUP BY industry_name ) AND measurement_name = 'Real GDP by state' AND area_type = 'State' ORDER BY value DESC;", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "Which states have the largest Primary metal industries industry?", 

    "sql_query": "SELECT year, area_name, industry_name, value FROM bea_gross_domestic_product_by_year WHERE industry_name = 'Primary metal industries' AND year = ( SELECT MAX(year) FROM bea_gross_domestic_product_by_year WHERE industry_name = 'Primary metal industries' GROUP BY industry_name ) AND measurement_name = 'Real GDP by state' AND area_type = 'State' ORDER BY value DESC;", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "Which states have the largest Accommodation and food services industry?", 

    "sql_query": "SELECT year, area_name, industry_name, value FROM bea_gross_domestic_product_by_year WHERE industry_name = 'Accommodation and food services' AND year = ( SELECT MAX(year) FROM bea_gross_domestic_product_by_year WHERE industry_name = 'Accommodation and food services' GROUP BY industry_name ) AND measurement_name = 'Real GDP by state' AND area_type = 'State' ORDER BY value DESC;", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "Which states have the largest Pipeline transportation industry?", 

    "sql_query": "SELECT year, area_name, industry_name, value FROM bea_gross_domestic_product_by_year WHERE industry_name = 'Pipeline transportation' AND year = ( SELECT MAX(year) FROM bea_gross_domestic_product_by_year WHERE industry_name = 'Pipeline transportation' GROUP BY industry_name ) AND measurement_name = 'Real GDP by state' AND area_type = 'State' ORDER BY value DESC;", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "Which states have the largest Furniture and related product manufacturing industry?", 

    "sql_query": "SELECT year, area_name, industry_name, value FROM bea_gross_domestic_product_by_year WHERE industry_name = 'Furniture and related product manufacturing' AND year = ( SELECT MAX(year) FROM bea_gross_domestic_product_by_year WHERE industry_name = 'Furniture and related product manufacturing' GROUP BY industry_name ) AND measurement_name = 'Real GDP by state' AND area_type = 'State' ORDER BY value DESC;", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What industries most impacted GDP in Oklahoma in 1979?", 

    "sql_query": "SELECT industry_name, value as GDP FROM bea_gross_domestic_product_by_year WHERE area_name = 'Oklahoma' AND year = 1979 AND industry_type = 'Sector' AND measurement_name = 'Real GDP by state' ORDER BY value DESC", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What industries most impacted GDP in Wisconsin in 2005?", 

    "sql_query": "SELECT industry_name, value as GDP FROM bea_gross_domestic_product_by_year WHERE area_name = 'Wisconsin' AND year = 2005 AND industry_type = 'Sector' AND measurement_name = 'Real GDP by state' ORDER BY value DESC", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What industries most impacted GDP in Louisiana in 1988?", 

    "sql_query": "SELECT industry_name, value as GDP FROM bea_gross_domestic_product_by_year WHERE area_name = 'Louisiana' AND year = 1988 AND industry_type = 'Sector' AND measurement_name = 'Real GDP by state' ORDER BY value DESC", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What industries most impacted GDP in Georgia in 2017?", 

    "sql_query": "SELECT industry_name, value as GDP FROM bea_gross_domestic_product_by_year WHERE area_name = 'Georgia' AND year = 2017 AND industry_type = 'Sector' AND measurement_name = 'Real GDP by state' ORDER BY value DESC", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What industries most impacted GDP in Iowa in 2013?", 

    "sql_query": "SELECT industry_name, value as GDP FROM bea_gross_domestic_product_by_year WHERE area_name = 'Iowa' AND year = 2013 AND industry_type = 'Sector' AND measurement_name = 'Real GDP by state' ORDER BY value DESC", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "Which industry contributed most to GDP growth in Colorado in 1994?", 

    "sql_query": "SELECT year, industry_name, value as contribution FROM bea_gross_domestic_product_by_year WHERE area_name = 'Colorado' AND year = 1994 AND industry_type = 'Sector' AND measurement_name = 'Contributions to percent change in real GDP' ORDER BY value DESC", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "Which industry contributed most to GDP growth in Virginia in 1982?", 

    "sql_query": "SELECT year, industry_name, value as contribution FROM bea_gross_domestic_product_by_year WHERE area_name = 'Virginia' AND year = 1982 AND industry_type = 'Sector' AND measurement_name = 'Contributions to percent change in real GDP' ORDER BY value DESC", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "Which industry contributed most to GDP growth in Wisconsin in 1964?", 

    "sql_query": "SELECT year, industry_name, value as contribution FROM bea_gross_domestic_product_by_year WHERE area_name = 'Wisconsin' AND year = 1964 AND industry_type = 'Sector' AND measurement_name = 'Contributions to percent change in real GDP' ORDER BY value DESC", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "Which industry contributed most to GDP growth in Alaska in 1982?", 

    "sql_query": "SELECT year, industry_name, value as contribution FROM bea_gross_domestic_product_by_year WHERE area_name = 'Alaska' AND year = 1982 AND industry_type = 'Sector' AND measurement_name = 'Contributions to percent change in real GDP' ORDER BY value DESC", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "Which industry contributed most to GDP growth in Oklahoma in 1973?", 

    "sql_query": "SELECT year, industry_name, value as contribution FROM bea_gross_domestic_product_by_year WHERE area_name = 'Oklahoma' AND year = 1973 AND industry_type = 'Sector' AND measurement_name = 'Contributions to percent change in real GDP' ORDER BY value DESC", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What product has seen the biggest percent increase in consumer spending between 2010 and 2021 in Kansas?", 

    "sql_query": "SELECT pce2021.product_category_name, pce2021.value AS value2021, pce2010.value AS value2010, (pce2021.value - pce2010.value)/pce2010.value AS rate_of_change FROM bamboo.bea_personal_consumption_expenditures_aggregate pce2021, bamboo.bea_personal_consumption_expenditures_aggregate pce2010 WHERE pce2021.year = 2021 AND pce2021.product_category_type = 'Product Type' AND pce2021.area_name = 'Kansas' AND pce2010.year = 2010 AND pce2010.product_category_type = 'Product Type' AND pce2010.area_name = 'Kansas' AND pce2010.product_category_name = pce2021.product_category_name ORDER BY rate_of_change DESC LIMIT 10;", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What product has seen the biggest percent increase in consumer spending between 2010 and 2021 in Oklahoma?", 

    "sql_query": "SELECT pce2021.product_category_name, pce2021.value AS value2021, pce2010.value AS value2010, (pce2021.value - pce2010.value)/pce2010.value AS rate_of_change FROM bamboo.bea_personal_consumption_expenditures_aggregate pce2021, bamboo.bea_personal_consumption_expenditures_aggregate pce2010 WHERE pce2021.year = 2021 AND pce2021.product_category_type = 'Product Type' AND pce2021.area_name = 'Oklahoma' AND pce2010.year = 2010 AND pce2010.product_category_type = 'Product Type' AND pce2010.area_name = 'Oklahoma' AND pce2010.product_category_name = pce2021.product_category_name ORDER BY rate_of_change DESC LIMIT 10;", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What product has seen the biggest percent increase in consumer spending between 2010 and 2021 in New York?", 

    "sql_query": "SELECT pce2021.product_category_name, pce2021.value AS value2021, pce2010.value AS value2010, (pce2021.value - pce2010.value)/pce2010.value AS rate_of_change FROM bamboo.bea_personal_consumption_expenditures_aggregate pce2021, bamboo.bea_personal_consumption_expenditures_aggregate pce2010 WHERE pce2021.year = 2021 AND pce2021.product_category_type = 'Product Type' AND pce2021.area_name = 'New York' AND pce2010.year = 2010 AND pce2010.product_category_type = 'Product Type' AND pce2010.area_name = 'New York' AND pce2010.product_category_name = pce2021.product_category_name ORDER BY rate_of_change DESC LIMIT 10;", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What product has seen the biggest percent increase in consumer spending between 2010 and 2021 in Ohio?", 

    "sql_query": "SELECT pce2021.product_category_name, pce2021.value AS value2021, pce2010.value AS value2010, (pce2021.value - pce2010.value)/pce2010.value AS rate_of_change FROM bamboo.bea_personal_consumption_expenditures_aggregate pce2021, bamboo.bea_personal_consumption_expenditures_aggregate pce2010 WHERE pce2021.year = 2021 AND pce2021.product_category_type = 'Product Type' AND pce2021.area_name = 'Ohio' AND pce2010.year = 2010 AND pce2010.product_category_type = 'Product Type' AND pce2010.area_name = 'Ohio' AND pce2010.product_category_name = pce2021.product_category_name ORDER BY rate_of_change DESC LIMIT 10;", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What product has seen the biggest percent increase in consumer spending between 2010 and 2021 in Illinois?", 

    "sql_query": "SELECT pce2021.product_category_name, pce2021.value AS value2021, pce2010.value AS value2010, (pce2021.value - pce2010.value)/pce2010.value AS rate_of_change FROM bamboo.bea_personal_consumption_expenditures_aggregate pce2021, bamboo.bea_personal_consumption_expenditures_aggregate pce2010 WHERE pce2021.year = 2021 AND pce2021.product_category_type = 'Product Type' AND pce2021.area_name = 'Illinois' AND pce2010.year = 2010 AND pce2010.product_category_type = 'Product Type' AND pce2010.area_name = 'Illinois' AND pce2010.product_category_name = pce2021.product_category_name ORDER BY rate_of_change DESC LIMIT 10;", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What product has seen the biggest increase in per capita consumer spending between 2010 and 2021 in Tennessee?", 

    "sql_query": "SELECT pce2021.product_category_name, pce2021.value AS value2021, pce2010.value AS value2010, (pce2021.value - pce2010.value)/pce2010.value AS rate_of_change FROM bamboo.bea_personal_consumption_expenditures_per_capita pce2021, bamboo.bea_personal_consumption_expenditures_per_capita pce2010 WHERE pce2021.year = 2021 AND pce2021.product_category_type = 'Product Type' AND pce2021.area_name = 'Tennessee' AND pce2010.year = 2010 AND pce2010.product_category_type = 'Product Type' AND pce2010.area_name = 'Tennessee' AND pce2010.product_category_name = pce2021.product_category_name ORDER BY rate_of_change DESC LIMIT 10;", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What product has seen the biggest increase in per capita consumer spending between 2010 and 2021 in Hawaii?", 

    "sql_query": "SELECT pce2021.product_category_name, pce2021.value AS value2021, pce2010.value AS value2010, (pce2021.value - pce2010.value)/pce2010.value AS rate_of_change FROM bamboo.bea_personal_consumption_expenditures_per_capita pce2021, bamboo.bea_personal_consumption_expenditures_per_capita pce2010 WHERE pce2021.year = 2021 AND pce2021.product_category_type = 'Product Type' AND pce2021.area_name = 'Hawaii' AND pce2010.year = 2010 AND pce2010.product_category_type = 'Product Type' AND pce2010.area_name = 'Hawaii' AND pce2010.product_category_name = pce2021.product_category_name ORDER BY rate_of_change DESC LIMIT 10;", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What product has seen the biggest increase in per capita consumer spending between 2010 and 2021 in Louisiana?", 

    "sql_query": "SELECT pce2021.product_category_name, pce2021.value AS value2021, pce2010.value AS value2010, (pce2021.value - pce2010.value)/pce2010.value AS rate_of_change FROM bamboo.bea_personal_consumption_expenditures_per_capita pce2021, bamboo.bea_personal_consumption_expenditures_per_capita pce2010 WHERE pce2021.year = 2021 AND pce2021.product_category_type = 'Product Type' AND pce2021.area_name = 'Louisiana' AND pce2010.year = 2010 AND pce2010.product_category_type = 'Product Type' AND pce2010.area_name = 'Louisiana' AND pce2010.product_category_name = pce2021.product_category_name ORDER BY rate_of_change DESC LIMIT 10;", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What product has seen the biggest increase in per capita consumer spending between 2010 and 2021 in Missouri?", 

    "sql_query": "SELECT pce2021.product_category_name, pce2021.value AS value2021, pce2010.value AS value2010, (pce2021.value - pce2010.value)/pce2010.value AS rate_of_change FROM bamboo.bea_personal_consumption_expenditures_per_capita pce2021, bamboo.bea_personal_consumption_expenditures_per_capita pce2010 WHERE pce2021.year = 2021 AND pce2021.product_category_type = 'Product Type' AND pce2021.area_name = 'Missouri' AND pce2010.year = 2010 AND pce2010.product_category_type = 'Product Type' AND pce2010.area_name = 'Missouri' AND pce2010.product_category_name = pce2021.product_category_name ORDER BY rate_of_change DESC LIMIT 10;", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What product has seen the biggest increase in per capita consumer spending between 2010 and 2021 in California?", 

    "sql_query": "SELECT pce2021.product_category_name, pce2021.value AS value2021, pce2010.value AS value2010, (pce2021.value - pce2010.value)/pce2010.value AS rate_of_change FROM bamboo.bea_personal_consumption_expenditures_per_capita pce2021, bamboo.bea_personal_consumption_expenditures_per_capita pce2010 WHERE pce2021.year = 2021 AND pce2021.product_category_type = 'Product Type' AND pce2021.area_name = 'California' AND pce2010.year = 2010 AND pce2010.product_category_type = 'Product Type' AND pce2010.area_name = 'California' AND pce2010.product_category_name = pce2021.product_category_name ORDER BY rate_of_change DESC LIMIT 10;", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "How much money do people in Colorado spend on Other services per capita?", 

    "sql_query": "SELECT year, product_category_name, value FROM bea_personal_consumption_expenditures_per_capita WHERE area_name = 'Colorado' AND product_category_name = 'Other services' AND YEAR = (SELECT MAX(YEAR) FROM bea_personal_consumption_expenditures_per_capita WHERE area_name = 'Colorado')", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "How much money do people in Arizona spend on Recreation services per capita?", 

    "sql_query": "SELECT year, product_category_name, value FROM bea_personal_consumption_expenditures_per_capita WHERE area_name = 'Arizona' AND product_category_name = 'Recreation services' AND YEAR = (SELECT MAX(YEAR) FROM bea_personal_consumption_expenditures_per_capita WHERE area_name = 'Arizona')", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "How much money do people in Kansas spend on Food and beverages purchased for off-premises consumption per capita?", 

    "sql_query": "SELECT year, product_category_name, value FROM bea_personal_consumption_expenditures_per_capita WHERE area_name = 'Kansas' AND product_category_name = 'Food and beverages purchased for off-premises consumption' AND YEAR = (SELECT MAX(YEAR) FROM bea_personal_consumption_expenditures_per_capita WHERE area_name = 'Kansas')", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "How much money do people in South Carolina spend on Recreation services per capita?", 

    "sql_query": "SELECT year, product_category_name, value FROM bea_personal_consumption_expenditures_per_capita WHERE area_name = 'South Carolina' AND product_category_name = 'Recreation services' AND YEAR = (SELECT MAX(YEAR) FROM bea_personal_consumption_expenditures_per_capita WHERE area_name = 'South Carolina')", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "How much money do people in Utah spend on Other services per capita?", 

    "sql_query": "SELECT year, product_category_name, value FROM bea_personal_consumption_expenditures_per_capita WHERE area_name = 'Utah' AND product_category_name = 'Other services' AND YEAR = (SELECT MAX(YEAR) FROM bea_personal_consumption_expenditures_per_capita WHERE area_name = 'Utah')", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "How many Quits were there in Retail trade in 2022?", 

    "sql_query": "SELECT data_element, value FROM bls_job_turnover WHERE data_element = 'Quits' AND industry_name = 'Retail trade' AND state = 'Total US' AND size_class = 'All size classes' AND rate_level = 'Level' AND year = 2022 AND month_name = 'Annual' AND seasonal = 'Not Seasonally Adjusted';", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "How many Total separations were there in Health care and social assistance in 2007?", 

    "sql_query": "SELECT data_element, value FROM bls_job_turnover WHERE data_element = 'Total separations' AND industry_name = 'Health care and social assistance' AND state = 'Total US' AND size_class = 'All size classes' AND rate_level = 'Level' AND year = 2007 AND month_name = 'Annual' AND seasonal = 'Not Seasonally Adjusted';", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "How many Other separations were there in Transportation, warehousing, and utilities in 2018?", 

    "sql_query": "SELECT data_element, value FROM bls_job_turnover WHERE data_element = 'Other separations' AND industry_name = 'Transportation, warehousing, and utilities' AND state = 'Total US' AND size_class = 'All size classes' AND rate_level = 'Level' AND year = 2018 AND month_name = 'Annual' AND seasonal = 'Not Seasonally Adjusted';", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "How many Other separations were there in Real estate and rental and leasing in 2001?", 

    "sql_query": "SELECT data_element, value FROM bls_job_turnover WHERE data_element = 'Other separations' AND industry_name = 'Real estate and rental and leasing' AND state = 'Total US' AND size_class = 'All size classes' AND rate_level = 'Level' AND year = 2001 AND month_name = 'Annual' AND seasonal = 'Not Seasonally Adjusted';", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "How many Job openings were there in Education and health services in 2013?", 

    "sql_query": "SELECT data_element, value FROM bls_job_turnover WHERE data_element = 'Job openings' AND industry_name = 'Education and health services' AND state = 'Total US' AND size_class = 'All size classes' AND rate_level = 'Level' AND year = 2013 AND month_name = 'Annual' AND seasonal = 'Not Seasonally Adjusted';", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What is the median salary in Washington state?", 

    "sql_query": "SELECT year, MAX(value) * 52 as median_annual_salary FROM bls_earnings WHERE location_name = 'Washington' AND measure = 'Median usual weekly earnings - in current dollars (second quartile)' AND union_status = 'N/A' AND industry_name = 'All Industries' AND occupation_name = 'All Occupations' AND age = '16 years and over' AND race = 'All Races' AND national_origin = 'All Origins' AND sex = 'Both Sexes' AND native_foreign_born = 'N/A' GROUP BY year ORDER BY year DESC LIMIT 10", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What percent of employees quit their jobs in the Other services industry in October 2015?", 

    "sql_query": "SELECT data_element, industry_name, value FROM bls_job_turnover WHERE data_element = 'Quits' AND industry_name = 'Other services' AND state = 'Total US' AND size_class = 'All size classes' AND rate_level = 'Rate' AND year = 2015 AND month_name = 'October' AND seasonal = 'Seasonally Adjusted';", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What percent of employees quit their jobs in the Government industry in March 2020?", 

    "sql_query": "SELECT data_element, industry_name, value FROM bls_job_turnover WHERE data_element = 'Quits' AND industry_name = 'Government' AND state = 'Total US' AND size_class = 'All size classes' AND rate_level = 'Rate' AND year = 2020 AND month_name = 'March' AND seasonal = 'Seasonally Adjusted';", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What percent of employees quit their jobs in the Leisure and hospitality industry in December 2022?", 

    "sql_query": "SELECT data_element, industry_name, value FROM bls_job_turnover WHERE data_element = 'Quits' AND industry_name = 'Leisure and hospitality' AND state = 'Total US' AND size_class = 'All size classes' AND rate_level = 'Rate' AND year = 2022 AND month_name = 'December' AND seasonal = 'Seasonally Adjusted';", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What percent of employees quit their jobs in the Nondurable goods manufacturing industry in March 2017?", 

    "sql_query": "SELECT data_element, industry_name, value FROM bls_job_turnover WHERE data_element = 'Quits' AND industry_name = 'Nondurable goods manufacturing' AND state = 'Total US' AND size_class = 'All size classes' AND rate_level = 'Rate' AND year = 2017 AND month_name = 'March' AND seasonal = 'Seasonally Adjusted';", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What percent of employees quit their jobs in the Total private industry in April 2005?", 

    "sql_query": "SELECT data_element, industry_name, value FROM bls_job_turnover WHERE data_element = 'Quits' AND industry_name = 'Total private' AND state = 'Total US' AND size_class = 'All size classes' AND rate_level = 'Rate' AND year = 2005 AND month_name = 'April' AND seasonal = 'Seasonally Adjusted';", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "Which industries had the most job openings in Oregon in 2011?", 

    "sql_query": "SELECT year, industry_name, data_element, value FROM bls_job_turnover WHERE data_element = 'Job openings' AND state = 'Oregon' AND size_class = 'All size classes' AND rate_level = 'Level' AND year = 2011 AND month_name = 'Annual' AND industry_name != 'Total nonfarm' AND industry_name != 'Total private' AND industry_name != 'Other services' ORDER BY value DESC", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "Which industries had the most job openings in Maryland in 2021?", 

    "sql_query": "SELECT year, industry_name, data_element, value FROM bls_job_turnover WHERE data_element = 'Job openings' AND state = 'Maryland' AND size_class = 'All size classes' AND rate_level = 'Level' AND year = 2021 AND month_name = 'Annual' AND industry_name != 'Total nonfarm' AND industry_name != 'Total private' AND industry_name != 'Other services' ORDER BY value DESC", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "Which industries had the most job openings in West region in 2022?", 

    "sql_query": "SELECT year, industry_name, data_element, value FROM bls_job_turnover WHERE data_element = 'Job openings' AND state = 'West region' AND size_class = 'All size classes' AND rate_level = 'Level' AND year = 2022 AND month_name = 'Annual' AND industry_name != 'Total nonfarm' AND industry_name != 'Total private' AND industry_name != 'Other services' ORDER BY value DESC", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "Which industries had the most job openings in Nevada in 2011?", 

    "sql_query": "SELECT year, industry_name, data_element, value FROM bls_job_turnover WHERE data_element = 'Job openings' AND state = 'Nevada' AND size_class = 'All size classes' AND rate_level = 'Level' AND year = 2011 AND month_name = 'Annual' AND industry_name != 'Total nonfarm' AND industry_name != 'Total private' AND industry_name != 'Other services' ORDER BY value DESC", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "Which industries had the most job openings in Mississippi in 2009?", 

    "sql_query": "SELECT year, industry_name, data_element, value FROM bls_job_turnover WHERE data_element = 'Job openings' AND state = 'Mississippi' AND size_class = 'All size classes' AND rate_level = 'Level' AND year = 2009 AND month_name = 'Annual' AND industry_name != 'Total nonfarm' AND industry_name != 'Total private' AND industry_name != 'Other services' ORDER BY value DESC", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What percent of Florida's economy is the Petroleum and coal products industry in 2022?", 

    "sql_query": "SELECT gdpindustry.year AS year, gdptotal.value AS total_gdp, gdpindustry.value AS industry_GDP, gdpindustry.value/gdptotal.value AS industry_proportion FROM bea_gross_domestic_product_by_year AS gdptotal, bea_gross_domestic_product_by_year AS gdpindustry WHERE gdptotal.area_name = 'Florida' AND gdptotal.year = 2022 AND gdptotal.industry_type = 'Total' AND gdptotal.measurement_name = 'Real GDP by state' AND gdpindustry.area_name = 'Florida' AND gdpindustry.year = 2022 AND gdpindustry.industry_name = 'Petroleum and coal products' AND gdpindustry.measurement_name = 'Real GDP by state'", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What percent of Illinois's economy is the Petroleum and coal products manufacturing industry in 2022?", 

    "sql_query": "SELECT gdpindustry.year AS year, gdptotal.value AS total_gdp, gdpindustry.value AS industry_GDP, gdpindustry.value/gdptotal.value AS industry_proportion FROM bea_gross_domestic_product_by_year AS gdptotal, bea_gross_domestic_product_by_year AS gdpindustry WHERE gdptotal.area_name = 'Illinois' AND gdptotal.year = 2022 AND gdptotal.industry_type = 'Total' AND gdptotal.measurement_name = 'Real GDP by state' AND gdpindustry.area_name = 'Illinois' AND gdpindustry.year = 2022 AND gdpindustry.industry_name = 'Petroleum and coal products manufacturing' AND gdpindustry.measurement_name = 'Real GDP by state'", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What percent of Colorado's economy is the Insurance carriers and related activities industry in 2022?", 

    "sql_query": "SELECT gdpindustry.year AS year, gdptotal.value AS total_gdp, gdpindustry.value AS industry_GDP, gdpindustry.value/gdptotal.value AS industry_proportion FROM bea_gross_domestic_product_by_year AS gdptotal, bea_gross_domestic_product_by_year AS gdpindustry WHERE gdptotal.area_name = 'Colorado' AND gdptotal.year = 2022 AND gdptotal.industry_type = 'Total' AND gdptotal.measurement_name = 'Real GDP by state' AND gdpindustry.area_name = 'Colorado' AND gdpindustry.year = 2022 AND gdpindustry.industry_name = 'Insurance carriers and related activities' AND gdpindustry.measurement_name = 'Real GDP by state'", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What percent of Michigan's economy is the Fabricated metal products industry in 2022?", 

    "sql_query": "SELECT gdpindustry.year AS year, gdptotal.value AS total_gdp, gdpindustry.value AS industry_GDP, gdpindustry.value/gdptotal.value AS industry_proportion FROM bea_gross_domestic_product_by_year AS gdptotal, bea_gross_domestic_product_by_year AS gdpindustry WHERE gdptotal.area_name = 'Michigan' AND gdptotal.year = 2022 AND gdptotal.industry_type = 'Total' AND gdptotal.measurement_name = 'Real GDP by state' AND gdpindustry.area_name = 'Michigan' AND gdpindustry.year = 2022 AND gdpindustry.industry_name = 'Fabricated metal products' AND gdpindustry.measurement_name = 'Real GDP by state'", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What percent of Tennessee's economy is the Electronic equipment and instruments industry in 2022?", 

    "sql_query": "SELECT gdpindustry.year AS year, gdptotal.value AS total_gdp, gdpindustry.value AS industry_GDP, gdpindustry.value/gdptotal.value AS industry_proportion FROM bea_gross_domestic_product_by_year AS gdptotal, bea_gross_domestic_product_by_year AS gdpindustry WHERE gdptotal.area_name = 'Tennessee' AND gdptotal.year = 2022 AND gdptotal.industry_type = 'Total' AND gdptotal.measurement_name = 'Real GDP by state' AND gdpindustry.area_name = 'Tennessee' AND gdpindustry.year = 2022 AND gdpindustry.industry_name = 'Electronic equipment and instruments' AND gdpindustry.measurement_name = 'Real GDP by state'", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "Which industries grew the most between 2010 and 2020 in Georgia?", 

    "sql_query": "SELECT gdp2020.industry_name, gdp2020.value AS value_2020, gdp2010.value AS value_2010, (gdp2020.value - gdp2010.value)/gdp2010.value AS gdp_percent_change FROM bea_gross_domestic_product_by_year AS gdp2020, bea_gross_domestic_product_by_year AS gdp2010 WHERE gdp2020.area_name = 'Georgia' AND gdp2020.year = 2020 AND gdp2020.industry_type = 'Sector' AND gdp2020.measurement_name = 'Real GDP by state' AND gdp2010.area_name = 'Georgia' AND gdp2010.year = 2010 AND gdp2010.industry_type = 'Sector' AND gdp2010.measurement_name = 'Real GDP by state' AND gdp2020.area_name = gdp2010.area_name AND gdp2020.industry_name = gdp2010.industry_name ORDER BY gdp_percent_change DESC;", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "Which industries grew the most between 2010 and 2020 in Oklahoma?", 

    "sql_query": "SELECT gdp2020.industry_name, gdp2020.value AS value_2020, gdp2010.value AS value_2010, (gdp2020.value - gdp2010.value)/gdp2010.value AS gdp_percent_change FROM bea_gross_domestic_product_by_year AS gdp2020, bea_gross_domestic_product_by_year AS gdp2010 WHERE gdp2020.area_name = 'Oklahoma' AND gdp2020.year = 2020 AND gdp2020.industry_type = 'Sector' AND gdp2020.measurement_name = 'Real GDP by state' AND gdp2010.area_name = 'Oklahoma' AND gdp2010.year = 2010 AND gdp2010.industry_type = 'Sector' AND gdp2010.measurement_name = 'Real GDP by state' AND gdp2020.area_name = gdp2010.area_name AND gdp2020.industry_name = gdp2010.industry_name ORDER BY gdp_percent_change DESC;", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "Which industries grew the most between 2010 and 2020 in Virginia?", 

    "sql_query": "SELECT gdp2020.industry_name, gdp2020.value AS value_2020, gdp2010.value AS value_2010, (gdp2020.value - gdp2010.value)/gdp2010.value AS gdp_percent_change FROM bea_gross_domestic_product_by_year AS gdp2020, bea_gross_domestic_product_by_year AS gdp2010 WHERE gdp2020.area_name = 'Virginia' AND gdp2020.year = 2020 AND gdp2020.industry_type = 'Sector' AND gdp2020.measurement_name = 'Real GDP by state' AND gdp2010.area_name = 'Virginia' AND gdp2010.year = 2010 AND gdp2010.industry_type = 'Sector' AND gdp2010.measurement_name = 'Real GDP by state' AND gdp2020.area_name = gdp2010.area_name AND gdp2020.industry_name = gdp2010.industry_name ORDER BY gdp_percent_change DESC;", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "Which industries grew the most between 2010 and 2020 in New Jersey?", 

    "sql_query": "SELECT gdp2020.industry_name, gdp2020.value AS value_2020, gdp2010.value AS value_2010, (gdp2020.value - gdp2010.value)/gdp2010.value AS gdp_percent_change FROM bea_gross_domestic_product_by_year AS gdp2020, bea_gross_domestic_product_by_year AS gdp2010 WHERE gdp2020.area_name = 'New Jersey' AND gdp2020.year = 2020 AND gdp2020.industry_type = 'Sector' AND gdp2020.measurement_name = 'Real GDP by state' AND gdp2010.area_name = 'New Jersey' AND gdp2010.year = 2010 AND gdp2010.industry_type = 'Sector' AND gdp2010.measurement_name = 'Real GDP by state' AND gdp2020.area_name = gdp2010.area_name AND gdp2020.industry_name = gdp2010.industry_name ORDER BY gdp_percent_change DESC;", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "Which industries grew the most between 2010 and 2020 in Mississippi?", 

    "sql_query": "SELECT gdp2020.industry_name, gdp2020.value AS value_2020, gdp2010.value AS value_2010, (gdp2020.value - gdp2010.value)/gdp2010.value AS gdp_percent_change FROM bea_gross_domestic_product_by_year AS gdp2020, bea_gross_domestic_product_by_year AS gdp2010 WHERE gdp2020.area_name = 'Mississippi' AND gdp2020.year = 2020 AND gdp2020.industry_type = 'Sector' AND gdp2020.measurement_name = 'Real GDP by state' AND gdp2010.area_name = 'Mississippi' AND gdp2010.year = 2010 AND gdp2010.industry_type = 'Sector' AND gdp2010.measurement_name = 'Real GDP by state' AND gdp2020.area_name = gdp2010.area_name AND gdp2020.industry_name = gdp2010.industry_name ORDER BY gdp_percent_change DESC;", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What is the employment rate trend over the years in the US?", 

    "sql_query": "SELECT year, value FROM bls_current_employment WHERE data_type = 'ALL EMPLOYEES, THOUSANDS' AND period_name = 'Annual Average' AND industry_name = 'Total nonfarm' ORDER BY year DESC LIMIT 10;", 

    "db_alias": "usafacts_postgres" 

  }, 

  { 

    "question": "What is the median annual income for the top 10 states with the highest GDP?", 

    "sql_query": "SELECT location_name, value * 52 AS median_annual_income  FROM bls_earnings  WHERE year = (SELECT MAX(year) FROM bls_earnings)  AND measure = 'Median usual weekly earnings - in current dollars (second quartile)'  AND location_name IN (SELECT area_name FROM bea_gross_domestic_product_by_year WHERE measurement_name = 'Real GDP by state' AND industry_type = 'Total' AND area_type = 'State' AND year = ( SELECT MAX(year) FROM bea_gross_domestic_product_by_year WHERE measurement_name = 'Real GDP by state' AND industry_type = 'Total' ) ORDER BY value DESC LIMIT 10)  AND union_status = 'N/A' AND industry_name = 'All Industries' AND occupation_name = 'All Occupations' AND education = 'All educational levels' AND age = '16 years and over' AND race = 'All Races' AND national_origin = 'All Origins' AND sex = 'Both Sexes' AND native_foreign_born = 'N/A' ORDER BY median_annual_income DESC  LIMIT 10; -- This query selects the top 10 states in terms of GDP, then calculates the median annual earnings for those states", 

    "db_alias": "usafacts_postgres" 

  } 

] 