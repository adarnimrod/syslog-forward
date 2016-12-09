def test_syslog_forward(Service, SystemInfo):
    if SystemInfo.type == 'openbsd':
        assert Service('syslogd').is_running
    if SystemInfo.type == 'linux' and SystemInfo.distribution == 'debian'
        assert Service('rsyslog').is_running
