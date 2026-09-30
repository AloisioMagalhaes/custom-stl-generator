import bpy,os
L1="Good";L2="";L3=""
F1=os.path.join(os.path.dirname(__file__),'fonts','DynaPuff_Condensed-Bold.ttf')
F2=os.path.join(os.path.dirname(__file__),'fonts','DynaPuff_Condensed-Regular.ttf');F3=F2
S1=10;S2=10;S3=10;P2=1.1;P3=1.1;PH=4;TH=2;HR=3;R=3;G=1.5
def clean():
 bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
def text(s,f,n,y):
 c=bpy.data.curves.new(s,'FONT');c.body=s;c.align_x='LEFT';c.align_y='BOTTOM_BASELINE';c.size=n;c.extrude=TH;c.resolution_u=16;c.font=bpy.data.fonts.load(f)
 o=bpy.data.objects.new(s,c);bpy.context.collection.objects.link(o);o.location=(0,y,PH);bpy.context.view_layer.objects.active=o;o.select_set(True);bpy.ops.object.convert(target='MESH');o.select_set(False);return o
def box(x,y,w,d,h):
 bpy.ops.mesh.primitive_cube_add(size=1,location=(x,y,h/2));o=bpy.context.object;o.dimensions=(w,d,h);bpy.ops.object.transform_apply(location=False,rotation=False,scale=True);m=o.modifiers.new('b','BEVEL');m.width=R;m.segments=8;bpy.context.view_layer.objects.active=o;bpy.ops.object.modifier_apply(modifier=m.name);return o
def cyl(x,y,r,h):
 bpy.ops.mesh.primitive_cylinder_add(vertices=96,radius=r,depth=h,location=(x,y,h/2));return bpy.context.object
def boolean(a,b,k):
 m=a.modifiers.new(k,'BOOLEAN');m.operation=k;m.solver='EXACT';m.object=b;bpy.context.view_layer.objects.active=a;bpy.ops.object.modifier_apply(modifier=m.name);bpy.data.objects.remove(b,do_unlink=True)
clean();ts=[];y=0
for s,f,n in ((L1,F1,S1),(L2,F2,S2),(L3,F3,S3)):
 if s:ts.append(text(s,f,n,y));y-=n*(P2 if s==L1 else P3)
vs=[o.matrix_world@v.co for o in ts for v in o.data.vertices];mn=min(v.x for v in vs);mx=max(v.x for v in vs);my=min(v.y for v in vs);My=max(v.y for v in vs)
w=mx-mn+2*G+2*HR+6;d=My-my+2*G+6;cx=(mn+mx)/2+HR+3;cy=(my+My)/2
a=box(cx,cy,w,d,PH);boolean(a,cyl(cx-w/2+HR+2,cy,HR,PH+2),'DIFFERENCE')
for o in ts:boolean(a,o,'UNION')
r=a.modifiers.new('r','REMESH');r.mode='VOXEL';r.voxel_size=.06;r.use_smooth_shade=False;bpy.context.view_layer.objects.active=a;bpy.ops.object.modifier_apply(modifier=r.name)
bpy.ops.object.select_all(action='DESELECT');a.select_set(True);bpy.context.view_layer.objects.active=a
o=os.path.join(os.path.dirname(__file__),'output_blender.stl');bpy.ops.wm.stl_export(filepath=o,export_selected_objects=True)
