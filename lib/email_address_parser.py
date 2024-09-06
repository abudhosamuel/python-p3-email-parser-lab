# your code goes here!

import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):
        # Use regex to find all valid email addresses
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = re.findall(email_pattern, self.email_addresses)
        
        # Remove duplicates by converting to a set, then return a sorted list
        unique_emails = sorted(set(emails))
        
        return unique_emails

