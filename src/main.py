
import ezdxf
import numpy as np

def create_2d_dxf(out_path):
    doc = ezdxf.new(dxfversion="R2010")
    msp = doc.modelspace()
    msp.add_line((0,0), (100,0))
    msp.add_line((100,0), (100,50))
    msp.add_line((100,50), (0,50))
    msp.add_line((0,50), (0,0))
    msp.add_circle((50,25), 15)
    msp.add_lwpolyline([(0,0),(20,40),(40,20),(60,60)])
    doc.saveas(out_path)
    print("Generated 2D DXF:", out_path)

def create_3d_stl(out_path):
    cube = [
        "solid cube",
        "facet normal 0 0 0",
        "outer loop",
        "vertex 0 0 0",
        "vertex 1 0 0",
        "vertex 1 1 0",
        "endloop",
        "endfacet",
        "facet normal 0 0 0",
        "outer loop",
        "vertex 0 0 0",
        "vertex 1 1 0",
        "vertex 0 1 0",
        "endloop",
        "endfacet",
        "endsolid cube"
    ]
    with open(out_path, "w") as f:
        f.write("\n".join(cube))
    print("Generated 3D STL:", out_path)

if __name__ == "__main__":
    create_2d_dxf("../models/2d_generated.dxf")
    create_3d_stl("../models/3d_generated.stl")
