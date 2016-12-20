from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_syslog_forward_service(Service, SystemInfo):
    if SystemInfo.type == 'openbsd':
        assert Service('syslogd').is_running
    elif SystemInfo.type == 'linux' and SystemInfo.distribution in ['debian',
                                                                    'ubuntu']:
        assert Service('rsyslog').is_running


def test_syslog_forwarding_syntax(SystemInfo, Command, Sudo):
    if SystemInfo.type == 'linux' and SystemInfo.distribution in ['debian',
                                                                  'ubuntu']:
        with Sudo():
            command = Command('rsyslogd -N1')
        assert command.rc == 0
        assert 'End of config validation run' in command.stderr
