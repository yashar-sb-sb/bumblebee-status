import bumblebee.module
import psutil

def fmt(num, suffix='B'):
    for unit in [ "", "Ki", "Mi", "Gi" ]:
        if num < 1024.0:
            return "{:.2f}{}{}".format(num, unit, suffix)
        num /= 1024.0
    return "{:05.2f%}{}{}".format(num, "Gi", suffix)

class Module(bumblebee.module.Module):
    def __init__(self, args):
        super(Module, self).__init__(args)
        self._mem = psutil.virtual_memory()

    def data(self):
        self._mem = psutil.virtual_memory()

        free = self._mem.available
        total = self._mem.total

        return "{}/{} ({:05.02f}%)".format(fmt(self._mem.available), fmt(self._mem.total), 100.0 - self._mem.percent)

    def warning(self):
        return self._mem.percent < 20

    def critical(self):
        return self._mem.percent < 10

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
