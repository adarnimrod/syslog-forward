def test_syslog_forward(Service, SystemInfo):
    if SystemInfo.type == 'openbsd':
        assert Service('syslogd').is_running
    elif SystemInfo.type == 'linux' and SystemInfo.distribution in ['debian',
                                                                    'ubuntu']:
        assert Service('rsyslog').is_running
