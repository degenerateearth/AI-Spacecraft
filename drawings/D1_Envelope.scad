// Degen-1 Rev A: visual allocation only. Units mm. NOT manufacturing CAD.
// Origin at nominal geometric center; camera optical axis +X.
module box(lo,hi,col){color(col)translate([0,0,(lo+hi)/2])cube([88,88,hi-lo],center=true);}
color([.4,.45,.5])for(x=[-46,46])for(y=[-46,46])translate([x,y,0])cube([8,8,113.5],center=true);
box(-21,-15,[.7,.5,.8]); // adapter envelope
box(-12,14.5,[.4,.7,.6]); // EPS/battery envelope
box(20,36,[.4,.6,.85]); // carrier and top-side avionics allocation
box(44,51,[.7,.75,.8]); // AntS allocation, not actual mechanism
color([.9,.65,.3])translate([25,0,-35.5])cube([45,42,25],center=true);
// Six panel placeholders omitted where they obscure internal view.
