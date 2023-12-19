from PATAKA.core.bot import PATAKA
from PATAKA.core.dir import dirr
from PATAKA.core.git import git
from PATAKA.core.userbot import Userbot
from PATAKA.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = PATAKA()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
