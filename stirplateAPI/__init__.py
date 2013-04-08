"""
A class to translate low levels to high levels.

Device SKU: ALAMEDA-ST-1
Software Rev: 0.1


"""
import LabJackPython, u6, time


DAC0_REGISTER = 5000
DAC1_REGISTER = 5002

class stirPlate():
    """
    The stir plate class allows access to the ALAMEDA-ST-1 stir plate.
    
    """
    

    def __init__(self):
        
        """
        Name: stirPlate.__init__()
        
        Args: None
        
        Desc: Makes a new instance of the stir_plate class.
        """
        
        DAC0_REGISTER = 5000
        DAC1_REGISTER = 5002
        print "hello"
        self.mode = ""
        self.on = False
        self.d = False
        self.stir_speed = 0
        
    def connect(self):
        
        """
        Name: stir_plate.__init__()
        
        Args: None
        
        Desc: Connects to the stir plate.
        """
        
        print "connected"
        
        
        if self.mode == "digital":
            print "your mode is digital"
            
        else:
            
            self.d = u6.U6()
            print "Alameda lab's stir plate detected"
            
            
            
    def On(self):
        
        """
        Name: stirPlate.On()
        
        Args: None
        
        Desc: Self explanatory.
        """
        if self.mode == "digital":
            print "your mode is digital"
            
        else:
            
            
            self.d.writeRegister(DAC0_REGISTER, 0.02) # Set DAC0 to 0.02V to turn plate off
            self.On = True 
            
    def Off(self):
        
        """
        Name: stirPlate.Off()
        
        Args: None
        
        Desc: Self explanatory.
        """
        
        if self.mode == "digital":
            print "your mode is digital"
            
        else:            
            
            self.d.writeRegister(DAC0_REGISTER, 5) # Set DAC0 to 0.02V to turn plate off
            print "Stir plate off"
            self.On = False 
            
    def set_stir_speed(self,flRPM):
        
        """
        Name: stir_plate.setStirSpeed
        
        Args: None
        
        Desc: 
        """
        
        assert flRPM <= 1540.0 #Fix this at some point
        
        linear_constant = 5.19/1600.0 # volts/RPM
        
        
        
        if self.mode == "digital":
            print "your mode is digital"
            
        else:            
            
            
                
            new_stir_speed = flRPM*linear_constant
            self.d.writeRegister(DAC1_REGISTER, new_stir_speed) # Set DAC0 to 0.02V to turn plate off
            self.stir_speed = str(new_stir_speed/linear_constant)
            
            if flRPM == 0.0:
                self.Off()
            print "Stir plate set to: " +  self.stir_speed + " RPM"




