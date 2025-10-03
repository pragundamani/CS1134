import pynvim

@pynvim.plugin
class MyPlugin(object):
    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.command('MyCommand', range='', nargs='*', sync=True)
    def my_command(self, args, range):
        self.nvim.out_write('This is my custom Neovim command!\n')