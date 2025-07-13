def test_hostname():
    import subprocess
    result = subprocess.run(['hostname'], capture_output=True, text=True)
    hostname = result.stdout.strip()
    print(f"[DEBUG] Hostname is: '{hostname}'")
    assert hostname != '', "Hostname should not be empty"
