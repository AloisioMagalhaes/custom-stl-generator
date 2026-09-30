Line1_Text="Good";
Line2_Text="";
Line3_Text="";
Font_L1="DynaPuff Condensed:style=Bold";
Font_L2="Bagel Fat One";
Font_L3="Bagel Fat One";
Font_Size_L1=10;
Font_Size_L2=10;
Font_Size_L3=10;
Font_Weight_Steps=0;
Font_Weight=Font_Weight_Steps/10;
Text_Height=2;
Plate_Height=4;
Border_Size=4;
Hole_Radius=3;
Ring_Offset=0;
Hole_Height_Offset=0;
Spacing_L2=1.1;
Spacing_L3=1.1;
Offset_L1=0;
Offset_L2=0;
Offset_L3=0;
$fn=64;

generateBackPlateWithHole();
generateKeychainText();

module generateBackPlateWithHole(){
 difference(){
  generateBackPlate();
  translate([-3+Ring_Offset,fixedHoleY(),0]) cylinder(h=Plate_Height,r=Hole_Radius);
 }
}

module generateBackPlate(){
 linear_extrude(Plate_Height) offset(r=Border_Size) generateTextShape();
 hull(){
  translate([-3+Ring_Offset,fixedHoleY(),0]) cylinder(h=Plate_Height,r=Hole_Radius+2);
  translate([2,fixedHoleY(),0]) cylinder(h=Plate_Height,r=Hole_Radius+2);
 }
}

module generateKeychainText(){
 translate([0,0,Plate_Height]) linear_extrude(Text_Height) generateTextShape();
}

module generateTextShape(){
 union(){
  translate([Offset_L1,0,0]) offset(delta=Font_Weight) text(Line1_Text,size=Font_Size_L1,font=Font_L1);
  if(Line2_Text!="") translate([Offset_L2,-Font_Size_L1*Spacing_L2,0]) offset(delta=Font_Weight) text(Line2_Text,size=Font_Size_L2,font=Font_L2);
  if(Line3_Text!="") translate([Offset_L3,-(Font_Size_L1*Spacing_L2+Font_Size_L2*Spacing_L3),0]) offset(delta=Font_Weight) text(Line3_Text,size=Font_Size_L3,font=Font_L3);
 }
}

function fixedHoleY()=Font_Size_L1*0.5+Hole_Height_Offset;
