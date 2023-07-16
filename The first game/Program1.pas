uses graphabc;
var 
x,y,i,a,b,c,x1,y1,p,xx,yy,ra,z,xx1,yy1,a1:integer;
p1,p2,p3,p4,p5,p6:picture;
n,n1,n3:system.Media.SoundPlayer;
game:boolean;
begin
randomize;
window.Maximize;
font.Size:=20;
n:= new system.Media.SoundPlayer('gun1.wav');
n1:= new system.Media.SoundPlayer('gun2.wav');
n3:= new system.Media.SoundPlayer('reload2.wav');
p1:=picture.Create('1.png');
p2:=picture.Create('2.png');
p3:=picture.Create('3.png');
p4:=picture.Create('4.png');
p5:=picture.Create('5.png');
p6:=picture.Create('6.png');
x1:=-300;
y1:=-300;
xx:=200;
yy:=200;
x:=650;
y:=300;
b:=200;
c:=200;
z:=5;
game:=true;
  OnkeyDown := key ->
  case key of
  vk_a: begin p:=1; x1:=x1+5; b:=b+5;end;
  vk_d:begin p:=2;  x1:=x1-5; b:=b-5;end;
  vk_w:begin y1:=y1+5; c:=c+5; end;
  vk_s:begin  y1:=y1-5; c:=c-5; end;
  vk_r:begin z:=5; n3.Play;end;
  end;
  
  onmousemove:=(x,y,mb) ->
  if x>650 then a:=2
  else a:=1;

  onmousedown:=(x,y,mb) ->
  begin 
  ra:=random(1,2);

  if (z<=5) and (z>0) then begin
  if ra=1 then
  n.Play else n1.Play; end;
   if  (z>0) then 
  z:=z-1;

 if (mb=1) and (x>(x1+xx1)) and (y>(y1+yy1)) and (x<(x1+xx1+100)) and (y<(y1+yy1+100)) and (z <> 0)  then
 begin
   i:=i+1;
   xx1:=random(0,1000);
    yy1:=random(0,1000);
  end;
  
  if (mb=1) and (x>(x1+xx)) and (y>(y1+yy)) and (x<(x1+xx+100)) and (y<(y1+yy+100)) and (z <> 0) then
  begin
  i:=i+1;
  xx:=random(0,1000);
    yy:=random(0,1000);
  end;
  end;
       
  while game do begin
  window.Clear;
  lockdrawing;
  p1.Draw(x1,y1);
  p6.Draw(x1+xx,y1+yy,100,100);
   p6.Draw(x1+xx1,y1+yy1,100,100);
  if p=1 then
  p3.Draw(x,y,50,100)
  else
  p2.Draw(x,y,50,100);
  if a=1 then
  p5.draw(x-20,y+40,40,25)
  else
  p4.Draw(x+40,y+40,40,25);
  if i<20 then
   textout(10,10,i+'/20');
   textout(800,600,'Bulletz '+z+'/5');
   if i=20 then begin font.Size:=200;font.Color:=clgreen; textout(100,100,'YOU WIN'); end;
  redraw;

if (x1+xx)>x then xx:=xx-5 else xx:=xx+5;
if (y1+yy)>y then yy:=yy-5 else yy:=yy+5;
if (x1+xx1)>x then xx1:=xx1-5 else xx1:=xx1+5;
if (y1+yy1)>y then yy1:=yy1-5 else yy1:=yy1+5;
  end;
end.