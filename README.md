
# CAD Designer: 2D & 3D CAD Mini-Project


- Basic 2D CAD drawing generation (DXF)
- Basic 3D CAD model creation (STL)
- A Python script that loads, displays, and exports simple CAD geometry

## Features
### 2D CAD
- Generates a DXF file containing:
  - A rectangle
  - A circle
  - A polyline path

### 3D CAD
- Generates an ASCII STL 3D model:
  - Simple cube mesh

### Python Script (`src/main.py`)
- Loads DXF & STL
- Displays file information
- Exports new generated CAD files

## How to Run
```
pip install ezdxf numpy
python src/main.py
```

## Project Structure
```
cad_project/
 ├─ README.md
 ├─ src/
 │   └─ main.py
 └─ models/
     ├─ 2d_sample.dxf
     └─ 3d_sample.stl
```
