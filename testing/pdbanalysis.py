"""
Calculate some properties on proteins structures.

The module provides facilities to read protein structures from PDB files and
to calculate some geometric properties.
"""

import numpy as np
import periodictable


def read_pdb_atoms(lines):
    """
    Read the coordinate and the atom names from a PDB files.

    The function expects an iterable on the lines of the PDB file (e.g. a file
    handler or a list). It returns a Nx3 array of coordinates and an array of
    atom names.

    Warning! The function is not aware of models, insertions, and alternate
    positions.
    """
    positions = []
    names = []
    for line in lines:
        if line.startswith('ATOM  '):
            x = line[30:38]
            y = line[38:46]
            z = line[46:54]
            name = line[12:16]
            positions.append([x, y, z])
            names.append(name)
    return np.array(positions, dtype=float), np.array(names)


def get_elements_from_names(names):
    """
    Build an array of element symbols from an array of atom names.

    Warning! The heuristic does not follow the PDB standard!
    """
    return np.array([name.strip()[0] for name in names])


def get_masses_from_elements(symbols):
    """
    Build an array of atom masses from an array of element symbols.

    The masses are expressed in atomic mass unit.
    """
    return np.array([
        periodictable.elements.symbol(symbol).mass
        for symbol in symbols
    ])


def compute_center_of_mass(positions, masses):
    """
    Compute the center of mass of a collection of atoms.

    The center of mass is expressed in the same unit as the provided positions.
    The positions are expected as an N by 3 array of floats with a row per atom.
    The masses are expected as an array of floats.
    """
    center = np.zeros((3,), dtype=float)
    total_mass = 0
    for atom_position, atom_mass in zip(positions, masses):
        center += atom_position * atom_mass
        total_mass += atom_mass
    center /= total_mass
    return center


def compute_euclidean_distance(position_a, position_b):
    """
    Compute the euclidean distance between two points.

    The points are expected as two arrays of shape (3, ). The distance is
    expressed in the same unit as the point positions.
    """
    return np.sqrt(
        (position_b[0] - position_a[0]) ** 2
        + (position_b[1] - position_a[1]) ** 2
        + (position_b[1] - position_a[1]) ** 2
    )


def get_carbon_alpha_index(names):
    """
    Returns the index of the carbon alpha in an array of atom names.

    The name of a carbon alpha is expected to be " CA " (mind the spaces) as
    it should be in a PDB file.
    """
    indices = []
    for index, name in enumerate(names):
        if name == ' CA ':
            indices.append(index)
    return np.array(indices)


def compute_end_to_end_distance(positions, names):
    """
    Compute the euclidean distance between the first and the last carbon alpha.
    """
    ca_indices = get_carbon_alpha_index(names)
    first_ca_position = positions[ca_indices[0]]
    last_ca_position = positions[ca_indices[-1]]
    return compute_euclidean_distance(first_ca_position, last_ca_position)


if __name__ == '__main__':
    pdb_path = '1bta.pdb'
    with open(pdb_path) as infile:
        positions, names = read_pdb_atoms(infile)
    elements = get_elements_from_names(names)
    masses = get_masses_from_elements(elements)
    center_of_mass = compute_center_of_mass(positions, masses)
    print('Center of mass:', center_of_mass)
    end_to_end_distance = compute_end_to_end_distance(positions, names)
    print('End to end distance is {:2f} Å'.format(end_to_end_distance))
