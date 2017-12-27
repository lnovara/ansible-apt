Ansible Role: apt
=========

[![Build Status](https://travis-ci.org/lnovara/ansible-apt.svg?branch=master)](https://travis-ci.org/lnovara/ansible-apt)

Setup APT repositories, configuration snippets and pinning.

Requirements
------------

None.

Role Variables
--------------

Available variables are listed below, along with default values (see
defaults/main.yml).

    apt_packages: [apt-transport-https]

Packages to install to provide additional functionalities.

    apt_remove_sources: yes

Remove /etc/apt/sources.list file. On a newly installed Debian system this file
contains only the official Debian repositories. This file can be safely removed
as this role reinstalls these sources under /etc/apt/sources.d.

    apt_remove_sources_d: no

Remove every file under /etc/apt/sources.list.d before adding any new
repository. This can be dangerous when you already have third party repositories
configured. Set this variable to yes only if you want this role to handle
everithing in /etc/apt/sources.list.d.

    apt_remove_conf: yes

Remove /etc/apt/apt.conf. On newly installed Debian system this file does not
exist, everithing is configured under /etc/apt/apt.conf.d.

    apt_remove_conf_d: no

Remove every file under /etc/apt/apt.conf.d before adding new configuration
snipptes . On newly installed Debian system everything is configured through
files under /etc/apt/apt.conf.d so removing them can be dangerous. Set this
variable to yes ony if you want to this role to handle everything in
/etc/apt/apt.conf.d.

    apt_remove_preferences: yes

Remove /etc/apt/preferences. On newly installed Debian system this file does not
exist.

    apt_remove_preferences_d: no

Remove every file under /etc/apt/preferences.d before adding new pinning
preferences. This can be dangerous when you already have third party
repositories preferences configured. Set this variable to yes only if you want
this role to handle everything in /etc/apt/preferences.d.

    apt_sources_default:
      - name: debian
        uri: https://deb.debian.org/debian
        suites:
          - "{{ ansible_distribution_release | lower }}"
        components:
          - main
        options: {}
        src: yes
        gpg_fingerprint: null
        gpg_keyserver: null
        gpg_url: null
      - name: debian-security
        uri: https://deb.debian.org/debian-security
        suites:
          - "{{ ansible_distribution_release | lower }}/updates"
        components:
          - main
        options: {}
        src: yes
        gpg_fingerprint: null
        gpg_keyserver: null
        gpg_url: null

    apt_sources_custom: []

List of default and user-defined repositories (merged at runtime).
Dictionary fields's semantics:
* `name`: repository name.

  File ``/etc/apt/sources.list.d/{{ name }}.sources`` will be created containing
  the repository definition.
* `uri`: repository URI.
* `suites`: repository suites list (*e.g.* stretch, stable).
* `components`: repository components list (*e.g.* main, contrib, non-free).
* `options`: repository options dict (*e.g.* ``Arch: amd64``).
* `src`: whether or not to include the corrisponding source repository.
* `gpg_fingerprint`: fingerprint of the key used to authenticate the repository.

  File ``/usr/share/keyrings/{{ name }}.gpg`` will be created containing the
  repository key.

  File ``/etc/apt/preferences.d/{{ name }}`` will be created containing the
  repository pinning preferences.
* `gpg_keyserver`: keyserver address to retrieve the key.
* `gpg_url`: URL to retrieve the key.

  Note that `gpg_keyserver` has precedence over ``gpg_url`` if both are defined.

[//]: # (This comment is useful only to and a list.)

    apt_conf_files: []

List of files to add under /etc/apt/apt.conf.d.

    apt_preferences_files: []

List of files to add under /etc/apt/preferences.d.


Dependencies
------------

None.

Example Playbook
----------------

    - name: Setup APT on all hosts.
      hosts: all
      roles:
        - { role: lnovara.apt }

License
-------

MIT

Author Information
------------------

Luca Novara
