#!/usr/bin/env python3

import amulet
import requests
import unittest

seconds=1000
class TestDeployment(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.deployment = amulet.Deployment(series='trusty')

        cls.deployment.add('centos')

        try:
            cls.deployment.setup(timeout=seconds)
            cls.deployment.sentry.wait()
        except amulet.helpers.TimeoutError:
            message='Environment not deployed in {0} seconds'.format(seconds)
            amulet.raise_status(amulet.SKIP, msg=message)
        except:
            raise

    def test_case(self):
        centos_unit = self.deployment.sentry.unit['centos'][0]
        # More information on writing Amulet tests can be found at:
        #     https://jujucharms.com/docs/stable/tools-amulet
        output, retcode = centos_unit.run('cat /etc/centos-release')
        print(output)
        if retcode != 0 or 'CentOS' not in output:
            amulet.raise_status(amulet.FAIL, msg="Not a CentOS environment")


if __name__ == '__main__':
    unittest.main()
