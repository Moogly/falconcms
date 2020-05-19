# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Below is a model extracted from Arcturus MorningStar.

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table


class Achievements(models.Model):
    name = models.CharField(primary_key=True, max_length=64)
    category = models.CharField(max_length=12)
    level = models.IntegerField()
    reward_amount = models.IntegerField()
    reward_type = models.IntegerField()
    points = models.IntegerField(blank=True, null=True)
    progress_needed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'achievements'
        unique_together = (('name', 'level'),)


class AchievementsTalents(models.Model):
    type = models.CharField(max_length=11)
    level = models.IntegerField()
    achievement_ids = models.CharField(max_length=100)
    achievement_levels = models.CharField(max_length=100)
    reward_furni = models.CharField(max_length=100)
    reward_perks = models.CharField(max_length=100)
    reward_badges = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'achievements_talents'


class Bans(models.Model):
    user_id = models.IntegerField(primary_key=True)
    ip = models.CharField(max_length=50)
    machine_id = models.CharField(max_length=255)
    user_staff_id = models.IntegerField()
    timestamp = models.IntegerField()
    ban_expire = models.IntegerField()
    ban_reason = models.CharField(max_length=200)
    type = models.CharField(max_length=7)
    cfh_topic = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bans'


class BotServes(models.Model):
    keys = models.CharField(max_length=128)
    item = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bot_serves'


class Bots(models.Model):
    user_id = models.IntegerField()
    room_id = models.IntegerField()
    name = models.CharField(max_length=25)
    motto = models.CharField(max_length=100)
    figure = models.CharField(max_length=500)
    gender = models.CharField(max_length=1)
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.FloatField()
    rot = models.IntegerField()
    chat_lines = models.CharField(max_length=5112)
    chat_auto = models.CharField(max_length=1)
    chat_random = models.CharField(max_length=1)
    chat_delay = models.IntegerField()
    dance = models.IntegerField()
    freeroam = models.CharField(max_length=1)
    type = models.CharField(max_length=14)
    effect = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bots'


class CalendarRewards(models.Model):
    custom_image = models.CharField(max_length=128)
    credits = models.IntegerField()
    points = models.IntegerField()
    points_type = models.IntegerField()
    badge = models.CharField(max_length=25)
    item_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'calendar_rewards'


class CalendarRewardsClaimed(models.Model):
    user_id = models.IntegerField()
    reward_id = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'calendar_rewards_claimed'


class CameraWeb(models.Model):
    user_id = models.IntegerField()
    room_id = models.IntegerField()
    timestamp = models.IntegerField()
    url = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'camera_web'


class CatalogClothing(models.Model):
    name = models.CharField(max_length=75)
    setid = models.CharField(max_length=75)

    class Meta:
        managed = False
        db_table = 'catalog_clothing'


class CatalogClubOffers(models.Model):
    id = models.IntegerField(primary_key=True)
    enabled = models.CharField(max_length=1)
    name = models.CharField(max_length=35)
    days = models.IntegerField()
    credits = models.IntegerField()
    points = models.IntegerField()
    points_type = models.IntegerField()
    type = models.CharField(max_length=3)
    deal = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'catalog_club_offers'


class CatalogFeaturedPages(models.Model):
    slot_id = models.IntegerField(primary_key=True)
    image = models.CharField(max_length=70)
    caption = models.CharField(max_length=130)
    type = models.CharField(max_length=12)
    expire_timestamp = models.IntegerField()
    page_name = models.CharField(max_length=30)
    page_id = models.IntegerField()
    product_name = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'catalog_featured_pages'


class CatalogItems(models.Model):
    item_ids = models.CharField(max_length=666)
    page_id = models.IntegerField()
    offer_id = models.IntegerField()
    song_id = models.PositiveIntegerField()
    order_number = models.IntegerField()
    catalog_name = models.CharField(max_length=100)
    cost_credits = models.IntegerField()
    cost_points = models.IntegerField()
    points_type = models.IntegerField()
    amount = models.IntegerField()
    limited_sells = models.IntegerField()
    limited_stack = models.IntegerField()
    extradata = models.CharField(max_length=500)
    have_offer = models.CharField(max_length=1)
    club_only = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'catalog_items'


class CatalogItemsLimited(models.Model):
    catalog_item_id = models.IntegerField()
    number = models.IntegerField()
    user_id = models.IntegerField()
    timestamp = models.IntegerField()
    item_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_items_limited'
        unique_together = (('catalog_item_id', 'number'),)


class CatalogPages(models.Model):
    parent_id = models.IntegerField()
    page_layout = models.CharField(max_length=26)
    caption_save = models.CharField(max_length=25)
    caption = models.CharField(max_length=128)
    icon_color = models.IntegerField()
    icon_image = models.IntegerField()
    min_rank = models.IntegerField()
    order_num = models.IntegerField()
    room_id = models.IntegerField()
    visible = models.CharField(max_length=1)
    enabled = models.CharField(max_length=1)
    club_only = models.CharField(max_length=1)
    vip_only = models.CharField(max_length=1)
    page_headline = models.CharField(max_length=1024)
    page_teaser = models.CharField(max_length=64)
    page_special = models.CharField(max_length=2048)
    page_text1 = models.TextField()
    page_text2 = models.TextField()
    page_text_details = models.TextField()
    page_text_teaser = models.TextField()
    includes = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_pages'


class CatalogTargetOffers(models.Model):
    offer_code = models.CharField(max_length=32)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=2048)
    image = models.CharField(max_length=128)
    icon = models.CharField(max_length=128)
    end_timestamp = models.IntegerField()
    credits = models.IntegerField()
    points = models.IntegerField()
    points_type = models.IntegerField()
    purchase_limit = models.IntegerField()
    catalog_item = models.IntegerField()
    vars = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'catalog_target_offers'


class ChatlogsPrivate(models.Model):
    user_from_id = models.IntegerField()
    user_to_id = models.IntegerField()
    message = models.CharField(max_length=255)
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'chatlogs_private'


class ChatlogsRoom(models.Model):
    room_id = models.IntegerField()
    user_from_id = models.IntegerField()
    user_to_id = models.IntegerField()
    message = models.CharField(max_length=255)
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'chatlogs_room'


class Commandlogs(models.Model):
    user_id = models.IntegerField()
    timestamp = models.IntegerField()
    command = models.CharField(max_length=255)
    params = models.CharField(max_length=255)
    succes = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'commandlogs'


class CraftingAltarsRecipes(models.Model):
    altar_id = models.IntegerField()
    recipe_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'crafting_altars_recipes'
        unique_together = (('altar_id', 'recipe_id'),)


class CraftingRecipes(models.Model):
    product_name = models.CharField(unique=True, max_length=32)
    reward = models.IntegerField()
    enabled = models.CharField(max_length=1)
    achievement = models.CharField(max_length=255)
    secret = models.CharField(max_length=1)
    limited = models.CharField(max_length=1)
    remaining = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'crafting_recipes'


class CraftingRecipesIngredients(models.Model):
    recipe_id = models.IntegerField()
    item_id = models.IntegerField()
    amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'crafting_recipes_ingredients'


class EmulatorErrors(models.Model):
    timestamp = models.IntegerField()
    version = models.CharField(max_length=64)
    build_hash = models.CharField(max_length=64)
    type = models.CharField(max_length=32)
    stacktrace = models.TextField()

    class Meta:
        managed = False
        db_table = 'emulator_errors'


class EmulatorSettings(models.Model):
    key = models.CharField(primary_key=True, max_length=100)
    value = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'emulator_settings'


class EmulatorTexts(models.Model):
    key = models.CharField(primary_key=True, max_length=100)
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'emulator_texts'


class GiftWrappers(models.Model):
    sprite_id = models.IntegerField()
    item_id = models.IntegerField()
    type = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'gift_wrappers'


class GroupsItems(models.Model):
    type = models.CharField(max_length=6)
    id = models.IntegerField(primary_key=True)
    firstvalue = models.CharField(max_length=255)
    secondvalue = models.CharField(max_length=2000)
    enabled = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'groups_items'
        unique_together = (('id', 'type'),)


class GuildForumViews(models.Model):
    user_id = models.IntegerField()
    guild_id = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'guild_forum_views'


class Guilds(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    room_id = models.IntegerField()
    state = models.IntegerField()
    rights = models.CharField(max_length=1)
    color_one = models.IntegerField()
    color_two = models.IntegerField()
    badge = models.CharField(max_length=255)
    date_created = models.IntegerField()
    forum = models.CharField(max_length=1)
    read_forum = models.CharField(max_length=8)
    post_messages = models.CharField(max_length=8)
    post_threads = models.CharField(max_length=8)
    mod_forum = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'guilds'


class GuildsElements(models.Model):
    id = models.IntegerField(primary_key=True)
    firstvalue = models.CharField(max_length=300)
    secondvalue = models.CharField(max_length=300)
    type = models.CharField(max_length=50)
    enabled = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'guilds_elements'
        unique_together = (('id', 'type'),)


class GuildsForumsComments(models.Model):
    thread_id = models.IntegerField()
    user_id = models.IntegerField()
    message = models.TextField()
    created_at = models.IntegerField()
    state = models.IntegerField()
    admin_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'guilds_forums_comments'


class GuildsForumsThreads(models.Model):
    guild_id = models.IntegerField(blank=True, null=True)
    opener_id = models.IntegerField(blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    posts_count = models.IntegerField(blank=True, null=True)
    created_at = models.IntegerField(blank=True, null=True)
    updated_at = models.IntegerField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    pinned = models.IntegerField(blank=True, null=True)
    locked = models.IntegerField(blank=True, null=True)
    admin_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guilds_forums_threads'


class GuildsMembers(models.Model):
    guild_id = models.IntegerField()
    user_id = models.IntegerField()
    level_id = models.IntegerField()
    member_since = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'guilds_members'


class HotelviewNews(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=500)
    button_text = models.CharField(max_length=50)
    button_type = models.CharField(max_length=6)
    button_link = models.CharField(max_length=200)
    image = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'hotelview_news'


class Items(models.Model):
    user_id = models.IntegerField()
    room_id = models.IntegerField()
    item_id = models.IntegerField(blank=True, null=True)
    wall_pos = models.CharField(max_length=20)
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.FloatField()
    rot = models.IntegerField()
    extra_data = models.CharField(max_length=1024)
    wired_data = models.CharField(max_length=255)
    limited_data = models.CharField(max_length=10)
    guild_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'items'


class ItemsBase(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    sprite_id = models.IntegerField()
    item_name = models.CharField(max_length=70)
    public_name = models.CharField(max_length=56)
    width = models.IntegerField()
    length = models.IntegerField()
    stack_height = models.FloatField()
    allow_stack = models.CharField(max_length=1)
    allow_sit = models.CharField(max_length=1)
    allow_lay = models.CharField(max_length=1)
    allow_walk = models.CharField(max_length=1)
    allow_gift = models.CharField(max_length=1)
    allow_trade = models.CharField(max_length=1)
    allow_recycle = models.CharField(max_length=1)
    allow_marketplace_sell = models.CharField(max_length=1)
    allow_inventory_stack = models.CharField(max_length=1)
    type = models.CharField(max_length=255)
    interaction_type = models.CharField(max_length=500)
    interaction_modes_count = models.IntegerField()
    vending_ids = models.CharField(max_length=255)
    multiheight = models.CharField(max_length=50)
    customparams = models.CharField(max_length=255)
    effect_id_male = models.IntegerField()
    effect_id_female = models.IntegerField()
    clothing_on_walk = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'items_base'


class ItemsCrackable(models.Model):
    item_id = models.IntegerField(primary_key=True)
    count = models.IntegerField()
    prizes = models.CharField(max_length=255)
    achievement_tick = models.CharField(max_length=64)
    achievement_cracked = models.CharField(max_length=64)
    required_effect = models.IntegerField()
    subscription_duration = models.IntegerField(blank=True, null=True)
    subscription_type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'items_crackable'


class ItemsHighscoreData(models.Model):
    item_id = models.IntegerField()
    user_ids = models.CharField(max_length=500)
    score = models.IntegerField()
    is_win = models.IntegerField(blank=True, null=True)
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'items_highscore_data'


class ItemsHoppers(models.Model):
    item_id = models.IntegerField()
    base_item = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'items_hoppers'


class ItemsPresents(models.Model):
    item_id = models.IntegerField()
    base_item_reward = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'items_presents'


class ItemsTeleports(models.Model):
    teleport_one_id = models.IntegerField()
    teleport_two_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'items_teleports'


class MarketplaceItems(models.Model):
    item_id = models.IntegerField()
    user_id = models.IntegerField()
    price = models.IntegerField()
    timestamp = models.IntegerField()
    sold_timestamp = models.IntegerField()
    state = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'marketplace_items'


class MessengerFriendrequests(models.Model):
    user_to_id = models.IntegerField()
    user_from_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'messenger_friendrequests'


class MessengerFriendships(models.Model):
    user_one_id = models.IntegerField()
    user_two_id = models.IntegerField()
    relation = models.IntegerField()
    friends_since = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'messenger_friendships'


class MessengerOffline(models.Model):
    user_id = models.IntegerField()
    user_from_id = models.IntegerField()
    message = models.CharField(max_length=500)
    sended_on = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'messenger_offline'


class NamechangeLog(models.Model):
    user_id = models.IntegerField()
    old_name = models.CharField(max_length=32)
    new_name = models.CharField(max_length=32)
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'namechange_log'


class NavigatorFilter(models.Model):
    key = models.CharField(primary_key=True, max_length=11)
    field = models.CharField(max_length=32)
    compare = models.CharField(max_length=18)
    database_query = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'navigator_filter'


class NavigatorFlatcats(models.Model):
    min_rank = models.IntegerField()
    caption_save = models.CharField(max_length=32)
    caption = models.CharField(max_length=100)
    can_trade = models.CharField(max_length=1)
    max_user_count = models.IntegerField()
    public = models.CharField(max_length=1)
    list_type = models.IntegerField()
    order_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'navigator_flatcats'


class NavigatorPubliccats(models.Model):
    name = models.CharField(max_length=32)
    image = models.CharField(max_length=1)
    visible = models.CharField(max_length=1)
    order_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'navigator_publiccats'


class NavigatorPublics(models.Model):
    public_cat_id = models.IntegerField()
    room_id = models.IntegerField()
    visible = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'navigator_publics'


class NuxGifts(models.Model):
    type = models.CharField(max_length=4)
    value = models.CharField(max_length=32)
    image = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'nux_gifts'


class OldGuildsForums(models.Model):
    guild_id = models.IntegerField()
    user_id = models.IntegerField()
    subject = models.TextField()
    message = models.TextField()
    state = models.CharField(max_length=15)
    admin_id = models.IntegerField()
    pinned = models.CharField(max_length=1)
    locked = models.CharField(max_length=1)
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'old_guilds_forums'


class OldGuildsForumsComments(models.Model):
    thread_id = models.IntegerField()
    user_id = models.IntegerField()
    timestamp = models.IntegerField()
    message = models.TextField()
    state = models.CharField(max_length=15)
    admin_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'old_guilds_forums_comments'


class Permissions(models.Model):
    rank_name = models.CharField(max_length=25)
    badge = models.CharField(max_length=12)
    level = models.IntegerField()
    room_effect = models.IntegerField()
    log_commands = models.CharField(max_length=1)
    prefix = models.CharField(max_length=5)
    prefix_color = models.CharField(max_length=7)
    cmd_about = models.CharField(max_length=1)
    cmd_alert = models.CharField(max_length=1)
    cmd_allow_trading = models.CharField(max_length=1)
    cmd_badge = models.CharField(max_length=1)
    cmd_ban = models.CharField(max_length=1)
    cmd_blockalert = models.CharField(max_length=1)
    cmd_bots = models.CharField(max_length=1)
    cmd_bundle = models.CharField(max_length=1)
    cmd_calendar = models.CharField(max_length=1)
    cmd_changename = models.CharField(max_length=1)
    cmd_chatcolor = models.CharField(max_length=1)
    cmd_commands = models.CharField(max_length=1)
    cmd_connect_camera = models.CharField(max_length=1)
    cmd_control = models.CharField(max_length=1)
    cmd_coords = models.CharField(max_length=1)
    cmd_credits = models.CharField(max_length=1)
    cmd_danceall = models.CharField(max_length=1)
    cmd_diagonal = models.CharField(max_length=1)
    cmd_disconnect = models.CharField(max_length=1)
    cmd_duckets = models.CharField(max_length=1)
    cmd_ejectall = models.CharField(max_length=1)
    cmd_empty = models.CharField(max_length=1)
    cmd_empty_bots = models.CharField(max_length=1)
    cmd_empty_pets = models.CharField(max_length=1)
    cmd_enable = models.CharField(max_length=1)
    cmd_event = models.CharField(max_length=1)
    cmd_faceless = models.CharField(max_length=1)
    cmd_fastwalk = models.CharField(max_length=1)
    cmd_filterword = models.CharField(max_length=1)
    cmd_freeze = models.CharField(max_length=1)
    cmd_freeze_bots = models.CharField(max_length=1)
    cmd_gift = models.CharField(max_length=1)
    cmd_give_rank = models.CharField(max_length=1)
    cmd_ha = models.CharField(max_length=1)
    acc_can_stalk = models.CharField(max_length=1)
    cmd_hal = models.CharField(max_length=1)
    cmd_invisible = models.CharField(max_length=1)
    cmd_ip_ban = models.CharField(max_length=1)
    cmd_machine_ban = models.CharField(max_length=1)
    cmd_hand_item = models.CharField(max_length=1)
    cmd_happyhour = models.CharField(max_length=1)
    cmd_hidewired = models.CharField(max_length=1)
    cmd_kickall = models.CharField(max_length=1)
    cmd_massbadge = models.CharField(max_length=1)
    cmd_masscredits = models.CharField(max_length=1)
    cmd_massduckets = models.CharField(max_length=1)
    cmd_massgift = models.CharField(max_length=1)
    cmd_masspoints = models.CharField(max_length=1)
    cmd_moonwalk = models.CharField(max_length=1)
    cmd_mimic = models.CharField(max_length=1)
    cmd_multi = models.CharField(max_length=1)
    cmd_mute = models.CharField(max_length=1)
    cmd_pet_info = models.CharField(max_length=1)
    cmd_pickall = models.CharField(max_length=1)
    cmd_plugins = models.CharField(max_length=1)
    cmd_points = models.CharField(max_length=1)
    cmd_promote_offer = models.CharField(max_length=1)
    cmd_pull = models.CharField(max_length=1)
    cmd_push = models.CharField(max_length=1)
    cmd_redeem = models.CharField(max_length=1)
    cmd_reload_room = models.CharField(max_length=1)
    cmd_roomalert = models.CharField(max_length=1)
    cmd_roomcredits = models.CharField(max_length=1)
    cmd_roomeffect = models.CharField(max_length=1)
    cmd_roomgift = models.CharField(max_length=1)
    cmd_roomitem = models.CharField(max_length=1)
    cmd_roommute = models.CharField(max_length=1)
    cmd_roompixels = models.CharField(max_length=1)
    cmd_roompoints = models.CharField(max_length=1)
    cmd_say = models.CharField(max_length=1)
    cmd_say_all = models.CharField(max_length=1)
    cmd_setmax = models.CharField(max_length=1)
    cmd_set_poll = models.CharField(max_length=1)
    cmd_setpublic = models.CharField(max_length=1)
    cmd_setspeed = models.CharField(max_length=1)
    cmd_shout = models.CharField(max_length=1)
    cmd_shout_all = models.CharField(max_length=1)
    cmd_shutdown = models.CharField(max_length=1)
    cmd_sitdown = models.CharField(max_length=1)
    cmd_staffalert = models.CharField(max_length=1)
    cmd_staffonline = models.CharField(max_length=1)
    cmd_summon = models.CharField(max_length=1)
    cmd_summonrank = models.CharField(max_length=1)
    cmd_super_ban = models.CharField(max_length=1)
    cmd_stalk = models.CharField(max_length=1)
    cmd_superpull = models.CharField(max_length=1)
    cmd_take_badge = models.CharField(max_length=1)
    cmd_talk = models.CharField(max_length=1)
    cmd_teleport = models.CharField(max_length=1)
    cmd_trash = models.CharField(max_length=1)
    cmd_transform = models.CharField(max_length=1)
    cmd_unban = models.CharField(max_length=1)
    cmd_unload = models.CharField(max_length=1)
    cmd_unmute = models.CharField(max_length=1)
    cmd_update_achievements = models.CharField(max_length=1)
    cmd_update_bots = models.CharField(max_length=1)
    cmd_update_catalogue = models.CharField(max_length=1)
    cmd_update_config = models.CharField(max_length=1)
    cmd_update_guildparts = models.CharField(max_length=1)
    cmd_update_hotel_view = models.CharField(max_length=1)
    cmd_update_items = models.CharField(max_length=1)
    cmd_update_navigator = models.CharField(max_length=1)
    cmd_update_permissions = models.CharField(max_length=1)
    cmd_update_pet_data = models.CharField(max_length=1)
    cmd_update_plugins = models.CharField(max_length=1)
    cmd_update_polls = models.CharField(max_length=1)
    cmd_update_texts = models.CharField(max_length=1)
    cmd_update_wordfilter = models.CharField(max_length=1)
    cmd_userinfo = models.CharField(max_length=1)
    cmd_word_quiz = models.CharField(max_length=1)
    cmd_warp = models.CharField(max_length=1)
    acc_anychatcolor = models.CharField(max_length=1)
    acc_anyroomowner = models.CharField(max_length=1)
    acc_empty_others = models.CharField(max_length=1)
    acc_enable_others = models.CharField(max_length=1)
    acc_see_whispers = models.CharField(max_length=1)
    acc_superwired = models.CharField(max_length=1)
    acc_supporttool = models.CharField(max_length=1)
    acc_unkickable = models.CharField(max_length=1)
    acc_guildgate = models.CharField(max_length=1)
    acc_moverotate = models.CharField(max_length=1)
    acc_placefurni = models.CharField(max_length=1)
    acc_unlimited_bots = models.CharField(max_length=1)
    acc_unlimited_pets = models.CharField(max_length=1)
    acc_hide_ip = models.CharField(max_length=1)
    acc_not_mimiced = models.CharField(max_length=1)
    acc_chat_no_flood = models.CharField(max_length=1)
    acc_staff_chat = models.CharField(max_length=1)
    acc_staff_pick = models.CharField(max_length=1)
    acc_enteranyroom = models.CharField(max_length=1)
    acc_fullrooms = models.CharField(max_length=1)
    acc_infinite_credits = models.CharField(max_length=1)
    acc_infinite_pixels = models.CharField(max_length=1)
    acc_infinite_points = models.CharField(max_length=1)
    acc_ambassador = models.CharField(max_length=1)
    acc_debug = models.CharField(max_length=1)
    acc_chat_no_limit = models.CharField(max_length=1)
    acc_chat_no_filter = models.CharField(max_length=1)
    acc_nomute = models.CharField(max_length=1)
    acc_guild_admin = models.CharField(max_length=1)
    acc_catalog_ids = models.CharField(max_length=1)
    acc_modtool_ticket_q = models.CharField(max_length=1)
    acc_modtool_user_logs = models.CharField(max_length=1)
    acc_modtool_user_alert = models.CharField(max_length=1)
    acc_modtool_user_kick = models.CharField(max_length=1)
    acc_modtool_user_ban = models.CharField(max_length=1)
    acc_modtool_room_info = models.CharField(max_length=1)
    acc_modtool_room_logs = models.CharField(max_length=1)
    acc_trade_anywhere = models.CharField(max_length=1)
    acc_update_notifications = models.CharField(max_length=1)
    acc_helper_use_guide_tool = models.CharField(max_length=1)
    acc_helper_give_guide_tours = models.CharField(max_length=1)
    acc_helper_judge_chat_reviews = models.CharField(max_length=1)
    acc_floorplan_editor = models.CharField(max_length=1)
    acc_camera = models.CharField(max_length=1)
    acc_ads_background = models.CharField(max_length=1)
    cmd_wordquiz = models.CharField(max_length=1)
    acc_room_staff_tags = models.CharField(max_length=1)
    acc_infinite_friends = models.CharField(max_length=1)
    acc_mimic_unredeemed = models.CharField(max_length=1)
    cmd_update_youtube_playlists = models.CharField(max_length=1)
    cmd_add_youtube_playlist = models.CharField(max_length=1)
    auto_credits_amount = models.IntegerField(blank=True, null=True)
    auto_pixels_amount = models.IntegerField(blank=True, null=True)
    auto_gotw_amount = models.IntegerField(blank=True, null=True)
    auto_points_amount = models.IntegerField(blank=True, null=True)
    acc_mention = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'permissions'


class PetActions(models.Model):
    pet_type = models.AutoField(primary_key=True)
    pet_name = models.CharField(max_length=32)
    offspring_type = models.IntegerField()
    happy_actions = models.CharField(max_length=100)
    tired_actions = models.CharField(max_length=100)
    random_actions = models.CharField(max_length=100)
    can_swim = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pet_actions'


class PetBreeding(models.Model):
    pet_id = models.IntegerField()
    offspring_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pet_breeding'


class PetBreedingRaces(models.Model):
    pet_type = models.IntegerField()
    rarity_level = models.IntegerField()
    breed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pet_breeding_races'


class PetBreeds(models.Model):
    race = models.IntegerField()
    color_one = models.IntegerField()
    color_two = models.IntegerField()
    has_color_one = models.CharField(max_length=1)
    has_color_two = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'pet_breeds'
        unique_together = (('race', 'color_one', 'color_two', 'has_color_one', 'has_color_two'),)


class PetCommands(models.Model):
    pet_id = models.IntegerField()
    command_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pet_commands'


class PetCommandsData(models.Model):
    command_id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=15)
    required_level = models.IntegerField()
    reward_xp = models.IntegerField()
    cost_happyness = models.IntegerField()
    cost_energy = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pet_commands_data'


class PetDrinks(models.Model):
    pet_id = models.IntegerField()
    item_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pet_drinks'


class PetFoods(models.Model):
    pet_id = models.IntegerField()
    item_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pet_foods'


class PetItems(models.Model):
    pet_id = models.IntegerField()
    item_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pet_items'


class PetVocals(models.Model):
    pet_id = models.IntegerField()
    type = models.CharField(max_length=15)
    message = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'pet_vocals'


class Polls(models.Model):
    title = models.CharField(max_length=255)
    thanks_message = models.CharField(max_length=255)
    reward_badge = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'polls'


class PollsAnswers(models.Model):
    poll_id = models.IntegerField()
    user_id = models.IntegerField()
    question_id = models.IntegerField()
    answer = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'polls_answers'
        unique_together = (('poll_id', 'user_id', 'question_id'),)


class PollsQuestions(models.Model):
    parent_id = models.IntegerField()
    poll_id = models.IntegerField()
    order = models.IntegerField()
    question = models.CharField(max_length=255)
    type = models.IntegerField()
    min_selections = models.IntegerField()
    options = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'polls_questions'


class RecyclerPrizes(models.Model):
    rarity = models.IntegerField()
    item_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'recycler_prizes'


class RoomBans(models.Model):
    room_id = models.IntegerField()
    user_id = models.IntegerField()
    ends = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_bans'


class RoomEnterLog(models.Model):
    room_id = models.IntegerField()
    user_id = models.IntegerField()
    timestamp = models.IntegerField()
    exit_timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_enter_log'


class RoomGameScores(models.Model):
    room_id = models.IntegerField()
    game_start_timestamp = models.IntegerField()
    game_name = models.CharField(max_length=64)
    user_id = models.IntegerField()
    team_id = models.IntegerField()
    score = models.IntegerField()
    team_score = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_game_scores'


class RoomModels(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    door_x = models.IntegerField()
    door_y = models.IntegerField()
    door_dir = models.IntegerField()
    heightmap = models.TextField()
    public_items = models.TextField()
    club_only = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'room_models'


class RoomModelsCustom(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    door_x = models.IntegerField()
    door_y = models.IntegerField()
    door_dir = models.IntegerField()
    heightmap = models.TextField()

    class Meta:
        managed = False
        db_table = 'room_models_custom'


class RoomMutes(models.Model):
    room_id = models.IntegerField()
    user_id = models.IntegerField()
    ends = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_mutes'


class RoomPromotions(models.Model):
    room_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=127)
    description = models.CharField(max_length=1024)
    end_timestamp = models.IntegerField()
    start_timestamp = models.IntegerField()
    category = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_promotions'


class RoomRights(models.Model):
    room_id = models.IntegerField()
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_rights'


class RoomTradeLog(models.Model):
    user_one_id = models.IntegerField()
    user_two_id = models.IntegerField()
    user_one_ip = models.CharField(max_length=45)
    user_two_ip = models.CharField(max_length=45)
    timestamp = models.IntegerField()
    user_one_item_count = models.IntegerField()
    user_two_item_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_trade_log'


class RoomTradeLogItems(models.Model):
    id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField()
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_trade_log_items'
        unique_together = (('id', 'item_id', 'user_id'),)


class RoomTraxPlaylist(models.Model):
    room_id = models.IntegerField()
    item_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_trax_playlist'


class RoomVotes(models.Model):
    user_id = models.IntegerField()
    room_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_votes'


class RoomWordfilter(models.Model):
    room_id = models.IntegerField()
    word = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'room_wordfilter'
        unique_together = (('room_id', 'word'),)


class Rooms(models.Model):
    owner_id = models.IntegerField()
    owner_name = models.CharField(max_length=25)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=512)
    model = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    state = models.CharField(max_length=9)
    users = models.IntegerField()
    users_max = models.IntegerField()
    guild_id = models.IntegerField()
    category = models.IntegerField()
    score = models.IntegerField()
    paper_floor = models.CharField(max_length=5)
    paper_wall = models.CharField(max_length=5)
    paper_landscape = models.CharField(max_length=5)
    thickness_wall = models.IntegerField()
    wall_height = models.IntegerField()
    thickness_floor = models.IntegerField()
    moodlight_data = models.CharField(max_length=254)
    tags = models.CharField(max_length=500)
    is_public = models.CharField(max_length=1)
    is_staff_picked = models.CharField(max_length=1)
    allow_other_pets = models.CharField(max_length=1)
    allow_other_pets_eat = models.CharField(max_length=1)
    allow_walkthrough = models.CharField(max_length=1)
    allow_hidewall = models.CharField(max_length=1)
    chat_mode = models.IntegerField()
    chat_weight = models.IntegerField()
    chat_speed = models.IntegerField()
    chat_hearing_distance = models.IntegerField()
    chat_protection = models.IntegerField()
    override_model = models.CharField(max_length=1)
    who_can_mute = models.IntegerField()
    who_can_kick = models.IntegerField()
    who_can_ban = models.IntegerField()
    poll_id = models.IntegerField()
    roller_speed = models.IntegerField()
    promoted = models.CharField(max_length=1)
    trade_mode = models.IntegerField()
    move_diagonally = models.CharField(max_length=1)
    jukebox_active = models.CharField(max_length=1)
    hidewired = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'rooms'


class SanctionLevels(models.Model):
    level = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=5)
    hour_length = models.IntegerField()
    probation_days = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sanction_levels'


class Sanctions(models.Model):
    habbo_id = models.IntegerField()
    sanction_level = models.IntegerField()
    probation_timestamp = models.IntegerField()
    reason = models.CharField(max_length=255)
    trade_locked_until = models.IntegerField()
    is_muted = models.IntegerField()
    mute_duration = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sanctions'


class Soundtracks(models.Model):
    code = models.CharField(max_length=32)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    track = models.TextField()
    length = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'soundtracks'


class SpecialEnables(models.Model):
    effect_id = models.IntegerField(unique=True)
    min_rank = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'special_enables'


class SupportCfhCategories(models.Model):
    name_internal = models.CharField(max_length=255, blank=True, null=True)
    name_external = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'support_cfh_categories'


class SupportCfhTopics(models.Model):
    category_id = models.IntegerField(blank=True, null=True)
    name_internal = models.CharField(max_length=255, blank=True, null=True)
    name_external = models.CharField(max_length=255, blank=True, null=True)
    action = models.CharField(max_length=11, blank=True, null=True)
    ignore_target = models.CharField(max_length=1)
    auto_reply = models.TextField(blank=True, null=True)
    default_sanction = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'support_cfh_topics'


class SupportIssueCategories(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'support_issue_categories'


class SupportIssuePresets(models.Model):
    category = models.IntegerField()
    name = models.CharField(max_length=100)
    message = models.CharField(max_length=300)
    reminder = models.CharField(max_length=100)
    ban_for = models.IntegerField()
    mute_for = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'support_issue_presets'


class SupportPresets(models.Model):
    type = models.CharField(max_length=4)
    preset = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'support_presets'


class SupportTickets(models.Model):
    state = models.IntegerField()
    type = models.IntegerField()
    timestamp = models.IntegerField()
    score = models.IntegerField()
    sender_id = models.IntegerField()
    reported_id = models.IntegerField()
    room_id = models.IntegerField()
    mod_id = models.IntegerField()
    issue = models.CharField(max_length=500)
    category = models.IntegerField()
    group_id = models.IntegerField()
    thread_id = models.IntegerField()
    comment_id = models.IntegerField()
    photo_item_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'support_tickets'


class UserWindowSettings(models.Model):
    user_id = models.IntegerField()
    x = models.IntegerField()
    y = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    open_searches = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'user_window_settings'


class Users(models.Model):
    username = models.CharField(unique=True, max_length=25)
    real_name = models.CharField(max_length=25)
    password = models.CharField(max_length=64)
    mail = models.CharField(max_length=25)
    mail_verified = models.CharField(max_length=1)
    account_created = models.IntegerField()
    account_day_of_birth = models.IntegerField()
    last_login = models.IntegerField()
    last_online = models.IntegerField()
    motto = models.CharField(max_length=127)
    look = models.CharField(max_length=255)
    gender = models.CharField(max_length=1)
    rank = models.IntegerField()
    credits = models.IntegerField()
    pixels = models.IntegerField()
    points = models.IntegerField()
    online = models.CharField(max_length=1)
    auth_ticket = models.CharField(max_length=255)
    ip_register = models.CharField(max_length=45)
    ip_current = models.CharField(max_length=45)
    machine_id = models.CharField(max_length=64)
    home_room = models.IntegerField()

    def __str__(self):
        return self.username

    class Meta:
        managed = False
        db_table = 'users'


class UsersAchievements(models.Model):
    user_id = models.IntegerField()
    achievement_name = models.CharField(max_length=255)
    progress = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users_achievements'


class UsersAchievementsQueue(models.Model):
    user_id = models.IntegerField()
    achievement_id = models.IntegerField()
    amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users_achievements_queue'
        unique_together = (('user_id', 'achievement_id'),)


class UsersBadges(models.Model):
    user_id = models.IntegerField()
    slot_id = models.IntegerField()
    badge_code = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'users_badges'


class UsersClothing(models.Model):
    user_id = models.IntegerField()
    clothing_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users_clothing'
        unique_together = (('user_id', 'clothing_id'),)


class UsersCurrency(models.Model):
    user_id = models.IntegerField(primary_key=True)
    type = models.IntegerField()
    amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users_currency'
        unique_together = (('user_id', 'type'),)


class UsersEffects(models.Model):
    user_id = models.IntegerField()
    effect = models.IntegerField()
    duration = models.IntegerField()
    activation_timestamp = models.IntegerField()
    total = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users_effects'
        unique_together = (('user_id', 'effect'),)


class UsersFavoriteRooms(models.Model):
    user_id = models.IntegerField()
    room_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users_favorite_rooms'
        unique_together = (('user_id', 'room_id'),)
        verbose_name_plural = "Users Favorite Rooms"


class UsersIgnored(models.Model):
    user_id = models.IntegerField()
    target_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users_ignored'
        verbose_name_plural = "Users Ignored"


class UsersNavigatorSettings(models.Model):
    user_id = models.IntegerField()
    caption = models.CharField(max_length=128)
    list_type = models.CharField(max_length=10)
    display = models.CharField(max_length=9)

    class Meta:
        managed = False
        db_table = 'users_navigator_settings'
        verbose_name_plural = "Users Navigator Settings"


class UsersPets(models.Model):
    user_id = models.IntegerField()
    room_id = models.IntegerField()
    name = models.CharField(max_length=15)
    race = models.IntegerField()
    type = models.IntegerField()
    color = models.CharField(max_length=6)
    happyness = models.IntegerField()
    experience = models.IntegerField()
    energy = models.IntegerField()
    hunger = models.IntegerField()
    thirst = models.IntegerField()
    respect = models.IntegerField()
    created = models.IntegerField()
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.FloatField()
    rot = models.IntegerField()
    hair_style = models.IntegerField()
    hair_color = models.IntegerField()
    saddle = models.CharField(max_length=1)
    ride = models.CharField(max_length=1)
    mp_type = models.IntegerField()
    mp_color = models.IntegerField()
    mp_nose = models.IntegerField()
    mp_nose_color = models.IntegerField()
    mp_eyes = models.IntegerField()
    mp_eyes_color = models.IntegerField()
    mp_mouth = models.IntegerField()
    mp_mouth_color = models.IntegerField()
    mp_death_timestamp = models.IntegerField()
    mp_breedable = models.CharField(max_length=1)
    mp_allow_breed = models.CharField(max_length=1)
    gnome_data = models.CharField(max_length=80)
    mp_is_dead = models.IntegerField()
    saddle_item_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_pets'
        verbose_name_plural = "Users Pets"


class UsersRecipes(models.Model):
    user_id = models.IntegerField()
    recipe = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users_recipes'
        unique_together = (('user_id', 'recipe'),)
        verbose_name_plural = "Users Recipes"


class UsersSavedSearches(models.Model):
    search_code = models.CharField(max_length=255)
    filter = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users_saved_searches'
        verbose_name_plural = "Users Saved Searches"


class UsersSettings(models.Model):
    user_id = models.IntegerField()
    credits = models.IntegerField()
    achievement_score = models.IntegerField()
    daily_respect_points = models.IntegerField()
    daily_pet_respect_points = models.IntegerField()
    respects_given = models.IntegerField()
    respects_received = models.IntegerField()
    guild_id = models.IntegerField()
    can_change_name = models.CharField(max_length=1)
    can_trade = models.CharField(max_length=1)
    is_citizen = models.CharField(max_length=1)
    citizen_level = models.IntegerField()
    helper_level = models.IntegerField()
    cfh_send = models.IntegerField()
    cfh_abusive = models.IntegerField()
    cfh_warnings = models.IntegerField()
    cfh_bans = models.IntegerField()
    block_following = models.CharField(max_length=1)
    block_friendrequests = models.CharField(max_length=1)
    block_roominvites = models.CharField(max_length=1)
    volume_system = models.IntegerField()
    volume_furni = models.IntegerField()
    volume_trax = models.IntegerField()
    old_chat = models.CharField(max_length=1)
    block_camera_follow = models.CharField(max_length=1)
    chat_color = models.IntegerField()
    home_room = models.IntegerField()
    online_time = models.IntegerField()
    tags = models.CharField(max_length=255)
    club_expire_timestamp = models.IntegerField()
    login_streak = models.IntegerField()
    rent_space_id = models.IntegerField()
    rent_space_endtime = models.IntegerField()
    hof_points = models.IntegerField()
    block_alerts = models.CharField(max_length=1)
    talent_track_citizenship_level = models.IntegerField()
    talent_track_helpers_level = models.IntegerField()
    ignore_bots = models.CharField(max_length=1)
    ignore_pets = models.CharField(max_length=1)
    nux = models.CharField(max_length=1)
    mute_end_timestamp = models.IntegerField()
    allow_name_change = models.CharField(max_length=1)
    perk_trade = models.CharField(max_length=1)
    forums_post_count = models.IntegerField(blank=True, null=True)
    ui_flags = models.IntegerField()
    has_gotten_default_saved_searches = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users_settings'
        verbose_name_plural = "Users Settings"


class UsersTargetOfferPurchases(models.Model):
    user_id = models.IntegerField()
    offer_id = models.IntegerField()
    state = models.IntegerField()
    amount = models.IntegerField()
    last_purchase = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users_target_offer_purchases'
        unique_together = (('user_id', 'offer_id'),)
        verbose_name_plural = "Users Target Offer Purchases"


class UsersWardrobe(models.Model):
    user_id = models.IntegerField()
    slot_id = models.IntegerField()
    look = models.CharField(max_length=255)
    gender = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'users_wardrobe'


class VoucherHistory(models.Model):
    voucher_id = models.IntegerField()
    user_id = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'voucher_history'
        verbose_name_plural = "Voucher History"


class Vouchers(models.Model):
    code = models.CharField(max_length=10)
    credits = models.IntegerField()
    points = models.IntegerField()
    points_type = models.IntegerField()
    catalog_item_id = models.IntegerField()
    amount = models.IntegerField()
    limit = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vouchers'
        verbose_name_plural = "Vouchers"


class WiredRewardsGiven(models.Model):
    wired_item = models.IntegerField()
    user_id = models.IntegerField()
    reward_id = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wired_rewards_given'


class Wordfilter(models.Model):
    key = models.CharField(unique=True, max_length=255, primary_key=True)
    replacement = models.CharField(max_length=16)
    hide = models.CharField(max_length=1)
    report = models.CharField(max_length=1)
    mute = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wordfilter'


class YoutubePlaylists(models.Model):
    item_id = models.IntegerField()
    playlist_id = models.CharField(max_length=255)
    order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'youtube_playlists'
        unique_together = (('item_id', 'playlist_id', 'order'),)
        verbose_name_plural = "Youtube Playlists"
