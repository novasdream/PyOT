# Fix run tests as root.
import sys
sys.path.insert(0, "./test")

import framework
from random import randint

# Test if the framework is even working
class TestFramework(framework.FrameworkTest):
    def test_hasClient(self):
        self.assertTrue(self.client)
        
    def test_isConnected(self):
        self.assertTrue(self.tr.connected)
        
    def test_canReadWrite(self):
        self.tr.sendPacket('bb', 0, 0)
        self.assertTrue(self.tr.value())
        self.assertTrue(self.client._data)

# Test the virtual player
class TestVirtualPlayer(framework.FrameworkTestGame):
    def test_existance(self):
        # Do this player even exist?
        self.assertTrue(getPlayer(self.player.data["name"]))
        
        # Are we placed?
        self.assertTrue(self.player in self.player.position.getTile().things)
        
        # cid lookup?
        self.assertTrue(self.player.cid in game.creature.allCreatures)
        
        # And it's us?
        self.assertIs(game.creature.allCreatures[self.player.cid], self.player)
        
    def test_multiplayers(self):
        player = self.setupPlayer(randint(1, 0x7FFFFFFF), "__TEST2__")
        
        players = game.creature.getPlayers(player.position)

        self.assertTrue(players)
        self.assertEqual(len(players), 2)
        self.assertTrue(self.player in players)
        self.assertTrue(player in players)
