from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_syslog_forward(Service, SystemInfo):
    if SystemInfo.type == 'openbsd':
        assert Service('syslogd').is_running
    elif SystemInfo.type == 'linux' and SystemInfo.distribution in ['debian',
                                                                    'ubuntu']:
        assert Service('rsyslog').is_running
