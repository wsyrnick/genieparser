expected_output = {
        "entries": {
            1: {
                "timestamp": "Wed Jul 21 20:31:23.000",
                "vlan": 1,
                "interface": "Et0/1",
                "mac": "aabb.cc00.0300",
                "protocol": "ARP::REP",
                "ip": "192.168.23.3",
                "ignored": False,
            },
            2: {
                "timestamp": "Wed Jul 21 20:31:23.000",
                "vlan": 1006,
                "interface": "Et0/1",
                "mac": "aabb.cc00.0300",
                "protocol": "ARP::REP",
                "ip": "192.168.23.3",
                "ignored": False,
            },
            3: {
                "timestamp": "Wed Jul 21 20:31:25.000",
                "vlan": 1006,
                "interface": "Et0/1",
                "mac": "aabb.cc00.0300",
                "protocol": "ARP::REP",
                "ip": "192.168.23.3",
                "ignored": True,
            },
            4: {
                "timestamp": "Wed Jul 21 20:31:26.000",
                "vlan": 10,
                "interface": "Et0/0",
                "protocol": "NDP::NS",
                "ip": "FE80::A8BB:CCFF:FE00:100",
                "ignored": False,
            },
            5: {
                "timestamp": "Wed Jul 21 20:31:27.000",
                "vlan": 10,
                "interface": "Et0/0",
                "mac": "aabb.cc00.0100",
                "protocol": "NDP::NA",
                "ip": "FE80::A8BB:CCFF:FE00:100",
                "ignored": False,
                "drop_reason": "Packet accepted but not forwarded",
            },
            6: {
                "timestamp": "Wed Jul 21 20:31:27.000",
                "vlan": 10,
                "interface": "Et0/0",
                "protocol": "NDP::NS",
                "ip": "A::1",
                "ignored": False,
            },
            7: {
                "timestamp": "Wed Jul 21 20:31:27.000",
                "vlan": 10,
                "interface": "Et0/0",
                "mac": "aabb.cc00.0100",
                "protocol": "NDP::RA",
                "ip": "FE80::A8BB:CCFF:FE00:100",
                "ignored": False,
                "drop_reason": "Packet not authorized on port",
            },
            8: {
                "timestamp": "Wed Jul 21 20:31:28.000",
                "vlan": 10,
                "interface": "Et0/0",
                "mac": "aabb.cc00.0100",
                "protocol": "NDP::NA",
                "ip": "A::1",
                "ignored": False,
                "drop_reason": "Packet accepted but not forwarded"
            }
        }
    }