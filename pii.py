__author__ = "Younes Karimi"
__email__ = "younes@psu.edu"
__description__ = "This file contains functions for extracting Personally Identifiable Information (PII) from text. (To be completed for other types of PII)"

import re

def extract_ssns(text, verbose=None):
    """Takes a piece of text and returns all the social security numbers (SSNs) 
    it finds in the text.

    Args:
        text (string): The input string in which we search for SSNs

    Returns:
        list: A list of SSNs extracted from the input text
    """
    invalid_looking_ssns = [
        '111-11-1111',
        '222-22-2222',
        '333-33-3333',
        '444-44-4444',
        '555-55-5555',
        '666-66-6666',
        '777-77-7777',
        '888-88-8888',
        '999-99-9999',
        '123-45-6789',
        '078-05-1120',
        '420-69-6969',
        '420-69-6669',
        '420-69-6666',
        '420-69-1488',
        '420-69-1337',
        '420-69-8008',
        '420-69-1312',
        '420-69-1313',
        '420-69-1234',
        '420-69-2001',
        '420-69-1969',
        '420-69-1738',
        '696-96-9696'
    ]
    ssns = re.findall(r'((?!000|666)[0-8][0-9]{2}-(?!00)[0-9]{2}-(?!0000)[0-9]{4})', text)
    for ssn in ssns:
        # remove SSN-like digits that may belong to a URL or another number
        if text.find('-' + ssn) > -1 or text.find(ssn + '-') > -1:
            ssns.remove(ssn)
            continue
        # remove SSNs that are listed as invalid-looking
        if ssn in invalid_looking_ssns:
            ssns.remove(ssn)
            if verbose:
                if ssn == '078-05-1120':
                    print('>>> woolworth ssn')
                elif ssn.find('420-69-') == 0:
                    print('>>> Unknown SSN that starts with 420-69:  ', ssn)
            continue
        # remove SSN-like digits that are part of a longer string of digits
        prev_indx = text.find(ssn) - 1
        next_indx = text.find(ssn) + 11
        if prev_indx >= 0:
            if text[prev_indx].isdigit():
                ssns.remove(ssn)
                # replace the first instance of an invalid SSN with void for 
                # cases where there are multiple instances of an invalid SSN 
                # exist in a piece of text and the 'find' funtion only finds the 
                # first instance.
                text = text.replace(ssn, ' ')
                continue
        if next_indx < len(text):
            if text[next_indx].isdigit():
                ssns.remove(ssn)
                # replace the first instance of an invalid SSN with void
                text = text.replace(ssn, ' ')
    return ssns

def has_ssn_kws(text):
    for kw in ['ssn', 'social security', 'sn', 'social number']:
        if text.lower().find(kw) > -1:
            return True
    return False

def has_ssn(text):
    if len(extract_ssns(text)) == 0:
        return False
    return has_ssn_kws(text)

def extract_ips(text):
    """Takes a piece of text and returns all the IP addresses it finds in the 
    text.

    Args:
        text (string): The input string in which we search for SSNs

    Returns:
        list: A list of SSNs extracted from the input text
    """
    ips = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', text)
    for ip in ips:
        # remove IP-like digits that do not follow the IPv4 standard
        invalid = False
        for part in ip.split('.'):
            try:
                if int(part) > 255 or part.startswith('0'):
                    ips.remove(ip)
                    # replace the first instance of an invalid IP with void for 
                    # cases where there are multiple instances of an invalid IP 
                    # exist in a piece of text and the 'find' funtion only finds 
                    # the first instance.
                    text = text.replace(ip, ' ')
                    invalid = True
                    break
            except:
                pass
        if invalid:
            continue
        # remove typical non-sensitive IP addresses
        if (ip.find('192.168') == 0) \
            or (ip.find('127.0.0') == 0) \
            or (ip.find('8.8.8.8') == 0) \
            or (ip.find('0.0.0.0') == 0) \
            or (ip.find('255.255.255') == 0):
            ips.remove(ip)
            text = text.replace(ip, ' ')
            continue
        # remove IP-like digits that are part of a longer string of digits
        prev_indx = text.find(ip) - 1
        next_indx = text.find(ip) + len(ip)
        if prev_indx >= 0:
            # remove IP-like digits that are part of a URL
            if text[prev_indx].isdigit() \
                or text[prev_indx] == '/' \
                or text[prev_indx] == ':' \
                or text[prev_indx] == '-':
                ips.remove(ip)
                text = text.replace(ip, ' ')
                continue
        if prev_indx - 1 >= 0:
            # remove IP-like digits that are part of a longer struct
            if text[prev_indx - 1].isdigit() and text[prev_indx] == '.':
                ips.remove(ip)
                text = text.replace(ip, ' ')
                continue
        if next_indx < len(text):
            # remove IP-like digits that are part of a URL
            if text[next_indx].isdigit() \
                or text[next_indx] == '/' \
                or text[next_indx] == ':' \
                or text[next_indx] == '-':
                ips.remove(ip)
                text = text.replace(ip, ' ')
                continue
        if next_indx + 1 < len(text):
            # remove IP-like digits that are part of a longer struct
            if text[next_indx + 1].isdigit() and text[next_indx] == '.':
                ips.remove(ip)
                text = text.replace(ip, ' ')
                continue
    return ips

def has_ip_kws(text):
  for kw in ['ip ']:
    if text.lower().find(kw) > -1:
      return True
  return False

def has_ip(text):
    if len(extract_ips(text)) == 0:
        return False
    return has_ip_kws(text)

def has_phone(text):
    phones = re.findall(r'(\d{3}[-\s]??\d{3}[-\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4})', text)
    for phone in phones:
        if (phone.find(' ') > 0) or (phone.find('-') > 0):
            return True
    return False