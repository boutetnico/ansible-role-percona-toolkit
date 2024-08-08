[![tests](https://github.com/boutetnico/ansible-role-percona-toolkit/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-percona-toolkit/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.percona_toolkit-blue.svg)](https://galaxy.ansible.com/boutetnico/percona_toolkit)

ansible-role-percona-toolkit
============================

This role installs [percona-toolkit](https://docs.percona.com/percona-toolkit/).

Requirements
------------

Ansible 2.10 or newer.

Supported Platforms
-------------------

- [Debian - 11 (Bullseye)](https://wiki.debian.org/DebianBullseye)
- [Debian - 12 (Bookworm)](https://wiki.debian.org/DebianBookworm)
- [Ubuntu - 22.04 (Jammy Jellyfish)](http://releases.ubuntu.com/22.04/)
- [Ubuntu - 24.04 (Noble Numbat)](http://releases.ubuntu.com/24.04/)

Role Variables
--------------

| Variable                        | Required | Default       | Choices   | Comments                                          |
|---------------------------------|----------|---------------|-----------|---------------------------------------------------|
| percona_toolkit_packages        | true     |               | list      | See `defaults/main.yml`.                          |
| percona_toolkit_package_version | true     | `present`     | string    | Use `latest` to update.                           |

Dependencies
------------

- [percona-release role](https://github.com/boutetnico/ansible-role-percona-release/)

Example Playbook
----------------

    - hosts: all
      roles:
        - role: ansible-role-percona-toolkit


Testing
-------

    molecule test

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
