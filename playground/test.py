import fptest1 as fp

print(fp.hello())
print(fp.pauli_x())
print(fp.pauli_y())
print(fp.pauli_z())

assert (fp.pauli_x() @ fp.pauli_y() == 1j * fp.pauli_z()).all()


def greet(name: str) -> str:
    return "Hello, " + name


print(greet("Einstein"))
