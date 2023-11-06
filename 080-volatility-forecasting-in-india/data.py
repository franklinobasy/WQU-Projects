"""This is for all the code used to interact with the AlphaVantage API
and the SQLite database. Remember that the API relies on a key that is
stored in your `.env` file and imported via the `config` module.
"""

import sqlite3

import pandas as pd
import requests
from config import settings


class AlphaVantageAPI:
    def __init__():
    
        pass

    def get_daily():
    
        """Get daily time series of an equity from AlphaVantage API.

        Parameters
        ----------
        ticker : str
            The ticker symbol of the equity.
        output_size : str, optional
            Number of observations to retrieve. "compact" returns the
            latest 100 observations. "full" returns all observations for
            equity. By default "full".

        Returns
        -------
        pd.DataFrame
            Columns are 'open', 'high', 'low', 'close', and 'volume'.
            All columns are numeric.
        """
        

        # Send request to API
        

        # Check if there's been an error
        

        # Clean results
        

        # Return results
        pass


class SQLRepository:
    def __init__():

        pass

    def insert_table():
    
        """Insert DataFrame into SQLite database as table

        Parameters
        ----------
        table_name : str
        records : pd.DataFrame
        if_exists : str, optional
            How to behave if the table already exists.

            - 'fail': Raise a ValueError.
            - 'replace': Drop the table before inserting new values.
            - 'append': Insert new values to the existing table.

            Dafault: 'fail'

        Returns
        -------
        dict
            Dictionary has two keys:

            - 'transaction_successful', followed by bool
            - 'records_inserted', followed by int
        """
        
        pass

    def read_table():
    
        """Read table from database.

        Parameters
        ----------
        table_name : str
            Name of table in SQLite database.
        limit : int, None, optional
            Number of most recent records to retrieve. If `None`, all
            records are retrieved. By default, `None`.

        Returns
        -------
        pd.DataFrame
            Index is DatetimeIndex "date". Columns are 'open', 'high',
            'low', 'close', and 'volume'. All columns are numeric.
        """
        # Create SQL query (with optional limit)
        

        # Retrieve data, read into DataFrame
        

        # Return DataFrame
        pass
