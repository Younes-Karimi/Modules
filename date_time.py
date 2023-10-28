__author__ = "Younes Karimi"
__email__ = "younes@psu.edu"
__description__ = "This file contains functions for processing time and date"

from datetime import datetime
import time

def time():
  return datetime.now().strftime("%H:%M:%S")

def extract_month_day(date_str):
  """Returns concatenation of month and day from tweet creation timestamp"""
  return '-'.join(time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(date_str,'%Y-%m-%dT%H:%M:%S.%fZ')).split()[0].split('-')[1:3]) # datetime format for the new API

