def test_ssh_service_running():
    import subprocess
    result = subprocess.run(['systemctl', 'is-active', 'ssh'], capture_output=True, text=True)
    output = result.stdout.strip()
    print(f"[DEBUG] SSH service status: {output}")
    assert output == 'active', "SSH service should be active"
