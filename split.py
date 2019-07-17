from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.errors import AnsibleError, AnsibleFilterError

try:
    import re
    HAS_LIB = True
except ImportError:
    HAS_LIB = False

def split_string(string, separator=' '):
    '''Split string into a list using delimiter. Example:
    - debug: msg="{{ csv | split(",") }}"
    '''
    if not string:
      return None

    try:
        return string.split(separator)
    except Exception, e:
        raise AnsibleFilterError('split filter plugin error: %s, provided string: "%s"' % str(e),str(data) )

def split_regex(string, separator_pattern='\s+'):

    if not HAS_LIB:
      raise AnsibleError('Python RegEx Module not available. ')

    if not string:
      return None
                   
    try:
        return re.split(separator_pattern, string)
    except Exception, e:
        raise AnsibleFilterError('split filter plugin error: %s, provided string: "%s"' % str(e),str(string) )

class FilterModule(object):
    ''' A filter to split a string into a list. '''
    def filters(self):
        return {
            'split' : split_string,
            'split_regex' : split_regex,
        }