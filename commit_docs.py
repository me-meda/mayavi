#!/usr/bin/env python
# encoding: utf-8
from optparse import OptionParser
import os.path
import shutil
from subprocess import Popen
import tempfile

CEC_MAYAVI_SVN = 'https://svn.enthought.com/svn/cec/trunk/projects/mayavi'

def find_stdout(options):
    if not hasattr(options, 'stdout'):
        if options.verbose:
            options.stdout = None
        else:
            options.stdout = open(os.devnull, 'w')

    return options.stdout

def debug_print(msg, options):
    if options.verbose == None:
        print msg

def build_html(options):
    debug_print('Building html', options)

    Popen('sphinx-build -b html %s %s/html/' % (options.docsrc,
        options.target), stdout=find_stdout(options), shell=True).wait()

def build_latex(options):
    debug_print('Building LaTeX', options)

    # Build the LaTeX source files (ignore cwd property)
    Popen('sphinx-build -b latex %s %s/latex/' % (options.docsrc,
        options.target), stdout=find_stdout(options), shell=True).wait()

    kwargs = {
        'cwd': '%s/latex/' % options.target,
        'shell': True,
        'stdout': find_stdout(options),
    }

    # Build LaTeX (stupidly difficult)
    for i in range(3):
        Popen('pdflatex mayavi_user_guide.tex', **kwargs).wait()

    Popen('makeindex -s python.ist mayavi_user_guide.idx', **kwargs).wait()
    Popen('makeindex -s python.ist modmayavi_user_guide.idx', **kwargs).wait()

    for i in range(2):
        Popen('pdflatex mayavi_user_guide.tex', **kwargs).wait()

    # Clean up all the non-PDF files
    for name in os.listdir(kwargs['cwd']):
        full_path = '%s/%s' % (os.path.dirname(kwargs['cwd']), name)

        if full_path[-3:] != 'pdf' and full_path[-4:] != '.svn':
            if os.path.isdir(full_path):
                shutil.rmtree(full_path)
            else:
                os.remove(full_path)

def main(options):
    # Checkout SVN to target directory
    debug_print('Using "%s" target dir' % options.target, options)

    Popen('svn co %s %s' % (CEC_MAYAVI_SVN, options.target),
        stdout=find_stdout(options), shell=True).wait()

    # Build docs
    build_html(options)
    # build_latex(options)

    # Checkin HTML to CEC SVN.
    Popen('svn add %(target)s/html/* %(target)s/latex/*' % {
            'target': options.target
        }, stdout=find_stdout(options), shell=True).wait()
    Popen('svn commit %s -m "%s"' % (options.target, options.commit_message),
        stdout=find_stdout(options), shell=True).wait()

    # Removed target directory
    shutil.rmtree(options.target)

def handle_exec():
    # Handle options
    parser = OptionParser()

    parser.add_option('-d', '--docsrc', action='store',
        default=os.path.join(os.path.abspath(os.path.dirname(__file__)),
            'docs', 'mayavi', 'user_guide', 'source'),
        help='read the documentation from the documentation source')

    parser.add_option('-m', '--commit-message', action='store',
        help='use commit message when committing to code.enthought.com\'s ' \
            'repo')

    parser.add_option('-t', '--target', action='store',
        help='place the html and latex directories in the target destination')

    parser.add_option('-v', '--verbose', action='store_true',
        help='print output of all commands which this executes [default]',)

    parser.add_option('-q', '--quiet', action='store_false', dest='verbose',
        help='suppress the output of all commands which this executes')

    parser.set_defaults(**{
        'docsrc': os.path.join(os.path.abspath(os.path.dirname(__file__)),
            'docs', 'mayavi', 'user_guide', 'source'),
        'commit_message': 'Updating docs',
        'target': tempfile.mkdtemp(),
        'verbose': False,
    })

    options, args = parser.parse_args()

    # Begin execution
    main(options)

if __name__ == '__main__':
    handle_exec()