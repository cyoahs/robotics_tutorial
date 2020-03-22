import xml.etree.ElementTree as ET

robot = ET.Element('robot')
robot.set('name', 'forest')

inertiaKey = ['ixx', 'ixy', 'ixz', 'iyy', 'iyz', 'izz']

# add a material
name = 'grey'
rgba = []
def addMaterial(parent, name, rgba):
    material = ET.SubElement(parent, 'material')
    material.set('name', name)
    color = ET.SubElement(material, 'color')
    color.set('rbga', f'{rgba[0]} {rgba[1]} {rgba[2]} {rgba[3]}')

# add a base
name = 'base'
massValue = 0.0
inertiaValue = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
def addLink(name, massValue, inertiaValue, size=None, materialName=None):
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
        size = [1.0, 1.0, 4.0]
        visual = ET.SubElement(link, 'visual')
        ET.SubElement(visual, 'matertial', attrib={'name': materialName})
        geometry = ET.SubElement(visual, 'geometry')
        ET.SubElement(geometry, 'box', attrib={'size': f'{size[0]} {size[1]} {size[2]}'})

        collision = ET.SubElement(link, 'collision')
        geometry = ET.SubElement(collision, 'geometry')
        ET.SubElement(geometry, 'box', attrib={'size': f'{size[0]} {size[1]} {size[2]}'})

# add joint
def addFixedJoint(root, parent, child, xyz, rpy):
    joint = ET.SubElement(root, 'joint', attrib={'name': f'{parent}_to_{child}', 'type': 'fixed'})
    ET.SubElement(joint, 'origin', attrib={'xyz': f'{xyz[0]} {xyz[1]} {xyz[2]}', 'rpy': f'{rpy[0]} {rpy[1]} {rpy[2]}'})
    ET.SubElement(joint, 'parent', attrib={'link': parent})
    ET.SubElement(joint, 'child', attrib={'link': child})