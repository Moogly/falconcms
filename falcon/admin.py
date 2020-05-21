from django.contrib import admin
from django.contrib.admin import AdminSite

from falcon import models


class FalconAdminSite(AdminSite):
    site_header = 'Housekeeping'
    site_title = 'FalconCMS'
    index_title = 'Housekeeping'


admin_site = FalconAdminSite(name='housekeeping')


class AchievementsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'level',
        'reward_amount',
        'reward_type',
        'points',
        'progress_needed',
    )
    search_fields = ('name',)


class AchievementsTalentsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'type',
        'level',
        'achievement_ids',
        'achievement_levels',
        'reward_furni',
        'reward_perks',
        'reward_badges',
    )
    list_filter = (
        'id',
        'type',
        'level',
        'achievement_ids',
        'achievement_levels',
        'reward_furni',
        'reward_perks',
        'reward_badges',
    )


class BansAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        'ip',
        'machine_id',
        'user_staff_id',
        'timestamp',
        'ban_expire',
        'ban_reason',
        'type',
        'cfh_topic',
    )
    list_filter = (
        'user_id',
        'ip',
        'machine_id',
        'user_staff_id',
        'timestamp',
        'ban_expire',
        'ban_reason',
        'type',
        'cfh_topic',
    )


class BotServesAdmin(admin.ModelAdmin):
    list_display = ('keys', 'item')
    list_filter = ('keys', 'item')


class BotsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user_id',
        'room_id',
        'name',
        'motto',
        'figure',
        'gender',
        'x',
        'y',
        'z',
        'rot',
        'chat_lines',
        'chat_auto',
        'chat_random',
        'chat_delay',
        'dance',
        'freeroam',
        'type',
        'effect',
    )
    list_filter = (
        'id',
        'user_id',
        'room_id',
        'name',
        'motto',
        'figure',
        'gender',
        'x',
        'y',
        'z',
        'rot',
        'chat_lines',
        'chat_auto',
        'chat_random',
        'chat_delay',
        'dance',
        'freeroam',
        'type',
        'effect',
    )
    search_fields = ('name',)


class CalendarRewardsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'custom_image',
        'credits',
        'points',
        'points_type',
        'badge',
        'item_id',
    )
    list_filter = (
        'id',
        'custom_image',
        'credits',
        'points',
        'points_type',
        'badge',
        'item_id',
    )


class CalendarRewardsClaimedAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'reward_id', 'timestamp')
    list_filter = ('user_id', 'reward_id', 'timestamp')


class CameraWebAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'room_id', 'timestamp', 'url')
    list_filter = ('id', 'user_id', 'room_id', 'timestamp', 'url')


class CatalogClothingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'setid')
    search_fields = ('name',)


class CatalogClubOffersAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'enabled',
        'name',
        'days',
        'credits',
        'points',
        'points_type',
        'type',
        'deal',
    )
    list_filter = (
        'id',
        'enabled',
        'name',
        'days',
        'credits',
        'points',
        'points_type',
        'type',
        'deal',
    )
    search_fields = ('name',)


class CatalogFeaturedPagesAdmin(admin.ModelAdmin):
    list_display = (
        'slot_id',
        'image',
        'caption',
        'type',
        'expire_timestamp',
        'page_name',
        'page_id',
        'product_name',
    )
    list_filter = (
        'slot_id',
        'image',
        'caption',
        'type',
        'expire_timestamp',
        'page_name',
        'page_id',
        'product_name',
    )


class CatalogItemsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'item_ids',
        'page_id',
        'offer_id',
        'song_id',
        'order_number',
        'catalog_name',
        'cost_credits',
        'cost_points',
        'points_type',
        'amount',
        'limited_sells',
        'limited_stack',
        'extradata',
        'have_offer',
        'club_only',
    )


class CatalogItemsLimitedAdmin(admin.ModelAdmin):
    list_display = (
        'catalog_item_id',
        'number',
        'user_id',
        'timestamp',
        'item_id',
    )
    list_filter = (
        'catalog_item_id',
        'number',
        'user_id',
        'timestamp',
        'item_id',
    )


class CatalogPagesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'parent_id',
        'page_layout',
        'caption_save',
        'caption',
        'icon_color',
        'icon_image',
        'min_rank',
        'order_num',
        'room_id',
        'visible',
        'enabled',
        'club_only',
        'vip_only',
        'page_headline',
        'page_teaser',
        'page_special',
        'page_text1',
        'page_text2',
        'page_text_details',
        'page_text_teaser',
        'includes',
    )


class CatalogTargetOffersAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'offer_code',
        'title',
        'description',
        'image',
        'icon',
        'end_timestamp',
        'credits',
        'points',
        'points_type',
        'purchase_limit',
        'catalog_item',
        'vars',
    )
    list_filter = (
        'id',
        'offer_code',
        'title',
        'description',
        'image',
        'icon',
        'end_timestamp',
        'credits',
        'points',
        'points_type',
        'purchase_limit',
        'catalog_item',
        'vars',
    )


class ChatlogsPrivateAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user_from_id',
        'user_to_id',
        'message',
        'timestamp',
    )
    list_filter = (
        'id',
        'user_from_id',
        'user_to_id',
        'message',
        'timestamp',
    )


class ChatlogsRoomAdmin(admin.ModelAdmin):
    list_display = (
        'room_id',
        'user_from_id',
        'user_to_id',
        'message',
        'timestamp',
    )
    list_filter = ('room_id', 'user_from_id', 'user_to_id')


class CommandlogsAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'timestamp', 'command', 'params', 'succes')
    list_filter = ('user_id', 'timestamp', 'command', 'params', 'succes')


class CraftingAltarsRecipesAdmin(admin.ModelAdmin):
    list_display = ('altar_id', 'recipe_id')
    list_filter = ('altar_id', 'recipe_id')


class CraftingRecipesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'product_name',
        'reward',
        'enabled',
        'achievement',
        'secret',
        'limited',
        'remaining',
    )
    list_filter = (
        'id',
        'product_name',
        'reward',
        'enabled',
        'achievement',
        'secret',
        'limited',
        'remaining',
    )


class CraftingRecipesIngredientsAdmin(admin.ModelAdmin):
    list_display = ('recipe_id', 'item_id', 'amount')
    list_filter = ('recipe_id',)


class EmulatorErrorsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'timestamp',
        'version',
        'build_hash',
        'type',
        'stacktrace',
    )


class EmulatorSettingsAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')


class EmulatorTextsAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')


class GiftWrappersAdmin(admin.ModelAdmin):
    list_display = ('id', 'sprite_id', 'item_id', 'type')
    list_filter = ('id', 'sprite_id', 'item_id', 'type')


class GroupsItemsAdmin(admin.ModelAdmin):
    list_display = ('type', 'id', 'firstvalue', 'secondvalue', 'enabled')


class GuildForumViewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'guild_id', 'timestamp')
    list_filter = ('id', 'user_id', 'guild_id', 'timestamp')


class GuildsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user_id',
        'name',
        'description',
        'room_id',
        'state',
        'rights',
        'color_one',
        'color_two',
        'badge',
        'date_created',
        'forum',
        'read_forum',
        'post_messages',
        'post_threads',
        'mod_forum',
    )
    list_filter = (
        'id',
        'user_id',
        'name',
        'description',
        'room_id',
        'state',
        'rights',
        'color_one',
        'color_two',
        'badge',
        'date_created',
        'forum',
        'read_forum',
        'post_messages',
        'post_threads',
        'mod_forum',
    )
    search_fields = ('name',)


class GuildsElementsAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstvalue', 'secondvalue', 'type', 'enabled')


class GuildsForumsCommentsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'thread_id',
        'user_id',
        'message',
        'created_at',
        'state',
        'admin_id',
    )
    list_filter = (
        'id',
        'thread_id',
        'user_id',
        'message',
        'created_at',
        'state',
        'admin_id',
    )


class GuildsForumsThreadsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'guild_id',
        'opener_id',
        'subject',
        'posts_count',
        'created_at',
        'updated_at',
        'state',
        'pinned',
        'locked',
        'admin_id',
    )
    list_filter = (
        'id',
        'guild_id',
        'opener_id',
        'subject',
        'posts_count',
        'created_at',
        'updated_at',
        'state',
        'pinned',
        'locked',
        'admin_id',
    )


class GuildsMembersAdmin(admin.ModelAdmin):
    list_display = ('id', 'guild_id', 'user_id', 'level_id', 'member_since')
    list_filter = ('id', 'guild_id', 'user_id', 'level_id', 'member_since')


class HotelviewNewsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'text',
        'button_text',
        'button_type',
        'button_link',
        'image',
    )
    list_filter = (
        'id',
        'title',
        'text',
        'button_text',
        'button_type',
        'button_link',
        'image',
    )


class ItemsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user_id',
        'room_id',
        'item_id',
        'wall_pos',
        'x',
        'y',
        'z',
        'rot',
        'extra_data',
        'wired_data',
        'limited_data',
        'guild_id',
    )


class ItemsBaseAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'sprite_id',
        'item_name',
        'public_name',
        'width',
        'length',
        'stack_height',
        'allow_stack',
        'allow_sit',
        'allow_lay',
        'allow_walk',
        'allow_gift',
        'allow_trade',
        'allow_recycle',
        'allow_marketplace_sell',
        'allow_inventory_stack',
        'type',
        'interaction_type',
        'interaction_modes_count',
        'vending_ids',
        'multiheight',
        'customparams',
        'effect_id_male',
        'effect_id_female',
        'clothing_on_walk',
    )


class ItemsCrackableAdmin(admin.ModelAdmin):
    list_display = (
        'item_id',
        'count',
        'prizes',
        'achievement_tick',
        'achievement_cracked',
        'required_effect',
        'subscription_duration',
        'subscription_type',
    )
    list_filter = (
        'item_id',
        'count',
        'prizes',
        'achievement_tick',
        'achievement_cracked',
        'required_effect',
        'subscription_duration',
        'subscription_type',
    )


class ItemsHighscoreDataAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'item_id',
        'user_ids',
        'score',
        'is_win',
        'timestamp',
    )
    list_filter = (
        'id',
        'item_id',
        'user_ids',
        'score',
        'is_win',
        'timestamp',
    )


class ItemsHoppersAdmin(admin.ModelAdmin):
    list_display = ('item_id', 'base_item')
    list_filter = ('item_id', 'base_item')


class ItemsPresentsAdmin(admin.ModelAdmin):
    list_display = ('item_id', 'base_item_reward')
    list_filter = ('item_id', 'base_item_reward')


class ItemsTeleportsAdmin(admin.ModelAdmin):
    list_display = ('teleport_one_id', 'teleport_two_id')


class MarketplaceItemsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'item_id',
        'user_id',
        'price',
        'timestamp',
        'sold_timestamp',
        'state',
    )
    list_filter = (
        'id',
        'item_id',
        'user_id',
        'price',
        'timestamp',
        'sold_timestamp',
        'state',
    )


class MessengerFriendrequestsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_to_id', 'user_from_id')
    list_filter = ('id', 'user_to_id', 'user_from_id')


class MessengerFriendshipsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user_one_id',
        'user_two_id',
        'relation',
        'friends_since',
    )
    list_filter = (
        'id',
        'user_one_id',
        'user_two_id',
        'relation',
        'friends_since',
    )


class MessengerOfflineAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'user_from_id', 'message', 'sended_on')
    list_filter = ('id', 'user_id', 'user_from_id', 'message', 'sended_on')


class NamechangeLogAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'old_name', 'new_name', 'timestamp')
    list_filter = ('user_id', 'old_name', 'new_name', 'timestamp')


class NavigatorFilterAdmin(admin.ModelAdmin):
    list_display = ('key', 'field', 'compare', 'database_query')
    list_filter = ('key', 'field', 'compare', 'database_query')


class NavigatorFlatcatsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'min_rank',
        'caption_save',
        'caption',
        'can_trade',
        'max_user_count',
        'public',
        'list_type',
        'order_num',
    )
    list_filter = (
        'id',
        'min_rank',
        'caption_save',
        'caption',
        'can_trade',
        'max_user_count',
        'public',
        'list_type',
        'order_num',
    )


class NavigatorPubliccatsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'visible', 'order_num')
    list_filter = ('id', 'name', 'image', 'visible', 'order_num')
    search_fields = ('name',)


class NavigatorPublicsAdmin(admin.ModelAdmin):
    list_display = ('public_cat_id', 'room_id', 'visible')
    list_filter = ('public_cat_id', 'room_id', 'visible')


class NuxGiftsAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'value', 'image')
    list_filter = ('id', 'type', 'value', 'image')


class OldGuildsForumsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'guild_id',
        'user_id',
        'subject',
        'message',
        'state',
        'admin_id',
        'pinned',
        'locked',
        'timestamp',
    )
    list_filter = (
        'id',
        'guild_id',
        'user_id',
        'subject',
        'message',
        'state',
        'admin_id',
        'pinned',
        'locked',
        'timestamp',
    )


class OldGuildsForumsCommentsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'thread_id',
        'user_id',
        'timestamp',
        'message',
        'state',
        'admin_id',
    )
    list_filter = (
        'id',
        'thread_id',
        'user_id',
        'timestamp',
        'message',
        'state',
        'admin_id',
    )


class PermissionsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'rank_name',
        'badge',
        'level',
        'room_effect',
        'log_commands',
        'prefix',
        'prefix_color',
        'cmd_about',
        'cmd_alert',
        'cmd_allow_trading',
        'cmd_badge',
        'cmd_ban',
        'cmd_blockalert',
        'cmd_bots',
        'cmd_bundle',
        'cmd_calendar',
        'cmd_changename',
        'cmd_chatcolor',
        'cmd_commands',
        'cmd_connect_camera',
        'cmd_control',
        'cmd_coords',
        'cmd_credits',
        'cmd_danceall',
        'cmd_diagonal',
        'cmd_disconnect',
        'cmd_duckets',
        'cmd_ejectall',
        'cmd_empty',
        'cmd_empty_bots',
        'cmd_empty_pets',
        'cmd_enable',
        'cmd_event',
        'cmd_faceless',
        'cmd_fastwalk',
        'cmd_filterword',
        'cmd_freeze',
        'cmd_freeze_bots',
        'cmd_gift',
        'cmd_give_rank',
        'cmd_ha',
        'acc_can_stalk',
        'cmd_hal',
        'cmd_invisible',
        'cmd_ip_ban',
        'cmd_machine_ban',
        'cmd_hand_item',
        'cmd_happyhour',
        'cmd_hidewired',
        'cmd_kickall',
        'cmd_massbadge',
        'cmd_masscredits',
        'cmd_massduckets',
        'cmd_massgift',
        'cmd_masspoints',
        'cmd_moonwalk',
        'cmd_mimic',
        'cmd_multi',
        'cmd_mute',
        'cmd_pet_info',
        'cmd_pickall',
        'cmd_plugins',
        'cmd_points',
        'cmd_promote_offer',
        'cmd_pull',
        'cmd_push',
        'cmd_redeem',
        'cmd_reload_room',
        'cmd_roomalert',
        'cmd_roomcredits',
        'cmd_roomeffect',
        'cmd_roomgift',
        'cmd_roomitem',
        'cmd_roommute',
        'cmd_roompixels',
        'cmd_roompoints',
        'cmd_say',
        'cmd_say_all',
        'cmd_setmax',
        'cmd_set_poll',
        'cmd_setpublic',
        'cmd_setspeed',
        'cmd_shout',
        'cmd_shout_all',
        'cmd_shutdown',
        'cmd_sitdown',
        'cmd_staffalert',
        'cmd_staffonline',
        'cmd_summon',
        'cmd_summonrank',
        'cmd_super_ban',
        'cmd_stalk',
        'cmd_superpull',
        'cmd_take_badge',
        'cmd_talk',
        'cmd_teleport',
        'cmd_trash',
        'cmd_transform',
        'cmd_unban',
        'cmd_unload',
        'cmd_unmute',
        'cmd_update_achievements',
        'cmd_update_bots',
        'cmd_update_catalogue',
        'cmd_update_config',
        'cmd_update_guildparts',
        'cmd_update_hotel_view',
        'cmd_update_items',
        'cmd_update_navigator',
        'cmd_update_permissions',
        'cmd_update_pet_data',
        'cmd_update_plugins',
        'cmd_update_polls',
        'cmd_update_texts',
        'cmd_update_wordfilter',
        'cmd_userinfo',
        'cmd_word_quiz',
        'cmd_warp',
        'acc_anychatcolor',
        'acc_anyroomowner',
        'acc_empty_others',
        'acc_enable_others',
        'acc_see_whispers',
        'acc_superwired',
        'acc_supporttool',
        'acc_unkickable',
        'acc_guildgate',
        'acc_moverotate',
        'acc_placefurni',
        'acc_unlimited_bots',
        'acc_unlimited_pets',
        'acc_hide_ip',
        'acc_not_mimiced',
        'acc_chat_no_flood',
        'acc_staff_chat',
        'acc_staff_pick',
        'acc_enteranyroom',
        'acc_fullrooms',
        'acc_infinite_credits',
        'acc_infinite_pixels',
        'acc_infinite_points',
        'acc_ambassador',
        'acc_debug',
        'acc_chat_no_limit',
        'acc_chat_no_filter',
        'acc_nomute',
        'acc_guild_admin',
        'acc_catalog_ids',
        'acc_modtool_ticket_q',
        'acc_modtool_user_logs',
        'acc_modtool_user_alert',
        'acc_modtool_user_kick',
        'acc_modtool_user_ban',
        'acc_modtool_room_info',
        'acc_modtool_room_logs',
        'acc_trade_anywhere',
        'acc_update_notifications',
        'acc_helper_use_guide_tool',
        'acc_helper_give_guide_tours',
        'acc_helper_judge_chat_reviews',
        'acc_floorplan_editor',
        'acc_camera',
        'acc_ads_background',
        'cmd_wordquiz',
        'acc_room_staff_tags',
        'acc_infinite_friends',
        'acc_mimic_unredeemed',
        'cmd_update_youtube_playlists',
        'cmd_add_youtube_playlist',
        'auto_credits_amount',
        'auto_pixels_amount',
        'auto_gotw_amount',
        'auto_points_amount',
        'acc_mention',
    )
    list_filter = (
        'id',
        'rank_name',
        'badge',
        'level',
        'room_effect',
        'log_commands',
        'prefix',
        'prefix_color',
        'cmd_about',
        'cmd_alert',
        'cmd_allow_trading',
        'cmd_badge',
        'cmd_ban',
        'cmd_blockalert',
        'cmd_bots',
        'cmd_bundle',
        'cmd_calendar',
        'cmd_changename',
        'cmd_chatcolor',
        'cmd_commands',
        'cmd_connect_camera',
        'cmd_control',
        'cmd_coords',
        'cmd_credits',
        'cmd_danceall',
        'cmd_diagonal',
        'cmd_disconnect',
        'cmd_duckets',
        'cmd_ejectall',
        'cmd_empty',
        'cmd_empty_bots',
        'cmd_empty_pets',
        'cmd_enable',
        'cmd_event',
        'cmd_faceless',
        'cmd_fastwalk',
        'cmd_filterword',
        'cmd_freeze',
        'cmd_freeze_bots',
        'cmd_gift',
        'cmd_give_rank',
        'cmd_ha',
        'acc_can_stalk',
        'cmd_hal',
        'cmd_invisible',
        'cmd_ip_ban',
        'cmd_machine_ban',
        'cmd_hand_item',
        'cmd_happyhour',
        'cmd_hidewired',
        'cmd_kickall',
        'cmd_massbadge',
        'cmd_masscredits',
        'cmd_massduckets',
        'cmd_massgift',
        'cmd_masspoints',
        'cmd_moonwalk',
        'cmd_mimic',
        'cmd_multi',
        'cmd_mute',
        'cmd_pet_info',
        'cmd_pickall',
        'cmd_plugins',
        'cmd_points',
        'cmd_promote_offer',
        'cmd_pull',
        'cmd_push',
        'cmd_redeem',
        'cmd_reload_room',
        'cmd_roomalert',
        'cmd_roomcredits',
        'cmd_roomeffect',
        'cmd_roomgift',
        'cmd_roomitem',
        'cmd_roommute',
        'cmd_roompixels',
        'cmd_roompoints',
        'cmd_say',
        'cmd_say_all',
        'cmd_setmax',
        'cmd_set_poll',
        'cmd_setpublic',
        'cmd_setspeed',
        'cmd_shout',
        'cmd_shout_all',
        'cmd_shutdown',
        'cmd_sitdown',
        'cmd_staffalert',
        'cmd_staffonline',
        'cmd_summon',
        'cmd_summonrank',
        'cmd_super_ban',
        'cmd_stalk',
        'cmd_superpull',
        'cmd_take_badge',
        'cmd_talk',
        'cmd_teleport',
        'cmd_trash',
        'cmd_transform',
        'cmd_unban',
        'cmd_unload',
        'cmd_unmute',
        'cmd_update_achievements',
        'cmd_update_bots',
        'cmd_update_catalogue',
        'cmd_update_config',
        'cmd_update_guildparts',
        'cmd_update_hotel_view',
        'cmd_update_items',
        'cmd_update_navigator',
        'cmd_update_permissions',
        'cmd_update_pet_data',
        'cmd_update_plugins',
        'cmd_update_polls',
        'cmd_update_texts',
        'cmd_update_wordfilter',
        'cmd_userinfo',
        'cmd_word_quiz',
        'cmd_warp',
        'acc_anychatcolor',
        'acc_anyroomowner',
        'acc_empty_others',
        'acc_enable_others',
        'acc_see_whispers',
        'acc_superwired',
        'acc_supporttool',
        'acc_unkickable',
        'acc_guildgate',
        'acc_moverotate',
        'acc_placefurni',
        'acc_unlimited_bots',
        'acc_unlimited_pets',
        'acc_hide_ip',
        'acc_not_mimiced',
        'acc_chat_no_flood',
        'acc_staff_chat',
        'acc_staff_pick',
        'acc_enteranyroom',
        'acc_fullrooms',
        'acc_infinite_credits',
        'acc_infinite_pixels',
        'acc_infinite_points',
        'acc_ambassador',
        'acc_debug',
        'acc_chat_no_limit',
        'acc_chat_no_filter',
        'acc_nomute',
        'acc_guild_admin',
        'acc_catalog_ids',
        'acc_modtool_ticket_q',
        'acc_modtool_user_logs',
        'acc_modtool_user_alert',
        'acc_modtool_user_kick',
        'acc_modtool_user_ban',
        'acc_modtool_room_info',
        'acc_modtool_room_logs',
        'acc_trade_anywhere',
        'acc_update_notifications',
        'acc_helper_use_guide_tool',
        'acc_helper_give_guide_tours',
        'acc_helper_judge_chat_reviews',
        'acc_floorplan_editor',
        'acc_camera',
        'acc_ads_background',
        'cmd_wordquiz',
        'acc_room_staff_tags',
        'acc_infinite_friends',
        'acc_mimic_unredeemed',
        'cmd_update_youtube_playlists',
        'cmd_add_youtube_playlist',
        'auto_credits_amount',
        'auto_pixels_amount',
        'auto_gotw_amount',
        'auto_points_amount',
        'acc_mention',
    )


class PetActionsAdmin(admin.ModelAdmin):
    list_display = (
        'pet_type',
        'pet_name',
        'offspring_type',
        'happy_actions',
        'tired_actions',
        'random_actions',
        'can_swim',
    )


class PetBreedingAdmin(admin.ModelAdmin):
    list_display = ('pet_id', 'offspring_id')
    list_filter = ('pet_id', 'offspring_id')


class PetBreedingRacesAdmin(admin.ModelAdmin):
    list_display = ('pet_type', 'rarity_level', 'breed')
    list_filter = ('pet_type', 'rarity_level', 'breed')


class PetBreedsAdmin(admin.ModelAdmin):
    list_display = (
        'race',
        'color_one',
        'color_two',
        'has_color_one',
        'has_color_two',
    )


class PetCommandsAdmin(admin.ModelAdmin):
    list_display = ('pet_id', 'command_id')
    list_filter = ('pet_id', 'command_id')


class PetCommandsDataAdmin(admin.ModelAdmin):
    list_display = (
        'command_id',
        'text',
        'required_level',
        'reward_xp',
        'cost_happyness',
        'cost_energy',
    )


class PetDrinksAdmin(admin.ModelAdmin):
    list_display = ('pet_id', 'item_id')
    list_filter = ('pet_id', 'item_id')


class PetFoodsAdmin(admin.ModelAdmin):
    list_display = ('pet_id', 'item_id')
    list_filter = ('pet_id', 'item_id')


class PetItemsAdmin(admin.ModelAdmin):
    list_display = ('pet_id', 'item_id')
    list_filter = ('pet_id', 'item_id')


class PetVocalsAdmin(admin.ModelAdmin):
    list_display = ('pet_id', 'type', 'message')
    list_filter = ('pet_id', 'type', 'message')


class PollsAdmin(admin.ModelAdmin):
    list_display = ('title', 'thanks_message', 'reward_badge')
    list_filter = ('title', 'thanks_message', 'reward_badge')


class PollsAnswersAdmin(admin.ModelAdmin):
    list_display = ('poll_id', 'user_id', 'question_id', 'answer')
    list_filter = ('poll_id', 'user_id', 'question_id', 'answer')


class PollsQuestionsAdmin(admin.ModelAdmin):
    list_display = (
        'parent_id',
        'poll_id',
        'order',
        'question',
        'type',
        'min_selections',
        'options',
    )
    list_filter = (
        'parent_id',
        'poll_id',
        'order',
        'question',
        'type',
        'min_selections',
        'options',
    )


class RecyclerPrizesAdmin(admin.ModelAdmin):
    list_display = ('rarity', 'item_id')
    list_filter = ('rarity', 'item_id')


class RoomBansAdmin(admin.ModelAdmin):
    list_display = ('room_id', 'user_id', 'ends')
    list_filter = ('room_id', 'user_id', 'ends')


class RoomEnterLogAdmin(admin.ModelAdmin):
    list_display = ('room_id', 'user_id', 'timestamp', 'exit_timestamp')


class RoomGameScoresAdmin(admin.ModelAdmin):
    list_display = (
        'room_id',
        'game_start_timestamp',
        'game_name',
        'user_id',
        'team_id',
        'score',
        'team_score',
    )
    list_filter = (
        'room_id',
        'game_start_timestamp',
        'game_name',
        'user_id',
        'team_id',
        'score',
        'team_score',
    )


class RoomModelsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'door_x',
        'door_y',
        'door_dir',
        'heightmap',
        'public_items',
        'club_only',
    )
    search_fields = ('name',)


class RoomModelsCustomAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'door_x',
        'door_y',
        'door_dir',
        'heightmap',
    )
    list_filter = ('id', 'name', 'door_x', 'door_y', 'door_dir', 'heightmap')
    search_fields = ('name',)


class RoomMutesAdmin(admin.ModelAdmin):
    list_display = ('room_id', 'user_id', 'ends')
    list_filter = ('room_id', 'user_id', 'ends')


class RoomPromotionsAdmin(admin.ModelAdmin):
    list_display = (
        'room_id',
        'title',
        'description',
        'end_timestamp',
        'start_timestamp',
        'category',
    )
    list_filter = (
        'room_id',
        'title',
        'description',
        'end_timestamp',
        'start_timestamp',
        'category',
    )


class RoomRightsAdmin(admin.ModelAdmin):
    list_display = ('room_id', 'user_id')
    list_filter = ('room_id', 'user_id')


class RoomTradeLogAdmin(admin.ModelAdmin):
    list_display = (
        'user_one_id',
        'user_two_id',
        'user_one_ip',
        'user_two_ip',
        'timestamp',
        'user_one_item_count',
        'user_two_item_count',
    )
    list_filter = (
        'user_one_id',
        'user_two_id',
        'user_one_ip',
        'user_two_ip',
        'timestamp',
        'user_one_item_count',
        'user_two_item_count',
    )


class RoomTradeLogItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_id', 'user_id')
    list_filter = ('id', 'item_id', 'user_id')


class RoomTraxPlaylistAdmin(admin.ModelAdmin):
    list_display = ('room_id', 'item_id')
    list_filter = ('room_id', 'item_id')


class RoomVotesAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'room_id')
    list_filter = ('user_id', 'room_id')


class RoomWordfilterAdmin(admin.ModelAdmin):
    list_display = ('room_id', 'word')
    list_filter = ('room_id', 'word')


class RoomsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'owner_id',
        'owner_name',
        'name',
        'description',
        'model',
        'password',
        'state',
        'users',
        'users_max',
        'guild_id',
        'category',
        'score',
        'paper_floor',
        'paper_wall',
        'paper_landscape',
        'thickness_wall',
        'wall_height',
        'thickness_floor',
        'moodlight_data',
        'tags',
        'is_public',
        'is_staff_picked',
        'allow_other_pets',
        'allow_other_pets_eat',
        'allow_walkthrough',
        'allow_hidewall',
        'chat_mode',
        'chat_weight',
        'chat_speed',
        'chat_hearing_distance',
        'chat_protection',
        'override_model',
        'who_can_mute',
        'who_can_kick',
        'who_can_ban',
        'poll_id',
        'roller_speed',
        'promoted',
        'trade_mode',
        'move_diagonally',
        'jukebox_active',
        'hidewired',
    )
    search_fields = ('name',)


class SanctionLevelsAdmin(admin.ModelAdmin):
    list_display = ('level', 'type', 'hour_length', 'probation_days')
    list_filter = ('level', 'type', 'hour_length', 'probation_days')


class SanctionsAdmin(admin.ModelAdmin):
    list_display = (
        'habbo_id',
        'sanction_level',
        'probation_timestamp',
        'reason',
        'trade_locked_until',
        'is_muted',
        'mute_duration',
    )
    list_filter = (
        'habbo_id',
        'sanction_level',
        'probation_timestamp',
        'reason',
        'trade_locked_until',
        'is_muted',
        'mute_duration',
    )


class SoundtracksAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'author', 'track', 'length')
    list_filter = ('code', 'name', 'author', 'track')
    search_fields = ('name',)


class SpecialEnablesAdmin(admin.ModelAdmin):
    list_display = ('effect_id', 'min_rank')
    list_filter = ('effect_id', 'min_rank')


class SupportCfhCategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_internal', 'name_external')
    list_filter = ('id', 'name_internal', 'name_external')


class SupportCfhTopicsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'category_id',
        'name_internal',
        'name_external',
        'action',
        'ignore_target',
        'auto_reply',
        'default_sanction',
    )


class SupportIssueCategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')
    search_fields = ('name',)


class SupportIssuePresetsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'category',
        'name',
        'message',
        'reminder',
        'ban_for',
        'mute_for',
    )
    list_filter = (
        'id',
        'category',
        'name',
        'message',
        'reminder',
        'ban_for',
        'mute_for',
    )
    search_fields = ('name',)


class SupportPresetsAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'preset')
    list_filter = ('id', 'type', 'preset')


class SupportTicketsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'state',
        'type',
        'timestamp',
        'score',
        'sender_id',
        'reported_id',
        'room_id',
        'mod_id',
        'issue',
        'category',
        'group_id',
        'thread_id',
        'comment_id',
        'photo_item_id',
    )
    list_filter = (
        'id',
        'state',
        'type',
        'timestamp',
        'score',
        'sender_id',
        'reported_id',
        'room_id',
        'mod_id',
        'issue',
        'category',
        'group_id',
        'thread_id',
        'comment_id',
        'photo_item_id',
    )


class UserWindowSettingsAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'x', 'y', 'width', 'height', 'open_searches')
    list_filter = ('user_id', 'x', 'y', 'width', 'height', 'open_searches')


class UsersAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'rank',
        'gender',
        'credits',
        'pixels',
        'points',
        'motto',
        'online',
        'ip_register',
        'ip_current',
        'mail',
        'mail_verified',
        'account_created',
        'account_day_of_birth',
        'last_login',
        'last_online',
        'look',
        'machine_id',
        'home_room',
    )
    list_filter = (
        'id',
        'username',
        'real_name',
        'password',
        'mail',
        'mail_verified',
        'account_created',
        'account_day_of_birth',
        'last_login',
        'last_online',
        'motto',
        'look',
        'gender',
        'rank',
        'credits',
        'pixels',
        'points',
        'online',
        'auth_ticket',
        'ip_register',
        'ip_current',
        'machine_id',
        'home_room',
    )


class UsersAchievementsAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'achievement_name', 'progress')
    list_filter = ('user_id', 'progress')


class UsersAchievementsQueueAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'achievement_id', 'amount')
    list_filter = ('user_id', 'achievement_id', 'amount')


class UsersBadgesAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'slot_id', 'badge_code')


class UsersClothingAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'clothing_id')
    list_filter = ('user_id', 'clothing_id')


class UsersCurrencyAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'type', 'amount')
    list_filter = ('user_id', 'type', 'amount')


class UsersEffectsAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        'effect',
        'duration',
        'activation_timestamp',
        'total',
    )
    list_filter = (
        'user_id',
        'effect',
        'duration',
        'activation_timestamp',
        'total',
    )


class UsersFavoriteRoomsAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'room_id')
    list_filter = ('user_id', 'room_id')


class UsersIgnoredAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'target_id')
    list_filter = ('user_id', 'target_id')


class UsersNavigatorSettingsAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'caption', 'list_type', 'display')
    list_filter = ('user_id', 'caption', 'list_type', 'display')


class UsersPetsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user_id',
        'room_id',
        'name',
        'race',
        'type',
        'color',
        'happyness',
        'experience',
        'energy',
        'hunger',
        'thirst',
        'respect',
        'created',
        'x',
        'y',
        'z',
        'rot',
        'hair_style',
        'hair_color',
        'saddle',
        'ride',
        'mp_type',
        'mp_color',
        'mp_nose',
        'mp_nose_color',
        'mp_eyes',
        'mp_eyes_color',
        'mp_mouth',
        'mp_mouth_color',
        'mp_death_timestamp',
        'mp_breedable',
        'mp_allow_breed',
        'gnome_data',
        'mp_is_dead',
        'saddle_item_id',
    )
    search_fields = ('name',)


class UsersRecipesAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'recipe')
    list_filter = ('user_id', 'recipe')


class UsersSavedSearchesAdmin(admin.ModelAdmin):
    list_display = ('id', 'search_code', 'filter', 'user_id')
    list_filter = ('id', 'search_code', 'filter', 'user_id')


class UsersSettingsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user_id',
        'credits',
        'achievement_score',
        'daily_respect_points',
        'daily_pet_respect_points',
        'respects_given',
        'respects_received',
        'guild_id',
        'can_change_name',
        'can_trade',
        'is_citizen',
        'citizen_level',
        'helper_level',
        'cfh_send',
        'cfh_abusive',
        'cfh_warnings',
        'cfh_bans',
        'block_following',
        'block_friendrequests',
        'block_roominvites',
        'volume_system',
        'volume_furni',
        'volume_trax',
        'old_chat',
        'block_camera_follow',
        'chat_color',
        'home_room',
        'online_time',
        'tags',
        'club_expire_timestamp',
        'login_streak',
        'rent_space_id',
        'rent_space_endtime',
        'hof_points',
        'block_alerts',
        'talent_track_citizenship_level',
        'talent_track_helpers_level',
        'ignore_bots',
        'ignore_pets',
        'nux',
        'mute_end_timestamp',
        'allow_name_change',
        'perk_trade',
        'forums_post_count',
        'ui_flags',
        'has_gotten_default_saved_searches',
    )
    list_filter = (
        'id',
        'user_id',
        'credits',
        'achievement_score',
        'daily_respect_points',
        'daily_pet_respect_points',
        'respects_given',
        'respects_received',
        'guild_id',
        'can_change_name',
        'can_trade',
        'is_citizen',
        'citizen_level',
        'helper_level',
        'cfh_send',
        'cfh_abusive',
        'cfh_warnings',
        'cfh_bans',
        'block_following',
        'block_friendrequests',
        'block_roominvites',
        'volume_system',
        'volume_furni',
        'volume_trax',
        'old_chat',
        'block_camera_follow',
        'chat_color',
        'home_room',
        'online_time',
        'tags',
        'club_expire_timestamp',
        'login_streak',
        'rent_space_id',
        'rent_space_endtime',
        'hof_points',
        'block_alerts',
        'talent_track_citizenship_level',
        'talent_track_helpers_level',
        'ignore_bots',
        'ignore_pets',
        'nux',
        'mute_end_timestamp',
        'allow_name_change',
        'perk_trade',
        'forums_post_count',
        'ui_flags',
        'has_gotten_default_saved_searches',
    )


class UsersTargetOfferPurchasesAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        'offer_id',
        'state',
        'amount',
        'last_purchase',
    )
    list_filter = ('user_id', 'offer_id', 'state', 'amount', 'last_purchase')


class UsersWardrobeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'slot_id', 'look', 'gender')
    list_filter = ('id', 'user_id', 'slot_id', 'look', 'gender')


class VoucherHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'voucher_id', 'user_id', 'timestamp')
    list_filter = ('id', 'voucher_id', 'user_id', 'timestamp')


class VouchersAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'code',
        'credits',
        'points',
        'points_type',
        'catalog_item_id',
        'amount',
        'limit',
    )
    list_filter = (
        'id',
        'code',
        'credits',
        'points',
        'points_type',
        'catalog_item_id',
        'amount',
        'limit',
    )


class WiredRewardsGivenAdmin(admin.ModelAdmin):
    list_display = ('wired_item', 'user_id', 'reward_id', 'timestamp')
    list_filter = ('wired_item', 'user_id', 'reward_id', 'timestamp')


class WordfilterAdmin(admin.ModelAdmin):
    list_display = ('key', 'replacement', 'hide', 'report', 'mute')
    list_filter = ('key', 'replacement', 'hide', 'report', 'mute')


class YoutubePlaylistsAdmin(admin.ModelAdmin):
    list_display = ('item_id', 'playlist_id', 'order')
    list_filter = ('item_id', 'order')


def _register(model, admin_class):
    admin_site.register(model, admin_class)


_register(models.Achievements, AchievementsAdmin)
_register(models.AchievementsTalents, AchievementsTalentsAdmin)
_register(models.Bans, BansAdmin)
_register(models.BotServes, BotServesAdmin)
_register(models.Bots, BotsAdmin)
_register(models.CalendarRewards, CalendarRewardsAdmin)
_register(models.CalendarRewardsClaimed, CalendarRewardsClaimedAdmin)
_register(models.CameraWeb, CameraWebAdmin)
_register(models.CatalogClothing, CatalogClothingAdmin)
_register(models.CatalogClubOffers, CatalogClubOffersAdmin)
_register(models.CatalogFeaturedPages, CatalogFeaturedPagesAdmin)
_register(models.CatalogItems, CatalogItemsAdmin)
_register(models.CatalogItemsLimited, CatalogItemsLimitedAdmin)
_register(models.CatalogPages, CatalogPagesAdmin)
_register(models.CatalogTargetOffers, CatalogTargetOffersAdmin)
_register(models.ChatlogsPrivate, ChatlogsPrivateAdmin)
_register(models.ChatlogsRoom, ChatlogsRoomAdmin)
_register(models.Commandlogs, CommandlogsAdmin)
_register(models.CraftingAltarsRecipes, CraftingAltarsRecipesAdmin)
_register(models.CraftingRecipes, CraftingRecipesAdmin)
_register(models.CraftingRecipesIngredients, CraftingRecipesIngredientsAdmin)
_register(models.EmulatorErrors, EmulatorErrorsAdmin)
_register(models.EmulatorSettings, EmulatorSettingsAdmin)
_register(models.EmulatorTexts, EmulatorTextsAdmin)
_register(models.GiftWrappers, GiftWrappersAdmin)
_register(models.GroupsItems, GroupsItemsAdmin)
_register(models.GuildForumViews, GuildForumViewsAdmin)
_register(models.Guilds, GuildsAdmin)
_register(models.GuildsElements, GuildsElementsAdmin)
_register(models.GuildsForumsComments, GuildsForumsCommentsAdmin)
_register(models.GuildsForumsThreads, GuildsForumsThreadsAdmin)
_register(models.GuildsMembers, GuildsMembersAdmin)
_register(models.HotelviewNews, HotelviewNewsAdmin)
_register(models.Items, ItemsAdmin)
_register(models.ItemsBase, ItemsBaseAdmin)
_register(models.ItemsCrackable, ItemsCrackableAdmin)
_register(models.ItemsHighscoreData, ItemsHighscoreDataAdmin)
_register(models.ItemsHoppers, ItemsHoppersAdmin)
_register(models.ItemsPresents, ItemsPresentsAdmin)
_register(models.ItemsTeleports, ItemsTeleportsAdmin)
_register(models.MarketplaceItems, MarketplaceItemsAdmin)
_register(models.MessengerFriendrequests, MessengerFriendrequestsAdmin)
_register(models.MessengerFriendships, MessengerFriendshipsAdmin)
_register(models.MessengerOffline, MessengerOfflineAdmin)
_register(models.NamechangeLog, NamechangeLogAdmin)
_register(models.NavigatorFilter, NavigatorFilterAdmin)
_register(models.NavigatorFlatcats, NavigatorFlatcatsAdmin)
_register(models.NavigatorPubliccats, NavigatorPubliccatsAdmin)
_register(models.NavigatorPublics, NavigatorPublicsAdmin)
_register(models.NuxGifts, NuxGiftsAdmin)
_register(models.OldGuildsForums, OldGuildsForumsAdmin)
_register(models.OldGuildsForumsComments, OldGuildsForumsCommentsAdmin)
_register(models.Permissions, PermissionsAdmin)
_register(models.PetActions, PetActionsAdmin)
_register(models.PetBreeding, PetBreedingAdmin)
_register(models.PetBreedingRaces, PetBreedingRacesAdmin)
_register(models.PetBreeds, PetBreedsAdmin)
_register(models.PetCommands, PetCommandsAdmin)
_register(models.PetCommandsData, PetCommandsDataAdmin)
_register(models.PetDrinks, PetDrinksAdmin)
_register(models.PetFoods, PetFoodsAdmin)
_register(models.PetItems, PetItemsAdmin)
_register(models.PetVocals, PetVocalsAdmin)
_register(models.Polls, PollsAdmin)
_register(models.PollsAnswers, PollsAnswersAdmin)
_register(models.PollsQuestions, PollsQuestionsAdmin)
_register(models.RecyclerPrizes, RecyclerPrizesAdmin)
_register(models.RoomBans, RoomBansAdmin)
_register(models.RoomEnterLog, RoomEnterLogAdmin)
_register(models.RoomGameScores, RoomGameScoresAdmin)
_register(models.RoomModels, RoomModelsAdmin)
_register(models.RoomModelsCustom, RoomModelsCustomAdmin)
_register(models.RoomMutes, RoomMutesAdmin)
_register(models.RoomPromotions, RoomPromotionsAdmin)
_register(models.RoomRights, RoomRightsAdmin)
_register(models.RoomTradeLog, RoomTradeLogAdmin)
_register(models.RoomTradeLogItems, RoomTradeLogItemsAdmin)
_register(models.RoomTraxPlaylist, RoomTraxPlaylistAdmin)
_register(models.RoomVotes, RoomVotesAdmin)
_register(models.RoomWordfilter, RoomWordfilterAdmin)
_register(models.Rooms, RoomsAdmin)
_register(models.SanctionLevels, SanctionLevelsAdmin)
_register(models.Sanctions, SanctionsAdmin)
_register(models.Soundtracks, SoundtracksAdmin)
_register(models.SpecialEnables, SpecialEnablesAdmin)
_register(models.SupportCfhCategories, SupportCfhCategoriesAdmin)
_register(models.SupportCfhTopics, SupportCfhTopicsAdmin)
_register(models.SupportIssueCategories, SupportIssueCategoriesAdmin)
_register(models.SupportIssuePresets, SupportIssuePresetsAdmin)
_register(models.SupportPresets, SupportPresetsAdmin)
_register(models.SupportTickets, SupportTicketsAdmin)
_register(models.UserWindowSettings, UserWindowSettingsAdmin)
_register(models.Users, UsersAdmin)
_register(models.UsersAchievements, UsersAchievementsAdmin)
_register(models.UsersAchievementsQueue, UsersAchievementsQueueAdmin)
_register(models.UsersBadges, UsersBadgesAdmin)
_register(models.UsersClothing, UsersClothingAdmin)
_register(models.UsersCurrency, UsersCurrencyAdmin)
_register(models.UsersEffects, UsersEffectsAdmin)
_register(models.UsersFavoriteRooms, UsersFavoriteRoomsAdmin)
_register(models.UsersIgnored, UsersIgnoredAdmin)
_register(models.UsersNavigatorSettings, UsersNavigatorSettingsAdmin)
_register(models.UsersPets, UsersPetsAdmin)
_register(models.UsersRecipes, UsersRecipesAdmin)
_register(models.UsersSavedSearches, UsersSavedSearchesAdmin)
_register(models.UsersSettings, UsersSettingsAdmin)
_register(models.UsersTargetOfferPurchases, UsersTargetOfferPurchasesAdmin)
_register(models.UsersWardrobe, UsersWardrobeAdmin)
_register(models.VoucherHistory, VoucherHistoryAdmin)
_register(models.Vouchers, VouchersAdmin)
_register(models.WiredRewardsGiven, WiredRewardsGivenAdmin)
_register(models.Wordfilter, WordfilterAdmin)
_register(models.YoutubePlaylists, YoutubePlaylistsAdmin)
