# jormungandr
Modern Linux desktop screen reader

Communication between the components:
REST is using JSON. so this might be a good idea. Its slim and fast.

The core need so be able to do the following actions to the components.
Speech (connected via TCP/ IP):
- Say
- Stop
- Set Config
- Set Pitch
- Set Rate
- Set Volume
- Set Language
- Set Voice
- Set Gender
- Set Module
- Restart
- Shutdown

Input (connected via TCP/ IP):
- Set Config
- Shutdown
- Restart
- Send Input To System
- Clear Buffer

Braille (connected via TCP/ IP):
- Set Message (for notifications)
- Set Text
- Set Config
- Set Braille Table
- Set offset
- Set Cursor
- Set Module
- Restart
- Shutdown

Sound (connected via TCP/ IP):
- Play Sound
- Play Frequence
- Stop
- Set Config
- Restart
- Shutdown
- Set Volume

Remote (loaded into the core):
- Set Config
- Restart
- Shutdown

Data Miner (connected via TCP/ IP):
- Set Config
- Force Update
- Set Active
- Set Deactive
- Restart
- Shutdown

Data Processor (connected via TCP/ IP):
- Set Config
- Force Update
- Set Active
- Set Deactive
- Restart
- Shutdown
- Set Screen
- Get Curser Position
- Get Content At Offset

The Data Miner need to do the following Actions:
Core (connected via TCP/ IP):
- Set Screen

Processor (connected via TCP/ IP):
- Set Content (complete content)
- Update Content (partial update)
- Update Cursor Position

The Data Processor need to do the following via network:
Core (connected via TCP/ IP):
- Speak
- Sound
- Braille

Data Miner (connected via TCP/ IP):
- Get Content (complete content)
- Update Content (partial update)
- Update Cursor Position

The Input Module need to send the input to the core
Input (connected via TCP/ IP):
- Send Key ( to core, this one detects shortcuts)

So the Network should look like the following:
All components are connected to the core.
Additional, the DataMiners are connected to the DataProcessor
