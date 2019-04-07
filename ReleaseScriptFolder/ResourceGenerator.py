import os
import shutil

def _setup(path):
    resouceFolder = os.path.join(path, "GeneratedResources")
    if os.path.isdir(resouceFolder):
       shutil.rmtree(resouceFolder)
    os.makedirs(resouceFolder)
    f = open(os.path.join(path, "GeneratedResources", "__init__.py"), "w")
    f.close()


def _setup_replacer(name, size, baseValue):
    return {"""{fixed_name}""": str(name), """{name}""": str(name), """{size}""": str(size), """{baseValue}""": str(baseValue)}


def _fix_template(line, replacer):
    r = line
    for k, v in replacer.items():
        r = r.replace(k, v)
    return r

def _generate_resource(path, template, name, size, baseValue):
    filename = "%s.py" % name
    f = open(os.path.join(path, "GeneratedResources", filename), "w")
    replacer = _setup_replacer(name, size, baseValue)
    for line in template:
        f.write(_fix_template(line, replacer))
    f.close()


def generate_resouces(path):
    _setup(path)
    f = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "ResouceTemplate.txt"))
    template = f.readlines()
    f.close()
    _generate_resource(path, template, "Banana", 1, 0.1)
    _generate_resource(path, template, "Iron", 15, 1)
    _generate_resource(path, template, "Steel", 100, 10)