"""
Data Cleaning Utility Module - Provides functions for cleaning and normalizing movie data.
This module contains utility functions that handle data type conversion, validation,
and normalization for various movie attributes like gross earnings, year, rating, etc.
"""

from decimal import Decimal
import pandas as pd

def clean_gross(value):
    """
    Clean and convert gross earnings value to Decimal type.
    
    Handles various formats including:
    - Dollar signs ($)
    - Comma separators
    - Millions (M) and thousands (K) suffixes
    - Various numeric formats
    
    Args:
        value: Raw gross earnings value (can be string, float, or int)
        
    Returns:
        Decimal: Cleaned gross earnings value
        None: If value is invalid or cannot be converted
    
    Examples:
        >>> clean_gross('$1.5M')  # Returns Decimal('1500000')
        >>> clean_gross('500K')   # Returns Decimal('500000')
        >>> clean_gross('NA')     # Returns None
    """
    if pd.isna(value) or not value or value == 'NA':
        return None
        
    try:
        # Convert to string if not already
        if not isinstance(value, str):
            value = str(value)
            
        # Remove currency symbols and separators
        cleaned = value.replace('$', '').replace(',', '')
        multiplier = 1
        
        # Handle suffixes and convert to full numbers
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
    """
    Clean and convert year value to integer type.
    
    Args:
        value: Raw year value (can be string, float, or int)
        
    Returns:
        int: Cleaned year value
        None: If value is invalid or cannot be converted
    
    Examples:
        >>> clean_year('2020')  # Returns 2020
        >>> clean_year(2019.0)  # Returns 2019
        >>> clean_year('NA')    # Returns None
    """
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

def clean_rating(value):
    """
    Clean and convert rating value to float type.
    
    Args:
        value: Raw rating value (can be string, float, or int)
        
    Returns:
        float: Cleaned rating value
        None: If value is invalid or cannot be converted
    
    Examples:
        >>> clean_rating('8.5')  # Returns 8.5
        >>> clean_rating(7)      # Returns 7.0
        >>> clean_rating('NA')   # Returns None
    """
    try:
        return float(value)
    except (ValueError, TypeError):
        return None

def clean_votes(value):
    """
    Clean and convert vote count value to integer type.
    
    Args:
        value: Raw vote count value (can be string, float, or int)
        
    Returns:
        int: Cleaned vote count value
        None: If value is invalid or cannot be converted
    
    Examples:
        >>> clean_votes('1000')  # Returns 1000
        >>> clean_votes(500.0)   # Returns 500
        >>> clean_votes('NA')    # Returns None
    """
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

def clean_runtime(value):
    """
    Clean and convert runtime value to integer type.
    
    Args:
        value: Raw runtime value in minutes (can be string, float, or int)
        
    Returns:
        int: Cleaned runtime value in minutes
        None: If value is invalid or cannot be converted
    
    Examples:
        >>> clean_runtime('120')  # Returns 120
        >>> clean_runtime(90.5)   # Returns 90
        >>> clean_runtime('NA')   # Returns None
    """
    try:
        return int(value)
    except (ValueError, TypeError):
        return None 