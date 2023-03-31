from invoke import task

@task
def start(ctx):
    ctx.run('python3 src/index.py', pty=True)

@task
def format(ctx):
    ctx.run('autopep8 --in-place --recursive src')

@task
def pylint(ctx):
    ctx.run('pylint src')

@task
def pytest(ctx):
    ctx.run('pytest src')

@task
def coverage(ctx):
    ctx.run('coverage run --branch -m pytest', pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run('coverage report -m',pty=True)
    ctx.run('coverage html', pty=True)

@task
def coverage_show(ctx):
    ctx.run("open htmlcov/index.html")