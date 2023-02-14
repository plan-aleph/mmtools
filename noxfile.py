import nox


@nox.session
def test_config_build(session):
    session.install('poetry')
    session.install('pytest')

    session.run('poetry', 'build')
    session.run('pip', 'install', 'dist/mmtools-0.1.0-py3-none-any.whl')
    session.run('pytest')
