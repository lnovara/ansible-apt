import os
import pytest
import testinfra.utils.ansible_runner
import yaml


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.fixture()
def ansible_defaults():
    with open('playbook-vars.yml', 'r') as stream:
        return yaml.load(stream)


@pytest.mark.parametrize('package', ansible_defaults()['apt_packages'])
def test_apt_packages(host, package):
    assert host.package(package).is_installed


def test_apt_sources(host, ansible_defaults):
    if ansible_defaults['apt_remove_sources']:
        assert not host.file('/etc/apt/sources.list').exists


def test_apt_conf(host, ansible_defaults):
    if ansible_defaults['apt_remove_conf']:
        assert not host.file('/etc/apt/apt.conf').exists


def test_apt_preferences(host, ansible_defaults):
    if ansible_defaults['apt_remove_preferences']:
        assert not host.file('/etc/apt/preferences').exists


@pytest.mark.parametrize('sources', ansible_defaults()['apt_sources_default'])
def test_apt_sources_default(host, sources):
    print sources
    assert host.file(os.path.join('/etc/apt/sources.list.d',
                                  sources['name'] + ".sources")).exists


@pytest.mark.parametrize('sources', ansible_defaults()['apt_sources_custom'])
def test_apt_sources_custom(host, sources):
    print sources
    assert host.file(os.path.join('/etc/apt/sources.list.d',
                                  sources['name'] + ".sources")).exists


@pytest.mark.parametrize('apt_conf', ansible_defaults()['apt_conf_files'])
def test_apt_conf_d_files(host, apt_conf):
    assert host.file(os.path.join('/etc/apt/apt.conf.d',
                                  os.path.basename(apt_conf))).exists


@pytest.mark.parametrize('apt_preferences',
                         ansible_defaults()['apt_preferences_files'])
def test_apt_preferences_d_files(host, apt_preferences):
    assert host.file(os.path.join('/etc/apt/preferences.d',
                                  os.path.basename(apt_preferences))).exists
