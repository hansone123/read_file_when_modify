from io import StringIO
import subprocess

# p = subprocess.Popen('python print.py', stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=True)
# for line in iter(p.stdout.getline, ''):
#     print(line)
# p.wait()

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=0, shell=True, universal_newlines=True,close_fds=True)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())
    
    rc = process.wait()
    return rc


r = run_command('python -u print.py')
print('result %d' % r)