import nox


@nox.session
def test_config_build(session):
    session.install('-r', 'requirements.txt')
    