# Copyright (c) 2021 xhrvan
# Part of: Nexa-Userbot

from . import nexa_mongodb

nexaub_conf = nexa_mongodb["config_db"]

# Database for log channel
async def set_log_channel(tgcc_id):
    log_chanel_id = tgcc_id
    p_log_c_id = await nexaub_conf.find_one({"_id": "LOG_CHANNEL_ID"})
    if p_log_c_id:
        return True
    else:
        await nexaub_conf.insert_one({"_id": "LOG_CHANNEL_ID", "nexaub_conf": log_chanel_id})

async def get_log_channel():
    log_channel = await nexaub_conf.find_one({"_id": "LOG_CHANNEL_ID"})
    if log_channel:
        return int(log_channel["nexaub_conf"])
    else:
        return None

# Database for custom alive message

async def set_custom_alive_msg(a_text=None):
    if a_text is None:
        alive_msg = "Heya, I'm Using Nexa Userbot"
    else:
        alive_msg = a_text
    p_alive_msg = await nexaub_conf.find_one({"_id": "CUSTOM_ALIVE_MSG"})
    if p_alive_msg:
        await nexaub_conf.update_one({"_id": "CUSTOM_ALIVE_MSG"}, {"$set": {"nexaub_conf": alive_msg}})
    else:
        await nexaub_conf.insert_one({"_id": "CUSTOM_ALIVE_MSG", "nexaub_conf": alive_msg})

async def get_custom_alive_msg():
    alive_msg = await nexaub_conf.find_one({"_id": "CUSTOM_ALIVE_MSG"})
    if alive_msg:
        return alive_msg["nexaub_conf"]
    else:
        return None

# Databse for set cutom variable
async def set_custom_var(var, value):
    p_variable = await nexaub_conf.find_one({"_id": var})
    if p_variable:
        await nexaub_conf.update_one({"_id": var}, {"$set": {"nexaub_conf": value}})
    else:
        await nexaub_conf.insert_one({"_id": var, "nexaub_conf": value})

async def get_custom_var(var):
    custom_var = await nexaub_conf.find_one({"_id": var})
    if not custom_var:
        return None
    else:
        g_custom_var = custom_var["nexaub_conf"]
        return g_custom_var
