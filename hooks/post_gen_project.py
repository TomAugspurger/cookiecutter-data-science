import subprocess

module_name = '{{ cookiecutter.module_name }}'

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '.'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])
