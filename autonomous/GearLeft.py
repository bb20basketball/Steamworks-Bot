from robotpy_ext.autonomous import StatefulAutonomous, timed_state, state

class DriveForward(StatefulAutonomous):

    MODE_NAME = 'Gear Left'

    def initialize(self):

        pass

    @timed_state(duration=0.5, next_state='toPeg', first=True)
    def drive_wait(self):
        self.gearDrop.set(False)
        self.drive.mecanumDrive_Cartesian(0,0,0,0) #Strafe Left, Forward Back, Strafe Right, Intensity)
        

    @timed_state(duration=4, next_state="OpenJaws")
    def toPeg(self):
        self.gearDrop.set(False)
        if self.ultrasonic.getRangeInches()<9:
            self.next_state("OpenJaws")
        else:
            self.drive.mecanumDrive_Cartesian(0,-1,0,.3)
        print (self.ultrasonic.getRangeInches())

    @timed_state(duration=.6, next_state="openUp")
    def OpenJaws(self):
        self.gearDrop.set(True)
        self.drive.mecanumDrive_Cartesian(0,0,0,0)
        

    @timed_state(duration=1, next_state="pushGear")
    def openUp(self):
        self.gearDrop.set(True)
        self.drive.mecanumDrive_Cartesian(0,0,0,0)
        
        
    @timed_state(duration=1, next_state="backAfterPush")
    def pushGear(self):
        self.gearDrop.set(False)
        self.drive.mecanumDrive_Cartesian(0,-1,0,.23)
        
    @timed_state(duration=1, next_state="onWards")
    def backAfterPush(self):
        self.gearDrop.set(False)
        self.drive.mecanumDrive_Cartesian(0,1,0,.3)



    @timed_state(duration=2, next_state="stop")
    def onWards(self):
        self.gearDrop.set(False)
        self.drive.mecanumDrive_Cartesian(0,-1,0,.5)
   
    @state()
    def stop(self):
        self.drive.mecanumDrive_Cartesian(0,0,0,0)


