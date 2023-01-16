import subprocess
class Console:

    @staticmethod
    def _run_cmd(cmd):
        return subprocess.run(cmd, stdout=subprocess.PIPE).stdout
    
    @staticmethod
    def _is_cmd(cmd):
        # OS Specific Code.
        raise NotImplementedError

    @staticmethod
    def _required_cmd(cmd):
        if not (Console._is_cmd(cmd)):
            raise RuntimeError(f"Please Install {cmd} to be able to use {__name__} {__version__}")