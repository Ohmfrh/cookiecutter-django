#!/bin/bash
(ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook ./deploy/deploy.yml \
    -u {{cookiecutter.remote_server_username}} \
    -i ./deployment_hosts \
    --private-key={{cookiecutter.server_connection_key_path}})
