#!/usr/bin/python

import cv2.cv as cv
import os

def is_rect_nonzero(r):
    (_,_,w,h) = r
    return (w > 0) and (h > 0)


class cutRegion():

    def __init__(self, orig):
        self.name = orig
        self.image = cv.LoadImage(orig)
        self.region = None
        self.drag_start = None
        cv.NamedWindow("Image")
        cv.SetMouseCallback("Image", self.on_mouse)
        #self.selection = None
        
    def on_mouse(self, event, x, y, flags, param):
        if event == cv.CV_EVENT_LBUTTONDOWN: #when start pressing
            self.drag_start = (x, y)
        if event == cv.CV_EVENT_LBUTTONUP: #when release left click
            self.drag_start = None
            self.track_window = self.selection
        if self.drag_start: #in both cases compute coordinates
            xmin = min(x, self.drag_start[0])
            ymin = min(y, self.drag_start[1])
            xmax = max(x, self.drag_start[0])
            ymax = max(y, self.drag_start[1])
            self.selection = (xmin, ymin, xmax - xmin, ymax - ymin)

    def run(self):
        
        copy=cv.CloneImage(self.image)
        
        while True:
            if self.drag_start and is_rect_nonzero(self.selection):
                copy = cv.CloneImage(self.image)
                sub = cv.GetSubRect(copy, self.selection) #Get specified area
                
                #Make the effect of background shadow when selecting a window
                save = cv.CloneMat(sub)
                
                cv.ConvertScale(copy, copy, 0.5)
                cv.Copy(save, sub)
                
                #Draw temporary rectangle
                x,y,w,h = self.selection
                cv.Rectangle(copy, (x,y), (x+w,y+h), (255,255,255))
      
            cv.ShowImage("Image", copy)
            c=cv.WaitKey(1)
            if c==27 or c == 1048603 or c==10: #Break if user enters 'Esc'.
                break

    def saveRegion(self, name=None):
        self.region = cv.GetSubRect(self.image, self.selection)
        if name is None:
            name = os.path.splitext(self.name)[0]+"-region.jpg"
        cv.SaveImage(name, self.region)
        
if __name__ == '__main__':
    import sys
    file = sys.argv[-1:][0]
    cutter = cutRegion(file)
    cutter.run()
    cutter.saveRegion()