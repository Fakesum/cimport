from .base import Console

class ConsoleWindow(Console):
    def is_cmd(self, cmd):
        """
            is_cmd implementation for windows
        """
        return self.run_cmd([cmd, "&&", 'echo "Command Exists"']) == "Command Exists"