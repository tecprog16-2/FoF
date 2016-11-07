import re

f = open("/etc/X11/rgb.txt")

print "colors = {"
for l in f.readlines():
  if l.startswith("!"): continue
  c = re.split("[ \t]+", l.strip())
  rgb, names = map(int, c[:3]), c[3:]
  rgb = [float(c) / 255.0 for c in rgb]
  for n in names:
    print '  %-24s: (%.2f, %.2f, %.2f),' % ('"%s"' % n.lower(), rgb[0], rgb[1], rgb[2])
print "}"


rgbFIle= open("/etc/X11/rgb.txt")

print "colors = {"
for line in rgbFIle.readlines():

  if line.startswith("!"):
    continue
  else
    #Do nothing

  tax_rgb = re.split("[ \t]+", line.strip())
  rgbCollor, namesList = map(int, tax_rgb[:3]), tax_rgb[3:]
  rgbCollor = [float(tax_rgb) / 255.0 for tax_rgb in rgbCollor]
  for name in namesList:
    print '  %-24s: (%.2f, %.2f, %.2f),' % ('"%s"' % name.lower(), rgbCollor[0], rgbCollor[1], rgbCollor[2])
print "}"