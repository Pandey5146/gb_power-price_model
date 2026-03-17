# GB Power Price Forecast Model

This project builds a fundamental electricity price model for the GB power market.

The model uses:

• Wind forecast data (NESO API)
• Demand forecast data
• Residual demand modelling
• Gas price fundamentals
• Linear regression price modelling

Outputs generated:

• Forward electricity price curve
• Residual demand analytics
• Trading signal classification
• Historical model training dataset

Project structure:

src/        → data extraction and cleaning scripts  
notebooks/  → analysis and modelling  
data/       → processed datasets  
db/         → SQLite market database  

Author: Shubham Pandey