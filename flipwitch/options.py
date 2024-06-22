from dataclasses import dataclass

from Options import Toggle, Choice, DefaultOnToggle, Range, PerGameCommonOptions, StartInventoryPool




class DeathLink(Toggle):
    """If on: Whenever another player on death link dies, you will be returned to the starting room."""
    display_name = "Death Link"


@dataclass
class FlipWitchOptions(PerGameCommonOptions):
    #Censorship Mode
    #Random Gender
    death_link: DeathLink
    start_inventory_from_pool: StartInventoryPool
