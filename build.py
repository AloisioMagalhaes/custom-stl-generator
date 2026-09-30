import argparse,subprocess,shutil
from pathlib import Path
p=argparse.ArgumentParser()
p.add_argument("-o","--output",default="output.stl")
p.add_argument("-D",action="append",default=[])
a=p.parse_args()
e=shutil.which("openscad") or shutil.which("openscad.com")
if not e: raise SystemExit("OpenSCAD not found")
r=Path(__file__).parent
x=[e,"-o",str(r/a.output),str(r/"keychain.scad")]
for d in a.D:x[1:1]=["-D",d]
subprocess.run(x,check=True)
