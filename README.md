[![Build Status](https://travis-ci.org/CSC-IT-Center-for-Science/ansible-role-pxe_bootstrap.svg?branch=master)](https://travis-ci.org/CSC-IT-Center-for-Science/ansible-role-pxe_bootstrap)

ansible-role-pxe_bootstrap
=========

Sets up a PXE system for reinstalling nodes

Related roles:

 - https://github.com/CSC-IT-Center-for-Science/ansible-role-pxe_config
 - https://github.com/CSC-IT-Center-for-Science/ansible-role-dhcp_server

Requirements
------------


Role Variables
--------------

see defaults/main.yml

Dependencies
------------


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: ansible-role-pxe_bootstrap }

License
-------

MIT

Author Information
------------------

