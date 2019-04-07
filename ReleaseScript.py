def releaseScript():
    import os
    import ReleaseScriptFolder.ResourceGenerator
    ReleaseScriptFolder.ResourceGenerator.generate_resouces(os.path.dirname(os.path.realpath(__file__)))
