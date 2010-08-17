#!/usr/bin/python

import cairo
import xml.dom.minidom

scale=0.5
def xmltopng(ifname="../as3/strokes018.xml",ofname="strokes018"):
  xmlDoc = xml.dom.minidom.parse(ifname)
  slides = xmlDoc.getElementsByTagName("slide") ; slideidx = 0
  for slide in slides:
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, int(640*scale), int(480*scale))
    ctx = cairo.Context(surface)
    ctx.set_source_rgb(1.0,1.0,1.0)
    ctx.paint()
    for curve in slide.getElementsByTagName("curve"):
      oldposx = None
      for point in curve.getElementsByTagName("point"):
        posx      = float(point.getElementsByTagName('posx')[0].childNodes[0].toxml())*scale
        posy      = float(point.getElementsByTagName('posy')[0].childNodes[0].toxml())*scale
        colorr    = float(point.getElementsByTagName('colorr')[0].childNodes[0].toxml())/255.
        colorg    = float(point.getElementsByTagName('colorg')[0].childNodes[0].toxml())/255.
        colorb    = float(point.getElementsByTagName('colorb')[0].childNodes[0].toxml())/255.
        thickness = float(point.getElementsByTagName('thickness')[0].childNodes[0].toxml())*scale*scale
        if oldposx:
          ctx.set_source_rgb(colorr,colorg,colorb)
          ctx.set_line_cap(cairo.LINE_CAP_ROUND)
          ctx.move_to(oldposx,oldposy)
          ctx.line_to(posx,posy)
          ctx.set_line_width(thickness)
          ctx.stroke()
        oldposx, oldposy = posx, posy
    surface.write_to_png("%s-%03d.png" % (ofname,slideidx))
    slideidx += 1

if __name__ == "__main__":
    import sys
    xmltopng(sys.argv[1], sys.argv[2])
