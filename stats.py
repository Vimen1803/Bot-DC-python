from cProfile import Profile
import discord, brawlstars, brawlstats, os, re
from discord.ext import commands, tasks
from brawlstats import Brawlers, bstag, Player, Club, Ranking, BattleLog, Client, Members
from brawlstars import PlayerLeaderboard, Player, RankedPlayer, StaticData, Client, BandLeaderboard, Map, Mode, Box, Brawler, InfoBrawler, RankedBand
from datetime import datetime
from functools import wraps
from typing import Union
from brawlstats.errors import NotFoundError

class API:
def __init__(self, base_url, version = 1):
    self.BASE = base_url

