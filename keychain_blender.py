import bpy,sys,os

L1="Good"
L2=""
L3=""
F1=os.path.join(os.path.dirname(__file__),'fonts','DynaPuff_Condensed-Bold.ttf')
F2=r"C:\Users\educa\AppData\Local\Microsoft\Windows\Fonts\BagelFatOne-Regular.ttf"
F3=F2
S1=10
S2=10
S3=10
W=0
TH=2
PH=4
B=4
HR=3
RO=0
HO=0
P2=1.1
P3=1.1
O1=O2=O3=0

def z():
 bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
def txt(s,f,n,y,h,b=0):
 if not s:return
 c=bpy.data.curves.new(s,'FONT');c.body=s;c.align_x='LEFT';c.align_y='BOTTOM_BASELINE';c.size=n;c.extrude=h;c.offset=b;c.resolution_u=12
 if os.path.isfile(f):c.font=bpy.data.fonts.load(f)
 o=bpy.data.objects.new(s,c);bpy.context.collection.objects.link(o);o.location=(0,y,0);bpy.context.view_layer.objects.active=o;o.select_set(True);bpy.ops.object.convert(target='MESH');o.select_set(False);return o
def cyl(x,y,r,h):
 bpy.ops.mesh.primitive_cylinder_add(vertices=64,radius=r,depth=h,location=(x,y,h/2));return bpy.context.object
def uni(a,b):
 m=a.modifiers.new('u','BOOLEAN');m.operation='UNION';m.solver='EXACT';m.object=b;bpy.context.view_layer.objects.active=a;bpy.ops.object.modifier_apply(modifier=m.name);bpy.data.objects.remove(b,do_unlink=True)
def sub(a,b):
 m=a.modifiers.new('s','BOOLEAN');m.operation='DIFFERENCE';m.solver='EXACT';m.object=b;bpy.context.view_layer.objects.active=a;bpy.ops.object.modifier_apply(modifier=m.name);bpy.data.objects.remove(b,do_unlink=True)

z()
q=[]
for s,f,n,o,p in ((L1,F1,S1,O1,0),(L2,F2,S2,O2,-S1*P2),(L3,F3,S3,O3,-(S1*P2+S2*P3))):
 if s:q.append(txt(s,f,n,p,PH,B+W))
if not q:raise SystemExit('texto vazio')
a=q[0]
for b in q[1:]:uni(a,b)
uni(a,cyl(-3+RO,S1*.5+HO,HR+2,PH))
uni(a,cyl(2,S1*.5+HO,HR+2,PH))
sub(a,cyl(-3+RO,S1*.5+HO,HR,PH+2))
for s,f,n,o,p in ((L1,F1,S1,O1,0),(L2,F2,S2,O2,-S1*P2),(L3,F3,S3,O3,-(S1*P2+S2*P3))):
 if s:
  t=txt(s,f,n,p,TH+.1,W);t.location.z=PH-.1;uni(a,t)
bpy.ops.object.select_all(action='DESELECT');a.select_set(True);bpy.context.view_layer.objects.active=a
r=a.modifiers.new('r','REMESH');r.mode='VOXEL';r.voxel_size=.08;r.use_smooth_shade=False;bpy.ops.object.modifier_apply(modifier=r.name)
o=os.path.join(os.path.dirname(__file__),'output_blender.stl')
bpy.ops.wm.stl_export(filepath=o,export_selected_objects=True)
