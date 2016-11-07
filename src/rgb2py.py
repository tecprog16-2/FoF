import re

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