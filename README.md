# GB Power Price Forecast Model

This project builds a fundamental electricity price model for the GB power market.

## Model Inputs
- Wind forecast data (NESO API)
- Demand forecast data
- Residual demand modelling
- Historical price data
- Gas price research input

## Core Logic
The model estimates GB power prices using:

- Wind → Residual Demand → Price
- Demand → Residual Demand → Price
- Gas as a baseline price driver

## Outputs
- Forward electricity price curve
- Residual demand analytics
- Trading signal classification
- Historical model training dataset

## Project Structure
- `src/` → data extraction and cleaning scripts
- `notebooks/` → analysis and modelling
- `data/` → processed datasets
- `db/` → SQLite database

## Current Status
Built:
- NESO wind forecast pipeline
- NESO demand forecast pipeline
- Historical demand and wind dataset
- Residual demand model
- Linear regression price model
- Forward price curve
- Trading signals

Next upgrades:
- Carbon price
- Interconnector effects
- Nonlinear / regime models
- Machine learning models

Author: Shubham Pandey