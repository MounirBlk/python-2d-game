from pythongame.common import *
from pythongame.game_state import GameState
from pythongame.visual_effects import VisualCircle, create_visual_healing_text, create_visual_mana_text


class PotionWasConsumed:
    pass


class PotionFailedToBeConsumed:
    def __init__(self, reason):
        self.reason = reason


def _create_visual_effect_at_player(game_state):
    game_state.visual_effects.append(VisualCircle(
        (230, 230, 230), game_state.player_entity.get_center_position(), 55, Millis(90), 3,
        game_state.player_entity))


def try_consume_potion(potion_type: PotionType, game_state: GameState):
    player_state = game_state.player_state
    if potion_type == PotionType.HEALTH:
        if game_state.player_state.health < game_state.player_state.max_health:
            _create_visual_effect_at_player(game_state)
            healing_amount = 100
            game_state.visual_effects.append(create_visual_healing_text(game_state.player_entity, healing_amount))
            player_state.gain_health(healing_amount)
            return PotionWasConsumed()
        else:
            return PotionFailedToBeConsumed("Already at full health!")
    elif potion_type == PotionType.MANA:
        if game_state.player_state.mana < game_state.player_state.max_mana:
            _create_visual_effect_at_player(game_state)
            mana_amount = 25
            player_state.gain_mana(mana_amount)
            game_state.visual_effects.append(create_visual_mana_text(game_state.player_entity, mana_amount))
            return PotionWasConsumed()
        else:
            return PotionFailedToBeConsumed("Already at full mana!")
    elif potion_type == PotionType.SPEED:
        _create_visual_effect_at_player(game_state)
        game_state.player_state.gain_buff(BuffType.INCREASED_MOVE_SPEED, Millis(3500))
        return PotionWasConsumed()
    elif potion_type == PotionType.INVISIBILITY:
        _create_visual_effect_at_player(game_state)
        game_state.player_state.gain_buff(BuffType.INVISIBILITY, Millis(5000))
        return PotionWasConsumed()
    else:
        raise Exception("Unhandled potion: " + str(potion_type))
