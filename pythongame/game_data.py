from typing import Dict

from pythongame.common import *

PLAYER_ENTITY_SIZE = (60, 60)

# TODO: These should be defined where the rest of the enemy data is. Perhaps add register_enemy_size method
ENEMY_ENTITY_SIZE = (28, 28)
ENEMY_2_ENTITY_SIZE = (60, 60)
ENEMY_MAGE_ENTITY_SIZE = (60, 60)
ENEMY_BERSERKER_SIZE = (50, 50)

ENEMY_PROJECTILE_SIZE = (50, 50)
POTION_ENTITY_SIZE = (30, 30)
WALL_SIZE = (50, 50)


class SpriteInitializer:
    def __init__(self, image_file_path: str, scaling_size: Tuple[int, int]):
        self.image_file_path = image_file_path
        self.scaling_size = scaling_size


class UiIconSprite(Enum):
    HEALTH_POTION = 1
    MANA_POTION = 2
    SPEED_POTION = 3
    ATTACK_ABILITY = 4
    HEAL_ABILITY = 5
    AOE_ABILITY = 6
    INVISIBILITY_POTION = 7
    MAGIC_MISSILE = 8
    TELEPORT = 9


class AbilityData:
    def __init__(self, icon_sprite: UiIconSprite, mana_cost: int, key_string: str, pygame_key, cooldown: Millis):
        self.icon_sprite = icon_sprite
        self.mana_cost = mana_cost
        self.key_string = key_string
        self.pygame_key = pygame_key
        self.cooldown = cooldown


ENTITY_SPRITE_INITIALIZERS: Dict[Sprite, SpriteInitializer] = {
    Sprite.PLAYER: SpriteInitializer("resources/player.png", PLAYER_ENTITY_SIZE),
    Sprite.WALL: SpriteInitializer("resources/stone_tile.png", WALL_SIZE)
}

UI_ICON_SPRITE_PATHS: Dict[UiIconSprite, str] = {}

POTION_ICON_SPRITES: Dict[PotionType, UiIconSprite] = {}

ABILITIES: Dict[AbilityType, AbilityData] = {}

BUFF_TEXTS: Dict[BuffType: str] = {}


def register_ability_data(ability_type: AbilityType, ability_data: AbilityData):
    ABILITIES[ability_type] = ability_data


def register_ui_icon_sprite_path(sprite: UiIconSprite, file_path: str):
    UI_ICON_SPRITE_PATHS[sprite] = file_path


def register_entity_sprite_initializer(sprite: Sprite, initializer: SpriteInitializer):
    ENTITY_SPRITE_INITIALIZERS[sprite] = initializer


def register_buff_text(buff_type: BuffType, text: str):
    BUFF_TEXTS[buff_type] = text


def register_potion_icon_sprite(potion_type: PotionType, ui_icon_sprite: UiIconSprite):
    POTION_ICON_SPRITES[potion_type] = ui_icon_sprite
