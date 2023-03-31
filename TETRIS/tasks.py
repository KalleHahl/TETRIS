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