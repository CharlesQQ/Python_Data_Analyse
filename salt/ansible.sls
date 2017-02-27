'/etc/ansible/ansible.cfg':
  ansible.files:
    - inventory: /etc/host
    - timeout: 88
    - forks: 8