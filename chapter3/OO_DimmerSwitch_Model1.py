# Create first DimmerSwitch, turn it on, and raise the level twice
from chapter2.DimmerSwitch import DimmerSwitch

oDimmer1 = DimmerSwitch('Dimmer1')
oDimmer1.turnOn()
oDimmer1.raiseLevel()
oDimmer1.raiseLevel()
# Create second DimmerSwitch, turn it on, and raise the level times
oDimmer2 = DimmerSwitch('Dimmer2')
oDimmer2.turnOn()
oDimmer2.raiseLevel()
oDimmer2.raiseLevel()
oDimmer2.raiseLevel()
# Create third DimmerSwitch, using the default settings
oDimmer3 = DimmerSwitch('Dimmer3')
# Ask each switch to show itself
oDimmer1.show()
oDimmer2.show()
oDimmer3.show()
