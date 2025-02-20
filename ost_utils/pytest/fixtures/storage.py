#
# Copyright oVirt Authors
# SPDX-License-Identifier: GPL-2.0-or-later
#
#

import functools
import pytest

from ost_utils import network_utils


@pytest.fixture(scope="session")
def storage_ips_for_network(ansible_storage_facts, backend):
    return functools.partial(network_utils.get_ips, backend, ansible_storage_facts)


@pytest.fixture(scope="session")
def storage_management_ips(storage_ips_for_network, management_network_name):
    return storage_ips_for_network(management_network_name)


@pytest.fixture(scope="session")
def sd_iscsi_host_ip():
    # return only one IP since we want to connect to just one endpoint
    return 'Please override sd_iscsi_host_ip'


@pytest.fixture(scope="session")
def sd_nfs_host_storage_name():
    return 'Please override sd_nfs_host_storage_name'


@pytest.fixture(scope="session")
def sd_iscsi_ansible_host():
    return 'Please override sd_iscsi_ansible_host'
