#You might want to change these
DEFAULT_PORT = 8999
OSD_DURATION = 3000
MPC_OSD_POSITION = 2 #Right corner, 1 for left
MPLAYER_OSD_LEVEL = 1
UI_TIME_FORMAT = "[%X] "
DEFAULT_ROOM = 'default'
DEFAULT_CONFIG_NAME = ".syncplay"

#Changing these might be ok
REWIND_THRESHOLD = 4
SEEK_THRESHOLD = 1
SLOWDOWN_RATE = 0.95
SLOWDOWN_KICKIN_THRESHOLD = 1.5
SLOWDOWN_RESET_THRESHOLD = 0.1
DIFFFERENT_DURATION_THRESHOLD = 1
PROTOCOL_TIMEOUT = 5
RECONNECT_RETRIES = 10


#Usually there's no need to adjust these
COMMANDS_UNDO = ["u", "undo", "revert"]
COMMANDS_LIST = ["l", "list", "users"]
COMMANDS_PAUSE = ["p", "play", "pause"]
COMMANDS_ROOM = ["r", "room"]
COMMANDS_HELP = ['help', 'h', '?', '/?', '\?']
MPC_PATHS = [
             "C:\Program Files (x86)\MPC-HC\mpc-hc.exe",
             "C:\Program Files\MPC-HC\mpc-hc.exe",
             "C:\Program Files\MPC-HC\mpc-hc64.exe",
             "C:\Program Files\Media Player Classic - Home Cinema\mpc-hc.exe",
             "C:\Program Files\Media Player Classic - Home Cinema\mpc-hc64.exe",
             "C:\Program Files (x86)\Media Player Classic - Home Cinema\mpc-hc.exe",
             "C:\Program Files (x86)\K-Lite Codec Pack\Media Player Classic\mpc-hc.exe",
             "C:\Program Files\K-Lite Codec Pack\Media Player Classic\mpc-hc.exe",
             "C:\Program Files (x86)\Combined Community Codec Pack\MPC\mpc-hc.exe",
             "C:\Program Files\MPC HomeCinema (x64)\mpc-hc64.exe",
             ]

#Changing these is usually not something you're looking for
PLAYER_ASK_DELAY = 0.1
PING_MOVING_AVERAGE_WEIGHT = 0.85
MPC_OPEN_MAX_WAIT_TIME = 10
MPC_LOCK_WAIT_TIME = 0.2
MPC_RETRY_WAIT_TIME = 0.01
MPC_MAX_RETRIES = 30
MPC_PAUSE_TOGGLE_DELAY = 0.05

#These are not changes you're looking for
MPLAYER_SLAVE_ARGS = [ '-slave', '-msglevel', 'all=1:global=4']
MPLAYER_ANSWER_REGEX = "^ANS_([a-zA-Z_]+)=(.+)$"
UI_COMMAND_REGEX = r"^(?P<command>[^\ ]+)(?:\ (?P<parameter>.+))?"
UI_OFFSET_REGEX = r"^(?:o|offset)\ ?(?P<sign>[/+-])?(?P<time>\d{1,4}(?:[^\d\.](?:\d{1,6})){0,2}(?:\.(?:\d{1,3}))?)$"
UI_SEEK_REGEX = r"^(?:s|seek)?\ ?(?P<sign>[+-])?(?P<time>\d{1,4}(?:[^\d\.](?:\d{1,6})){0,2}(?:\.(?:\d{1,3}))?)$"
PARSE_TIME_REGEX = r'(:?(?:(?P<hours>\d+?)[^\d\.])?(?:(?P<minutes>\d+?))?[^\d\.])?(?P<seconds>\d+?)(?:\.(?P<miliseconds>\d+?))?$'
