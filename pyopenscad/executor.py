import subprocess
import shutil

from pyopenscad.parameters import Parameters


class Executor:
    def __init__(self, openscad_path=None):
        if openscad_path:
            self.openscad_path = openscad_path
        else:
            self.openscad_path = shutil.which("openscad")

    def execute(self, parameters: [Parameters]):
        cmd = self.generate_command(parameters)
        ret = subprocess.run(cmd, capture_output=True)

        if ret.returncode != 0:
            raise Exception(ret.stderr)  # TODO

        return [ret.stdout, ret.stderr]

    def generate_command(self, parameters: [Parameters]) -> [str]:
        cmd = list()
        cmd.append(self.openscad_path)

        if parameters.output:
            cmd.append("-o")
            cmd.append(parameters.output)

        if parameters.variables and len(parameters.variables) > 0:
            for var_key in parameters.variables:
                cmd.append("-D")
                cmd.append("%s=%s" % (var_key, parameters.variables[var_key]))

        if parameters.preview:
            cmd.append("--preview")
            cmd.append(str(parameters.preview))

        if parameters.render:
            cmd.append("--render")
            cmd.append(str(parameters.render))

        if parameters.view:
            cmd.append("--view")
            cmd.append(parameters.view)

        if parameters.projection:
            cmd.append("--projection")
            cmd.append(parameters.projection)

        if parameters.csglimit:
            cmd.append("--csglimit")
            cmd.append(str(parameters.csglimit))

        if parameters.colorscheme:
            cmd.append("--colorscheme")
            cmd.append(parameters.colorscheme)

        if parameters.quiet:
            cmd.append("--quiet")

        if parameters.hardwarnings:
            cmd.append("--hardwarnings")

        if parameters.check_parameters:
            cmd.append("--check-parameters")
            cmd.append(parameters.check_parameters)

        if parameters.check_parameter_ranges:
            cmd.append("--check-parameter-ranges")
            cmd.append(parameters.check_parameter_ranges)

        if parameters.debug:
            cmd.append("--debug")
            cmd.append(parameters.debug)

        if parameters.help:
            cmd.append("--help")

        if parameters.input_file:
            cmd.append(parameters.input_file)

        return cmd
