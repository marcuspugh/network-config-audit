from pathlib import Path

REQUIRED_CONFIGS = {
    "Hostname": "host-name",
    "SSH Enabled": "ssh;",
    "NTP Server": "ntp",
    "Syslog": "syslog",
    "SNMP": "snmp",
}


def audit_config(file_path):
    print(f"\nAuditing: {file_path}")
    print("-" * 50)

    try:
        config = Path(file_path).read_text()

        passed = 0
        failed = 0

        for check_name, required_text in REQUIRED_CONFIGS.items():
            if required_text in config:
                print(f"[PASS] {check_name}")
                passed += 1
            else:
                print(f"[FAIL] {check_name}")
                failed += 1

        print("-" * 50)
        print(f"Passed: {passed}")
        print(f"Failed: {failed}")

    except FileNotFoundError:
        print(f"ERROR: File not found -> {file_path}")


if __name__ == "__main__":
    config_file = input("Enter config file path: ")
    audit_config(config_file)