class Parameters:
    output = None
    """Output specified file instead of running the GUI, the file extension specifies the type: 
        stl, off, amf, 3mf, csg, dxf, svg, png, echo, ast, term, nef3, nefdbg."""

    variables = None
    """Pre-define variables"""

    preview = None
    """[=throwntogether] -for ThrownTogether preview png"""

    render = None
    """for full geometry evaluation when exporting png"""

    view = None
    """view options: axes | crosshairs | edges | scales | wireframe"""

    projection = None
    """(o)rtho or (p)erspective when exporting png"""

    csglimit = None
    """n -stop rendering at n CSG elements when exporting png"""

    colorscheme = None
    """colorscheme: *Cornfield | Metallic | Sunset | Starnight | BeforeDawn | Nature | DeepOcean 
        | Solarized | Tomorrow | Tomorrow 2 | Tomorrow Night | Monotone"""

    quiet = None
    """quiet mode (don't print anything *except* errors)"""

    hardwarnings = None
    """Stop on the first warning"""

    check_parameters = None
    """true/false, configure the parameter check for user modules and functions"""

    check_parameter_ranges = None
    """true/false, configure the parameter range check for builtin modules"""

    debug = None
    """special debug info"""

    help = None
    """Print all commands (useless here?)"""

    input_file = None
    """OpenScad file to pass to OpenScad"""

    def __init__(self):
        pass
