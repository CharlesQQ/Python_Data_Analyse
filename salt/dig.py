from __future__ import absolute_import

# Import salt libs
import salt.utils

# Import python libs
import logging
import re
import socket

log = logging.getLogger(__name__)

__virtualname__ = 'dig'


def __virtual__():
    '''
    Only load module if dig binary is present
    '''
    return True if salt.utils.which('dig') else False

def A(host, nameserver=None):
    '''
    Return the A record for ``host``.

    Always returns a list.

    CLI Example:

    .. code-block:: bash

        salt ns1 dig.A www.google.com
    '''
    dig = ['dig', '+short', str(host), 'A']

    if nameserver is not None:
        dig.append('@{0}'.format(nameserver))

    cmd = __salt__['cmd.run_all'](dig, python_shell=False)
    # In this case, 0 is not the same as False
    if cmd['retcode'] != 0:
        log.warn(
            'dig returned exit code \'{0}\'. Returning empty list as '
            'fallback.'.format(
                cmd['retcode']
            )
        )
        return []

    # make sure all entries are IPs
    return [x for x in cmd['stdout'].split('\n') if check_ip(x)]