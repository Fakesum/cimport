from .base import Console

class ConsoleWindow(Console):
    @staticmethod
    def is_cmd(cmd):
        """
            is_cmd implementation for windows
        """
        return ConsoleWindow.run_cmd([cmd, "&&", 'echo "Command Exists"']) == "Command Exists"