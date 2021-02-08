--Add Playermodel
player_manager.AddValidModel( "My PM", "models/my_pm.mdl" )
player_manager.AddValidHands( "My PM", "models/my_pm_arm.mdl", 0, "0000000" )

--Add NPC
local Category = "My NPC"

--Friendly NPC
local NPC = 
{
    Name = "My NPC - Friendly",
    Class = "npc_citizen",
	Model = "models/my_npc_friendly.mdl",
	Health = "250",
	KeyValues = { citizentype = 4 },
	Category = Category
}
list.Set( "NPC", "my_npc_friendly", NPC )

--Hostile NPC
local NPC = 
{
    Name = "My NPC - Hostile",
	Class = "npc_combine_s",
	Model = "models/my_npc_hostile.mdl",
	Health = "250",
	Category = Category
}
list.Set( "NPC", "my_npc_hostile", NPC )