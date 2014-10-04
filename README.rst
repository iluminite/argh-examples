Examples using Argh
===================

Argh is a great library to use in simplifying the work to create console
scripts. While the library is clear, simple, and easy to use, there are many
ways to go about creating console scripts and argh is intended to be flexible.

This repository contains various examples hacked together to test and show how
argh functions.


Usage
-----

Create a virtualenv, then install with ``python setup.py install``. You should
then see the following scripts in the venv:

.. code::

   (argh) % ls $WORKON_HOME/argh/bin/z*
   
   z zall zdump zload


The commands in action
~~~~~~~~~~~~~~~~~~~~~~

.. code::

   (argh)% z

   (argh)% z --help
   usage: z [-h] [-m]
   
   optional arguments:
     -h, --help   show this help message and exit
     -m, --myarg  Test arg. (default: True)


   (argh)% z --myarg
   my arg:  False


   (argh)% zall
   usage: zall [-h] {cmd,load,dump} ...
   zall: error: too few arguments

   (argh)% zall --help
   usage: zall [-h] {cmd,load,dump} ...
   
   positional arguments:
     {cmd,load,dump}
       cmd
       load
       dump
   
   optional arguments:
     -h, --help       show this help message and exit


   (argh)% zall load --help
   usage: zall load [-h] [-m]
   
   optional arguments:
     -h, --help   show this help message and exit
     -m, --myarg  Test arg. (default: True)


   (argh)% zall load --myarg
   loading:  False
   

   (argh)% zload --help
   usage: zload [-h] [-m]
   
   optional arguments:
     -h, --help   show this help message and exit
     -m, --myarg  Test arg. (default: True)
   (argh)% zload --myarg
   loading:  False

