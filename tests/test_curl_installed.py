def test_curl_installed():
    import subprocess
    result = subprocess.run(['which', 'curl'], capture_output=True, text=True)
    # I'm checking this just for dev env
    print(f"[DEBUG] 'which curl' returned: {result.stdout.strip()} (code {result.returncode})")
    assert result.returncode == 0, "curl should be installed"
