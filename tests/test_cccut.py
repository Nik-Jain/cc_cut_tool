import subprocess

def test_version():
    result = subprocess.run(['cccut', '--version'], capture_output=True, text=True)
    assert "cccut v0.1.0" in result.stdout
    result = subprocess.run(['cccut', '-v'], capture_output=True, text=True)
    assert "cccut v0.1.0" in result.stdout


