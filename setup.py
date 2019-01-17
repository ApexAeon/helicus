from cx_Freeze import setup, Executable

setup(name='jaccsdnacode',
      version='pre-alpha1.0',
      executables = [Executable('dna.py')])
