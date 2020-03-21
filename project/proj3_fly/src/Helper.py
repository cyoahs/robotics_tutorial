import os


def findURDF(fileName):
    cwd = os.path.split(os.getcwd())
    if cwd[-1] == 'robotics_tutorials':
        relativePath = os.path.join('project', 'proj3_fly', 'rsc', fileName)
    elif cwd[-1] == 'project' and os.path.split(cwd[-2])[-1] == 'robotics_tutorials':
        relativePath = os.path.join('proj3_fly', 'rsc', fileName)
    elif cwd[-1] == 'proj3_fly' and os.path.split(cwd[-2])[-1] == 'project':
        relativePath = os.path.join('rsc', fileName)
    elif cwd[-1] == 'src' and os.path.split(cwd[-2])[-1] == 'proj3_fly':
        relativePath = os.path.join('..', 'rsc', fileName)
    else:
        raise RuntimeError('Please run the file in proper folder')

    return relativePath


def findLog(fileName):
    cwd = os.path.split(os.getcwd())
    if cwd[-1] == 'robotics_tutorials':
        relativePath = os.path.join('project', 'proj3_fly', 'log', fileName)
    elif cwd[-1] == 'project' and os.path.split(cwd[-2])[-1] == 'robotics_tutorials':
        relativePath = os.path.join('proj3_fly', 'log', fileName)
    elif cwd[-1] == 'proj3_fly' and os.path.split(cwd[-2])[-1] == 'project':
        relativePath = os.path.join('log', fileName)
    elif cwd[-1] == 'src' and os.path.split(cwd[-2])[-1] == 'proj3_fly':
        relativePath = os.path.join('..', 'log', fileName)
    else:
        raise RuntimeError('Please run the file in proper folder')

    return relativePath