from molmass import Formula


def submass(data):
    return Formula(data).composition()

