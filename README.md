# odoo

[![Build Status](https://img.shields.io/travis/infOpen/ansible-role-odoo/master.svg?label=travis_master)](https://travis-ci.org/infOpen/ansible-role-odoo)
[![Build Status](https://img.shields.io/travis/infOpen/ansible-role-odoo/develop.svg?label=travis_develop)](https://travis-ci.org/infOpen/ansible-role-odoo)
[![Updates](https://pyup.io/repos/github/infOpen/ansible-role-odoo/shield.svg)](https://pyup.io/repos/github/infOpen/ansible-role-odoo/)
[![Python 3](https://pyup.io/repos/github/infOpen/ansible-role-odoo/python-3-shield.svg)](https://pyup.io/repos/github/infOpen/ansible-role-odoo/)
[![Ansible Role](https://img.shields.io/ansible/role/17841.svg)](https://galaxy.ansible.com/infOpen/odoo/)

Install odoo package.

## Requirements

This role requires Ansible 2.1 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Locally, you can run tests on Docker (default driver) or Vagrant.
Travis run tests using Docker driver only.

Currently, tests are done on:
- Debian Jessie
- Ubuntu Xenial

and use:
- Ansible 2.1.x
- Ansible 2.2.x
- Ansible 2.3.x

### Running tests

#### Using Docker driver

```
$ tox
```

#### Using Vagrant driver

```
$ MOLECULE_DRIVER=vagrant tox
```

## Role Variables

### Default role variables

``` yaml
# Defaults vars file for odoo role

# Packages management
odoo_packages: "{{ _odoo_packages }}"
odoo_package_wkhtmltox: "{{ _odoo_package_wkhtmltox | default({}) }}"
odoo_repositories: "{{ _odoo_repositories }}"
odoo_repositories_keys: "{{ _odoo_repositories_keys }}"
odoo_repository_cache_valid_time: 3600
odoo_system_prerequisites: "{{ _odoo_system_prerequisites }}"

# Service management
odoo_service: "{{ _odoo_service }}"

# General
odoo_version: '10.0'

# Configuration
odoo_config_file_name: "{{
  odoo_version
  | version_compare('10.0', '<')
  | ternary('openerp-server.conf', 'odoo.conf') }}"
odoo_config_file_path: "{{ _odoo_config_file_path }}"
odoo_config_options: []
```

### Debian OS family variables

``` yaml
# Packages management
_odoo_packages:
  - name: 'odoo'
_odoo_repositories:
  - repo: "deb http://nightly.odoo.com/{{ odoo_version }}/nightly/deb/ ./"
_odoo_repositories_keys:
  - url: 'https://nightly.odoo.com/odoo.key'
_odoo_system_prerequisites:
  - name: 'ca-certificates'

# Service management
_odoo_service:
  name: 'odoo'

# Configuration
_odoo_config_file_path: "/etc/odoo/{{ odoo_config_file_name }}"
```

### Ubuntu distributions variables

``` yaml
# Ubuntu distributions specific vars
_odoo_packages:
  - name: 'odoo'
  - name: 'wkhtmltopdf'
```

### Debian Jessie specific variables

``` yaml
_odoo_package_wkhtmltox:
  url: 'https://nightly.odoo.com/extra/wkhtmltox-0.12.1.2_linux-jessie-amd64.deb'
```

## Dependencies

None

## Example Playbook

``` yaml
- hosts: servers
  roles:
    - { role: infOpen.odoo }
```

## License

MIT

## Author Information

Alexandre Chaussier (for Infopen company)
- http://www.infopen.pro
- a.chaussier [at] infopen.pro
