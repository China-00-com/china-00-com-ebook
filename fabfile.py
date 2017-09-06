# coding:utf-8
from fabric.api import env, roles, run, cd

env.parallel = True
env.use_ssh_config = True
env.roledefs = {
    'aws': ['tacey-aws']
}


@roles("aws")
def pre_deploy():
    run("ls")
    print("Executing on %s as %s" % (env.host, env.user))
