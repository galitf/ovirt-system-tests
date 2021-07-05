# -*- coding: utf-8 -*-
#
# Copyright 2021 Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA
#
# Refer to the README and COPYING files for full details of the license
#

import pytest

from ost_utils import engine_object_names
from ost_utils.pytest.fixtures.backend import backend
from ost_utils.pytest.fixtures.backend import hosts_hostnames


@pytest.fixture(scope="session")
def ost_dc_name():
    return engine_object_names.TEST_DC_NAME


@pytest.fixture(scope="session")
def ost_cluster_name():
    return engine_object_names.TEST_CLUSTER_NAME


@pytest.fixture(scope="session")
def hostnames_to_add(hosts_hostnames):
    return hosts_hostnames


@pytest.fixture(scope="session")
def hostnames_to_reboot(hosts_hostnames):
    return hosts_hostnames[:1]


@pytest.fixture(scope="session")
def deploy_hosted_engine():
    return False


@pytest.fixture(scope="session")
def ansible_vms_to_deploy(ansible_all):
    return ansible_all
