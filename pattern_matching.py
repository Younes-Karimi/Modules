__author__ = "Younes Karimi"
__email__ = "younes@psu.edu"
__description__ = """This file contains functions for extracting pieces of text 
                        that match a specific syntax or pattern"""

import re
from urllib.parse import urlparse

def has_ssn(text):
    return True if len(re.findall(r'((?!000|666)[0-8][0-9]{2}-(?!00)[0-9]{2}-(?!0000)[0-9]{4})', text)) > 0 else False

def has_ip(text):
    return True if len(re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', text)) > 0 else False

def has_phone(text):
    phones = re.findall(r'(\d{3}[-\s]??\d{3}[-\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4})', text)
    for phone in phones:
        if (phone.find(' ') > 0) or (phone.find('-') > 0):
            return True
    return False

def extract_domain(url):
    """
    Extracts domain from URL that has scheme (http, https). If no scheme is 
    present, returns an empty string. If a URL has subdomains, this function
    cannot extract the main domain/website.
    """
    url = urlparse(url).netloc
    return url.split('www.')[1] if url.find('www.') >= 0 else url