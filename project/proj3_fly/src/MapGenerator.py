# import xml.etree.ElementTree as ET
from lxml import etree as ET
import Helper

inertiaKey = ['ixx', 'ixy', 'ixz', 'iyy', 'iyz', 'izz']


# add a material
def addMaterial(parent, name, rgba):
    material = ET.SubElement(parent, 'material')
    material.set('name', name)
    color = ET.SubElement(material, 'color')
    color.set('rbga', f'{rgba[0]} {rgba[1]} {rgba[2]} {rgba[3]}')


def addLink(name, root, massValue, inertiaValue, size=None, materialName=None):
    # add link
    link = ET.SubElement(robot, 'link')
    link.set('name', name)

    # add inertia
    inertial = ET.SubElement(link, 'inertial')
    mass = ET.SubElement(inertial, 'mass')
    mass.set('value', f'{massValue}')
    inertia = ET.SubElement(inertial, 'inertia')
    for i in range(6):
        inertia.set(inertiaKey[i], f'{inertiaValue[i]}')

    # add visual and collision
    if size is not None:
        visual = ET.SubElement(link, 'visual')
        ET.SubElement(visual, 'matertial', attrib={'name': materialName})
        geometry = ET.SubElement(visual, 'geometry')
        ET.SubElement(geometry, 'box', attrib={'size': f'{size[0]} {size[1]} {size[2]}'})

        collision = ET.SubElement(link, 'collision')
        geometry = ET.SubElement(collision, 'geometry')
        ET.SubElement(geometry, 'box', attrib={'size': f'{size[0]} {size[1]} {size[2]}'})
    
    return link


# add joint
def addFixedJoint(root, parent, child, xyz, rpy):
    joint = ET.SubElement(root, 'joint', attrib={'name': f'{parent}_to_{child}', 'type': 'fixed'})
    ET.SubElement(joint, 'origin', attrib={'xyz': f'{xyz[0]} {xyz[1]} {xyz[2]}', 'rpy': f'{rpy[0]} {rpy[1]} {rpy[2]}'})
    ET.SubElement(joint, 'parent', attrib={'link': parent})
    ET.SubElement(joint, 'child', attrib={'link': child})


def addObstacle(name, size, root, parent, pos, rot, materialName='grey'):
    addLink(name, root, massValue=1.0, inertiaValue=[1.0, 0.0, 0.0, 1.0, 0.0, 1.0], size=size, materialName=materialName)
    addFixedJoint(root, parent, name, pos, rot)


if __name__ == "__main__":
    robot = ET.Element('robot')
    robot.set('name', 'forest')
    
    materialName = 'gray'
    rgba = [0.3, 0.3, 0.3, 1.0]
    addMaterial(robot, materialName, rgba)
    
    materialName = 'gold'
    rgba = [0.0, 0.8, 0.0, 1.0]
    addMaterial(robot, materialName, rgba)

    materialName = 'deep'
    rgba = [0.0, 0.9, 0.9, 1.0]
    addMaterial(robot, materialName, rgba)

    # add a base
    name = 'base'
    massValue = 0.0
    inertiaValue = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    base = addLink(name, robot, massValue, inertiaValue)

    pos_ = []
    size_ = []
    rot_ = []
    material_ = []

    pos_.append([-11, 0.9, -7])
    size_.append([2, 2, 2])

    pos_.append([-11, 0.9, 3])
    size_.append([2, 2, 10])

    pos_.append([-5, 0.9, -4])
    size_.append([2, 2, 8])

    pos_.append([-5, 0.9, 5])
    size_.append([2, 2, 6])

    pos_.append([-1, 0.9, 6])
    size_.append([2, 2, 4])

    pos_.append([1, 0.9, -3])
    size_.append([2, 2, 6])

    pos_.append([7, 0.9, -2])
    size_.append([2, 2, 12])

    pos_.append([7, 0.9, 7])
    size_.append([2, 2, 2])

    pos_.append([11, 0.9, 6])
    size_.append([2, 2, 4])

    pos_.append([11, 0.9, -1.25])
    size_.append([2, 2, 9.5])

    for i in range(len(size_)):
        rot_.append([0, 0, 0])
        material_.append('gray')
    
    # golden box
    gap = 0.6
    length = 1.5*2**0.5 - gap/2
    size_.append([length, 2, length])
    size_.append([length, 2, length])
    rot_.append([0, 1.57/2, 0])
    rot_.append([0, 1.57/2, 0])
    material_.append('gold')
    material_.append('gold')
    pos_.append([-1, 0.9, 4-length/2**0.5])
    pos_.append([1, 0.9, 0+length/2**0.5])

    # upper and lower boundary
    size_.append([40, 2, 2])
    size_.append([40, 2, 2])
    rot_.append([0, 0, 0])
    rot_.append([0, 0, 0])
    material_.append('deep')
    material_.append('deep')
    pos_.append([0, 0.9, -9])
    pos_.append([0, 0.9, 9])

    for i in range(len(size_)):
        addObstacle(f'obstacle_{i}', size_[i], robot, parent='base', pos=pos_[i], rot=rot_[i], materialName=material_[i])

    tree = ET.ElementTree(robot)
    tree.write(Helper.findURDF('forest.urdf'), pretty_print=True, encoding='utf-8')
