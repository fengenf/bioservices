from bioservices import chemspider
from settings import DEBUG




def test_chemspider():
    if DEBUG is not True:
        return
    s = chemspider.ChemSpider()
    assert s.find("Pyridine") == [1020]
    s.GetExtendedCompoundInfo(1020)
    s.mol(1020)
    s.mol3d(1020)
    s.image(1020)
    s.ImagesHandler(1020)
    s.databases
