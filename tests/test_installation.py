"""
Role tests
"""

from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_packages_installed(host):
    """
    Test packages installed
    """

    packages = ['ca-certificates', 'odoo']

    for package in packages:
        assert host.package(package).is_installed


def test_repository_file(host):
    """
    Test repository file properties
    """

    f_path = '/etc/apt/sources.list.d/nightly_odoo_com_10_0_nightly_deb.list'

    assert host.file(f_path).exists
    assert host.file(f_path).is_file
    assert host.file(f_path).user == 'root'
    assert host.file(f_path).group == 'root'
    assert host.file(f_path).mode == 0o644


def test_service(host):
    """
    Check if Odoo service is started and enabled
    """

    service = ''

    if host.system_info.distribution in ('debian', 'ubuntu'):
        service = 'odoo'

    assert host.service(service).is_enabled

    # Systemctl not available with Docker images
    if 'docker' != host.backend.NAME:
        assert host.service(service).is_running


def test_system_user(host):
    """
    Check if system user exists
    """

    if host.system_info.distribution in ('debian', 'ubuntu'):
        assert host.user('odoo').exists
        assert host.user('odoo').group == 'odoo'
        assert host.user('odoo').home == '/var/lib/odoo'
        assert host.user('odoo').shell == '/bin/false'


def test_config_file(host):
    """
    Check if configuration file exists
    """

    config_file = ''

    if host.system_info.distribution in ('debian', 'ubuntu'):
        config_file = '/etc/odoo/odoo.conf'

    assert host.file(config_file).exists
    assert host.file(config_file).user == 'odoo'
    assert host.file(config_file).group == 'odoo'
    assert host.file(config_file).mode == 0o640
