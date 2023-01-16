import subprocess

from .. import __version__, __name__

# a Console class
# with command util
# function
class Console:

    @staticmethod
    def run_cmd(cmd):
        """
            Run a Command and return the consoles output
        """
        return subprocess.run(cmd, stdout=subprocess.PIPE).stdout
    
    @staticmethod
    def is_cmd(cmd):
        """
            Return if command exists in console
        """
        raise NotImplementedError

    @staticmethod
    def _required_cmd(cmd):
        """
            Check and raise error if comamnd
            does not exists in console.
        """
        if not (Console.is_cmd(cmd)):
            raise RuntimeError(f"Please Install {cmd} to be able to use {__name__} {__version__}")