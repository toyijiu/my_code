#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""Usage:
  pip-grep [-s] <reqfile> <package>...
Options:
  -h --help     Show this screen.
"""
import os
from docopt import docopt
from pip.req import parse_requirements
from pip.index import PackageFinder
from pip._vendor.requests import session

results = session()

class Requirements(object):
    def __init__(self,reqfile=None):
        super(Requirements,self).__init__()
        self.path = reqfile
        self.requirements = []

        if reqfile:
            self.load(reqfile)
        
    def __repr__(self):
        return '<Requirements \'{}\'>'.format(self.path)

    def load(self,reqfile):
        if not os.path.exists(reqfile):
            raise ValueError('The given requirements file does not exist.')

        finder = PackageFinder([],[],session=requests)
        for requirement in parse_requirements(reqfile,finder=finder,session=requests):
            if requirement.req:
                if not getattr(requirement.req,'name',None):
                    requirement.req.name = requirement.req.project_name
                self.requirements.append(requirement.req)

def grep(reqfile, packages, silent=False):
    #新建Requirements对象并解析req.name
    try:
        r = Requirements(reqfile)
    except ValueError:
        if not silent:
            print('There was a problem loading the given requirement file.')
        exit(os.EX_NOINPUT)

    #轮询requirements并判断各自的name是否在入参package中，是的话则找到了
    for req in r.requirements:
        if req.name in packages:
            if not silent:
                print('Package {} found!'.format(req.name))
            exit(0)

    if not silent:
        print('Not found.')

    exit(1)


def main():
    #docopt解析命令行指令
    args = docopt(__doc__, version='pip-grep')

    kwargs = {'reqfile': args['<reqfile>'], 'packages': args['<package>'], 'silent': args['-s']}

    grep(**kwargs)


if __name__ == '__main__':
    main()