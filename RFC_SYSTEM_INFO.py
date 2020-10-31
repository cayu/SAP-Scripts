#!/usr/bin/env python
from pyrfc import Connection, ABAPApplicationError, ABAPRuntimeError, LogonError, CommunicationError
from configparser import ConfigParser
from pprint import PrettyPrinter

def main():

    try:
        config = ConfigParser()
        config.read('sap_conn.cfg')
        params_connection = config._sections['connection']
        conn = Connection(**params_connection)

        result = conn.call('RFC_SYSTEM_INFO')

        pp = PrettyPrinter(indent=4)
        pp.pprint(result)

    except CommunicationError:
        print ("Could not connect to server.")
        raise
    except LogonError:
        print ("Could not log in. Wrong credentials?")
        raise
    except (ABAPApplicationError, ABAPRuntimeError):
        print ("An error occurred.")
        raise

if __name__ == '__main__':
    main()
