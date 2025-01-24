from decimal import Decimal
import pandas as pd

def clean_gross(value):
    """Clean and convert gross value to Decimal."""
    if pd.isna(value) or not value or value == 'NA':
        return None
        
    try:
        if not isinstance(value, str):
            value = str(value)
            
        cleaned = value.replace('$', '').replace(',', '')
        multiplier = 1
        
        if cleaned.endswith('M'):
            multiplier = 1000000
            cleaned = cleaned[:-1]
        elif cleaned.endswith('K'):
            multiplier = 1000
            cleaned = cleaned[:-1]
            
        float_val = float(cleaned) * multiplier
        return Decimal(str(float_val))
    except (ValueError, TypeError) as e:
        return None

def clean_year(value):
    """Clean and convert year value to integer."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

def clean_rating(value):
    """Clean and convert rating value to float."""
    try:
        return float(value)
    except (ValueError, TypeError):
        return None

def clean_votes(value):
    """Clean and convert votes value to integer."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

def clean_runtime(value):
    """Clean and convert runtime value to integer."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return None 