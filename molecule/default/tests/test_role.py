import pytest


def test_percona_toolkit_package_installed(host):
    package = host.package("percona-toolkit")
    assert package.is_installed


@pytest.mark.parametrize(
    "tool",
    [
        "pt-align",
        "pt-archiver",
        "pt-config-diff",
        "pt-diskstats",
        "pt-duplicate-key-checker",
        "pt-fifo-split",
        "pt-find",
        "pt-fingerprint",
        "pt-fk-error-logger",
        "pt-heartbeat",
        "pt-index-usage",
        "pt-kill",
        "pt-mext",
        "pt-mysql-summary",
        "pt-online-schema-change",
        "pt-query-digest",
        "pt-show-grants",
        "pt-slave-delay",
        "pt-slave-find",
        "pt-slave-restart",
        "pt-table-checksum",
        "pt-table-sync",
        "pt-upgrade",
        "pt-variable-advisor",
        "pt-visual-explain",
    ],
)
def test_percona_toolkit_tools_exist(host, tool):
    """Test that Percona Toolkit tools are installed and executable."""
    cmd = host.run(f"which {tool}")
    assert cmd.rc == 0
    f = host.file(cmd.stdout.strip())
    assert f.exists
    assert f.is_file
    assert f.mode & 0o111  # Check executable bit


def test_pt_online_schema_change_version(host):
    """Test that pt-online-schema-change can be executed."""
    cmd = host.run("pt-online-schema-change --version")
    assert cmd.rc == 0
    assert "pt-online-schema-change" in cmd.stdout


def test_pt_query_digest_version(host):
    """Test that pt-query-digest can be executed."""
    cmd = host.run("pt-query-digest --version")
    assert cmd.rc == 0
    assert "pt-query-digest" in cmd.stdout


def test_pt_table_checksum_version(host):
    """Test that pt-table-checksum can be executed."""
    cmd = host.run("pt-table-checksum --version")
    assert cmd.rc == 0
    assert "pt-table-checksum" in cmd.stdout
