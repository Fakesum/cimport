import subprocess
import os

from .. import __version__, __name__

# a Console class
# with command util
# function
class Console:

    def run_cmd(self, cmd):
        """
            Run a Command and return the consoles output
        """
        return subprocess.run(cmd, stdout=subprocess.PIPE).stdout
    
    def is_cmd(self, cmd):
        """
            This function differs for windows and linux
            and is to be defined by inherited calss.
        """
        raise NotImplementedError
    
    def required_cmd(self, cmd):
        """
            Check and raise error if comamnd
            does not exists in console.
        """
        if not (self.is_cmd(cmd)):
            raise RuntimeError(f"Please Install {cmd} to be able to use {__name__} {__version__}")
    
    def require_file(self, filename):
        """
            raise Error if file does not exist
        """
        if not os.path.exists(filename):
            raise RuntimeError(f"File {filename} does not exist")