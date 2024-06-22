#!/usr/bin/env python3

import argparse
from subprocess import run
from jinja2 import Environment, FileSystemLoader
from re import search
from os import mkdir, chdir
from shutil import copy, rmtree

def parse_args():
    parser = argparse.ArgumentParser(description='Configure a new Cmake project')
    parser.add_argument('project', help='Name of the project to build')
    parser.add_argument('--cxxstd', default='20', help='C++ standard to build for. Default=20')
    parser.add_argument('--reset', action="store_true", default=False, help='Delete the existing project of the same name and reset to the original template')
    parser.add_argument('--build', action="store_true", default=False, help='Build the project using Ninja')
    return parser.parse_args()

def make_directory(folder):
    try:
        mkdir(folder)
    except:
        print("ERROR: Project already exists")
        print("Rerun with --reset to reset project to default template")
        exit(1)


class Ezmake:
    def __init__(self, args):
        self.project = args.project
        self.cxxstd = args.cxxstd
        self.reset = args.reset
        self.build = args.build
        self.PROJECT_DIR = self.project + '/'
        self.SRC_DIR = self.PROJECT_DIR + "src/"
        self.INC_DIR = self.PROJECT_DIR + "inc/"
        self.BUILD_DIR = self.PROJECT_DIR + "build/"
        self.TEMPLATES = '/opt/ezmake/templates/'

    def generate_cmakelists(self):
        environment = Environment(loader=FileSystemLoader(self.TEMPLATES))
        template = environment.get_template("CMakeLists.txt.tmpl")
        cmake_version = run(['cmake', '--version'], capture_output=True).stdout.decode('utf-8')
        cmake_version = search('[0-9]+\.[0-9]+\.[0-9]+', cmake_version).group()
        return template.render(cmake_version=cmake_version, project=self.project, cxx_standard=self.cxxstd).strip()
    
    def create_directories(self):
        make_directory(self.PROJECT_DIR)
        make_directory(self.SRC_DIR)
        make_directory(self.INC_DIR)
        make_directory(self.BUILD_DIR)

    def reset_project(self):
        rmtree(self.PROJECT_DIR)

    def populate_project(self, content):
        with open(self.PROJECT_DIR + "CMakeLists.txt", "w") as f:
            f.write(content)
        copy(self.TEMPLATES + "main.cpp", self.SRC_DIR)
        copy(self.TEMPLATES + "test.hpp", self.INC_DIR)

    def build_project(self):
        chdir(self.BUILD_DIR)
        run(['cmake', '..', '-G', 'Ninja'])
        run(['ninja'])

    def generate(self):
        if self.reset:
            self.reset_project()
        self.create_directories()
        self.populate_project(self.generate_cmakelists())
        if self.build:
            self.build_project()

def main():
    args = parse_args()
    ezmake = Ezmake(args)
    ezmake.generate()


if __name__ == '__main__':
    main()
