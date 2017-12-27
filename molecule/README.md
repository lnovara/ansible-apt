Testing with molecule
=====================

This role uses [molecule](https://molecule.readthedocs.io/en/latest/) to
implement automatic testing of its functionalities.

Requirements
------------

* Ansible >= 2.4
* molecule v2
* docker

Execute the tests
-----------------

```bash
git clone https://github.com/lnovara/ansible-apt.git

cd ansible-apt

# test all the scenarios
molecule test --all
```
