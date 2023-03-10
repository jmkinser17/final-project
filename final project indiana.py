# matt kinser
#sdev140-1ON
#this project will let the user decide who will win the indiana vs iowa game

from breezypythongui import EasyFrame 
from tkinter import PhotoImage, messagebox
from tkinter.font import Font



class sportsindiana(EasyFrame):
  def __init__(self):
      EasyFrame.__init__(self , width= 600 , height=600 , title= "Indiana vs Iowa" )
    #adds text to window
      self.addLabel(text="Indiana", row=0, column=0) 
      self.addLabel(text="Iowa", row=1, column=0)
      self.addLabel(text="Score", row=3, column=0)
     #Sets up the window, label, and buttons
     
     # A single label in the first row.
      self.indianaLable = self.addLabel(text = "", row= 4, column = 0, columnspan = 2)
     # four command buttons in the thrid row.
     # click on the indiana image button and the indiana immage will pop up an when you press the iowa image button the iowa logo will apper.
      self.iowaBtn = self.addButton(text = "Iowa image", row = 3, column= 1, command = self.iowalogo  )
      self.IndianaBtn = self.addButton(text = "Indiana image", row = 3, column = 2, command = self.indianalogos )
      self.scoreBtn = self.addButton(text = "indiana", row = 3, column= 3, command= self.Indiana )
      self.restoreBtn = self.addButton(text = "iowa", row = 3, column = 4, state = "normal", command= self.iowa )
   
  def indianaBtn(self):
        self.indianaLable["text"]=""
        self.IndianaBtn["state"]="normal"
        self.scoreBtn["state"]="normal"
        
        
    
  def restoreBtn(self):
      self.indianaLable["text"]= ""
      self.iowaBtn["state"]="normal"
      self.restoreBtn["state"]="normal"
      
  
   
  def indianalogos(self):
      #Displays an image and a caption.
     imageLabel_1 = self.addLabel(text = "" , row = 1, column = 1 )
     textLabel= self.addLabel(text="indiana", row=1, column=1)
      #adds image to logo and text to the window
     self.image_1 = PhotoImage(file= "indiana logo.png")
     imageLabel_1["image"] = self.image_1
     font = Font(family = "Verdana", size = 20, slant = "italic") 
     textLabel["font"] = font
     textLabel["foreground"] = "red"
      

  def iowalogo(self):
      #Displays an image and a caption.
     imageLabel2 = self.addLabel(text = "" , row = 1, column = 3 )
     textLabel= self.addLabel(text="Iowa", row=1, column=3)
      #adds image to logo and text to the window
     self.image2 = PhotoImage ( file= "Iowa logo.png")
     imageLabel2["image"] = self.image2
     font = Font(family = "Verdana", size = 23, slant = "italic") 
     textLabel["font"] = font
     textLabel["foreground"] = "yellow"

     #allows the user to click the button of indiana and get a message the ithey had won and if the user clik the iowa button they get a pop up that says iowa has won
  def Indiana(self):
      self.messageBox(title="Indiana wins", message="indiana wins by 20 points final score Indiana 90-70 Iowa")
  def iowa(self):
      self.messageBox(title="iowa wins", message="iowa wins by 11 points final score Indiana 77-88 Iowa")
  
        
      



      

 
  


        
   
      


  
  #pop up window
def main():
  sportsindiana().mainloop()
  
if __name__ == "__main__":
    main()
